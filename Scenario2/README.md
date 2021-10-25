# Metrics to be Captured

#### Solution for secnrio 2

## Metrics

### Infrastructre Metrics

- #### Uptime
    - one of the most basic metrics, uptime or availability is the gold standard for measuring the  availability of a service
    - Uptime is most commonly measured via a ping service, Configure probes or scripts to run on a fixed interval such as every minute to probe a specific endpoint such as `/health` or `/status`
- #### CPU usage
    - Cpu usage is one of the most important metric to check application responsiveness
    - High Server CPU usage can mean the server or virtual machine is oversubscribed or performance bug in the application
    - CPU usage can be measured by using multiple linux commands ie. `top`
- #### Memory usage
    - Memory usage is good way to measure resource utilization
    - high memory usage can be an indicator of servers overloaded or low memory usage can either be downsized or have additional services allocated to that VM to consume additional memory
    - Memory usage can be measured by using multiple linux commands ie. `PS` `top`
    - #### total threads count
        - As part of memory usage metric we should also monitor the number of the threads that currently running.
        - If the count exceeds the max count  this is effect CPU and memory usage of the VM
- #### Disk space availability
    - Disk space metric is good way to prevent the VM running out of space which can cause application unavailability
    - Disk usage can be measured by using multiple linux commands ie. `DF` `DS`
- #### Network connection
    - There are many reasons to monitor the network activity, to check to make sure that there are no malicious applications creating suspicious network activity, or simply want to know if any processes are working accordingly.
    - #### network erros
        - part of checking network availablilty we will have to check rate of network errors if those error are harmful 
        - we can monitor these erros by using multiple commands or tools like `ifconfig`, `netatat`, `traceroute` 
    - #### tcp established
        - metric to check the number of tcp connection established

### Application Metrics

- #### Request per minute
    -  Monitoring this metric can alert to spikes in incoming web traffic, whether legitimate or nefarious, or sudden drops, which are usually indicative of problems. 
    - A drastic change in requests per second can alert to problems brewing somewhere in the environment 
- #### Average and max latency
    - One of the most important metrics to track application performances.
    - Tracking latency of multiple endpoints would give a idea which endpoint is actually causing the latency.
    - monitoring the latency would help solve issue before it escalate to major issue
- #### Error rate
    - Its critical track the number of non 200s status code, this help to measure how buggy and error prone application is
    - #### server errors
        - `5XX's` error would imply either the service is unavailable or bad gateway
        - this can help in determining which particulate upstream server is causing it
    - #### Application errors
        - Capturing rate of `4xx's` error would help identify issue if its is present in the proxy,ie `404` path not found or if the authentication is buggy
        - Many `401` Unauthorized errors from one specific geo region could imply bots are attempting to hack application this can be prevented by monitoring this metric.

### Solution
- We can capture the above metric and as well setup alerts to effectively solve the issue before the application goes unresponsive by writing multiple scripts to capture and alert the user accordingly.
- The best approach would be use monitoring tools like `prometheus`, `new relic`, `datadog` `Grafana` etc,
these tools would run agent(a light weight process) on the target machines which would capture the different system and application metrics.
- These metrics can be visualized which would helpfully to identify any anomalies in the pattern
- We can set alerts on metric to trigger if the value of certain metric cross a threshold value
- We can setup recover steps if alert is triggered this would help solve level 1 issue without need of user intervention.
- We can setup prometheus by following [steps](https://prometheus.io/docs/introduction/first_steps/)

### Challenges
- Challenges faced in using 3rd party monitoring tool would be to make sure the monitoring agents are running in all the hosts and are sending data to the main application.
- Monitoring tool cluster has to be highly available and maintained.
- The cluster has be monitored to check if its always showing accurate data.
- Based on type of the cluster we will have to be using multiple montioring tools, like `prometheus` and `grafana` for infrastructure monitoring and `dynatrace` for cluster monitoring.


