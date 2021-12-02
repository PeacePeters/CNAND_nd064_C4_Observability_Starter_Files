**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

<img width="891" alt="Monitoring-Installation" src="https://user-images.githubusercontent.com/68206315/144473466-666ec20f-3e27-4260-b26f-b39e75db005a.png">


## Setup the Jaeger and Prometheus source

<img width="1264" alt="Granfana" src="https://user-images.githubusercontent.com/68206315/144473599-0ca95b4b-2955-42dc-8c41-417a3788acba.png">

## Create a Basic Dashboard

<img width="1264" alt="Basic-Dashboard" src="https://user-images.githubusercontent.com/68206315/144473685-1636b6a7-8db9-435d-b35b-54e6121f7692.png">


## Describe SLO/SLI

Service-Level Indicator (SLI)s are specific measureable metrics of a service level that tells us about the actual performance compared to the defined SLO. For an SLO of *monthly uptime*, the SLI can be achieved by measuring the uptime over the month, and maintaining the total uptime ratio as the SLO indicates. For instance, if the target SLO is 99.9% uptime and the actual value achieved is 99.45%, then SLI of `99.45%` uptime is the actual performance level of the service.

*Request Response Time* SLO can be obtained by measuring the precentage of requests that achieve a certain request response time as defined in the SLO, and maintain that ratio to be below a certain level as the SLO indicates. An example is shown below;
SLO - 99.9% requests should return in 50ms monthly
SLI - 99.5% requests return in 50ms in the past month.

## Creating SLI metrics. 

- Number of requests with 20x return codes
- Number of requests with 40x or 50x return codes
- Uptime - Total instance uptime in hours per month
+ Failure rate - Total instance downtime in hours per month
+ Resource capacity - CPU usage per month

## Create a Dashboard to measure our SLIs

<img width="1270" alt="SLIs" src="https://user-images.githubusercontent.com/68206315/144516729-f8d24702-4202-4c86-a89f-c1c9c19d720b.png">

## Tracing our Flask App

<img width="1274" alt="Jaeger-Span" src="https://user-images.githubusercontent.com/68206315/144475698-75a9ad51-54c7-454d-9451-8ff589e4d12c.png">

<img width="1274" alt="Jaeger-Grafana" src="https://user-images.githubusercontent.com/68206315/144475764-c670bbf3-0b60-4a61-a58d-67fe6fcf82b1.png">

## Jaeger in Dashboards

<img width="1270" alt="Jaeger-metrics" src="https://user-images.githubusercontent.com/68206315/144477475-a4942190-b890-4144-a155-34cf7a9043cc.png">


## Report Error

TROUBLE TICKET

Name: 405 Error on backend/app/app.py

Date: Nov 13 2021, 11:50 AM

Subject: Backend can't acces MongoDB

Affected Area: Backend Service

Severity: High

Description: The /star endpoint throws a 405 error when accessing it. This is caused by the absence of MongoDB URL which makes it available for the cluster. We need to deploy MongoDB and ensure it is avalable for the cluster. Here is the trace span mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb


## Creating SLIs and SLOs

SLO - Application will have 99.95% uptime per month

SLIs
+ 99.95% uptime per month
- Failure rate: 0.05% error rate per month
* 99.5% of requests returns in 50ms per month
- Resource capcity: CPU, RAM usage per pod.

## Building KPIs for our plan

- Uptime: Sucessful requests during pod uptime.
  * Uptime for each pod 
  + Uptime for backend and frontend services measured with 24 hours

+ Failure rate: Number of requests that are failing.
  * Number of HTTP 500 responses per day
  - Number of HTTP 200 responses per day

+ Response time for requests: This helps us know the latency of our service which in part tells us level of performance of our application.
  * Requests per second: Number of successful Flask requests per second.
  + Errors per second: Number of failed (non HTTP 200) responses per second.

* Resource capacity: Tells us the overall capacity of a service.
  + CPU usage per pod
  - Memory usage per pod (Cached and free memory of node)

## Final Dashboard

<img width="1268" alt="SLIs2" src="https://user-images.githubusercontent.com/68206315/144477744-ee29115d-9811-4e0a-8f1f-78e3c0308a5c.png">

<img width="1270" alt="SLIs3" src="https://user-images.githubusercontent.com/68206315/144477700-c6992c8b-c7f4-4e0d-8420-6394324a91bd.png">

+ *Uptime*: measures the uptime of each pod.
- *Frontend & Backend Uptime*: queries the uptime of the frontend and backend services
- *40X and 50X errors code*: measures HTTP 40X and 50X errors of the Backend and Frontend services.
* *Total successful request*: queries for all successful requests.
- *CPU usage*: measures CPU usage of Flask app.
+ *Memory usage*: is the memory usage of the Flask app.
- *Requests per second*: measures number of successful Flask requests per second.
+ *Errors per second*: is a graph that measures number of failed (non HTTP 200) responses per second.

