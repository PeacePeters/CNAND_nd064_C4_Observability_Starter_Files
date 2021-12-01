import logging
from os import getenv
from flask import Flask, render_template, request, jsonify
import time
import random
import pymongo
from flask_pymongo import PyMongo
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)

metrics = PrometheusMetrics(app,group_by='endpoint')
# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')
endpoint_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)

JAEGER_AGENT_HOST = getenv('JAEGER_AGENT_HOST', 'localhost')

@app.route('/error')
@endpoint_counter
def oops():
    return ':(', 500

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'local_agent': {'reporting_host': JAEGER_AGENT_HOST},
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('backend')

@app.route('/')
@endpoint_counter
def homepage(): 
    with tracer.start_span('hello-world'):
        return "Hello World"

@app.route('/api')
@endpoint_counter
def my_api():
    with tracer.start_span('api'):
        answer = "something"
    return jsonify(repsonse=answer)

# This will return 405 error
@app.route('/star', methods=['POST'])
@endpoint_counter
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

@app.route('/healthz')
@endpoint_counter
def healthcheck():
    app.logger.info('Status request successfull')
    return jsonify({"result": "OK - healthy"})

# register additional default metrics
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

if __name__ == "__main__":
    app.run(threaded=True)
