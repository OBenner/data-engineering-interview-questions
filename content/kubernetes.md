[Interview questions](full.md)
# Kubernetes
+ [How to do maintenance activity on the K8 node?](#How-to-do-maintenance-activity-on-the-K8-node)
+ [How do we control the resource usage of POD?](#How-do-we-control-the-resource-usage-of-POD)
+ [What are the various K8's services running on nodes and describe the role of each service?](#What-are-the-various-K8's-services-running-on-nodes-and-describe-the-role-of-each-service)
+ [What is PDB (Pod Disruption Budget)?](#What-is-PDB-(Pod-Disruption-Budget))
+ [WhatвЂ™s the init container and when it can be used?](#WhatвЂ™s-the-init-container-and-when-it-can-be-used)
+ [What is the role of Load Balance in Kubernetes?](#What-is-the-role-of-Load-Balance-in-Kubernetes)
+ [What are the various things that can be done to increase Kubernetes security?](#What-are-the-various-things-that-can-be-done-to-increase-Kubernetes-security)
+ [How to monitor the Kubernetes cluster?](#How-to-monitor-the-Kubernetes-cluster)
+ [How to get the central logs from POD?](#How-to-get-the-central-logs-from-POD)
+ [How to turn the service defined below in the spec into an external one?](#How-to-turn-the-service-defined-below-in-the-spec-into-an-external-one)
+ [How to configure TLS with Ingress?](#How-to-configure-TLS-with-Ingress)
+ [Why use namespaces? What is the problem with using the default namespace?](#Why-use-namespaces?-What-is-the-problem-with-using-the-default-namespace)
+ [In the following file which service and in which namespace is referred?](#In-the-following-file-which-service-and-in-which-namespace-is-referred)
+ [What is an Operator?](#What-is-an-Operator)
+ [Why do we need Operators?](#Why-do-we-need-Operators)
+ [What is GKE?](#What-is-GKE)
+ [What is Ingress Default Backend?](#What-is-Ingress-Default-Backend)
+ [How to run Kubernetes locally?](#How-to-run-Kubernetes-locally)
+ [What is Kubernetes Load Balancing?](#What-is-Kubernetes-Load-Balancing)
+ [What the following in the Deployment configuration file mean?](#What-the-following-in-the-Deployment-configuration-file-mean)
+ [What is the difference between Docker Swarm and Kubernetes?](#What-is-the-difference-between-Docker-Swarm-and-Kubernetes)
+ [How to troubleshoot if the POD is not getting scheduled?](#How-to-troubleshoot-if-the-POD-is-not-getting-scheduled)
+ [How to run a POD on a particular node?](#How-to-run-a-POD-on-a-particular-node)
+ [What are the different ways to provide external network connectivity to K8?](#What-are-the-different-ways-to-provide-external-network-connectivity-to-K8)
+ [How can we forward the port 8080 container -> 8080 service -> 8080 ingress -> 80 browser and how it can be done?](#How-can-we-forward-the-port-8080-container-to-8080-service-to-8080-ingress-to-80-browser-and-how-it-can-be-done)
[Table of Contents](#Kubernetes)

## How to do maintenance activity on the K8 node?
Whenever there are security patches available the Kubernetes administrator has to perform the maintenance task to apply the security patch to the running container in order to prevent it from vulnerability, which is often an unavoidable part of the administration. The following two commands are useful to safely drain the K8s node.

kubectl cordon
kubectl drain –ignore-daemon set
The first command moves the node to maintenance mode or makes the node unavailable, followed by kubectl drain which will finally discard the pod from the node. After the drain command is a success you can perform maintenance.

Note: If you wish to perform maintenance on a single pod following two commands can be issued in order:

kubectl get nodes: to list all the nodes
kubectl drain <node name>: drain a particular node

[Table of Contents](#Kubernetes)

## How do we control the resource usage of POD?
With the use of limit and request resource usage of a POD can be controlled.
Request: The number of resources being requested for a container. If a container exceeds its request for resources, it can be throttled back down to its request.

Limit: An upper cap on the resources a single container can use. If it tries to exceed this predefined limit it can be terminated if K8's decides that another container needs these resources. If you are sensitive towards pod restarts, it makes sense to have the sum of all container resource limits equal to or less than the total resource capacity for your cluster.
Example:

apiVersion: v1
kind: Pod
metadata:
name: demo
spec:
containers:
- name: example1
  image:example/example1
  resources:
  requests:
  memory: "_Mi"
  cpu: "_m"
  limits:
  memory: "_Mi"
  cpu: "_m"

[Table of Contents](#Kubernetes)

## What are the various K8's services running on nodes and describe the role of each service?
Mainly K8 cluster consists of two types of nodes, executor and master.
Executor node: (This runs on master node)
Kube-proxy: This service is responsible for the communication of pods within the cluster and to the outside network, which runs on every node. This service is responsible to maintain network protocols when your pod establishes a network communication.
kubelet: Each node has a running kubelet service that updates the running node accordingly with the configuration(YAML or JSON) file. NOTE: kubelet service is only for containers created by Kubernetes.
Master services:

Kube-apiserver: Master API service which acts as an entry point to K8 cluster.
Kube-scheduler: Schedule PODs according to available resources on executor nodes.
Kube-controller-manager:  is a control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired stable state

[Table of Contents](#Kubernetes)

## What is PDB (Pod Disruption Budget)?
A Kubernetes administrator can create a deployment of a kind: PodDisruptionBudget for high availability of the application, it makes sure that the minimum number is running pods are respected as mentioned by the attribute minAvailable spec file. This is useful while performing a drain where the drain will halt until the PDB is respected to ensure the High Availability(HA) of the application. The following spec file also shows minAvailable as 2 which implies the minimum number of an available pod (even after the election).
Example: YAML Config using minAvailable =>

apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
name: zk-pdb
spec:
minAvailable: 2
selector:
matchLabels:
app: zookeeper

[Table of Contents](#Kubernetes)

## What’s the init container and when it can be used?
init containers will set a stage for you before running the actual POD.
Wait for some time before starting the app Container with a command like sleep 60.
Clone a git repository into a volume.

[Table of Contents](#Kubernetes)

## What is the role of Load Balance in Kubernetes?
Load balancing is a way to distribute the incoming traffic into multiple backend servers, which is useful to ensure the application available to the users.
Load Balancer
In Kubernetes, as shown in the above figure all the incoming traffic lands to a single IP address on the load balancer which is a way to expose your service to outside the internet which routes the incoming traffic to a particular pod (via service) using an algorithm known as round-robin. Even if any pod goes down load balances are notified so that the traffic is not routed to that particular unavailable node. Thus load balancers in Kubernetes are responsible for distributing a set of tasks (incoming traffic) to the pods

[Table of Contents](#Kubernetes)

## What are the various things that can be done to increase Kubernetes security?
By default, POD can communicate with any other POD, we can set up network policies to limit this communication between the PODs.
RBAC (Role-based access control) to narrow down the permissions.
Use namespaces to establish security boundaries.
Set the admission control policies to avoid running the privileged containers.
Turn on audit logging.

[Table of Contents](#Kubernetes)

## How to monitor the Kubernetes cluster?
Prometheus is used for Kubernetes monitoring. The Prometheus ecosystem consists of multiple components.
Mainly Prometheus server which scrapes and stores time-series data.
Client libraries for instrumenting application code.
Push gateway for supporting short-lived jobs.
Special-purpose exporters for services like StatsD, HAProxy, Graphite, etc.
An alert manager to handle alerts on various support tools.

[Table of Contents](#Kubernetes)

## How to get the central logs from POD?
This architecture depends upon the application and many other factors. Following are the common logging patterns

Node level logging agent.
Streaming sidecar container.
Sidecar container with the logging agent.
Export logs directly from the application.
In the setup, journalbeat and filebeat are running as daemonset. Logs collected by these are dumped to the kafka topic which is eventually dumped to the ELK stack.
The same can be achieved using EFK stack and fluentd-bit.

[Table of Contents](#Kubernetes)

## How to turn the service defined below in the spec into an external one?

    spec:
    selector:
    app: some-app
    ports:
    - protocol: UDP
      port: 8080
      targetPort: 8080
      Explanation -

Adding type: LoadBalancer and nodePort as follows:

    spec:
    selector:
    app: some-app
    type: LoadBalancer
    ports:
    - protocol: UDP
    port: 8080
    targetPort: 8080
    nodePort: 32412


Complete the following configurationspec file to make it Ingress
    metadata:
    name: someapp-ingress
    spec:
    Explanation -

One of the several ways to answer this question.

    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
        name: someapp-ingress
    spec:
    rules:
        - host: my.host
    http:
    paths:
      - backend:
      serviceName: someapp-internal-service
      servicePort: 8080

[Table of Contents](#Kubernetes)

## How to configure TLS with Ingress?
Add tls and secretName entries.

spec:
tls:
- hosts:
    - some_app.com
      secretName: someapp-secret-tls

[Table of Contents](#Kubernetes)

## Why use namespaces? What is the problem with using the default namespace?
While using the default namespace alone, it becomes hard over time to get an overview of all the applications you can manage in your cluster. Namespaces make it easier to organize the applications into groups that make sense, like a namespace of all the monitoring applications and a namespace for all the security applications, etc.
Namespaces can also be useful for managing Blue/Green environments where each namespace can include a different version of an app and also share resources that are in other namespaces (namespaces like logging, monitoring, etc.).
Another use case for namespaces is one cluster with multiple teams. When multiple teams use the same cluster, they might end up stepping on each other's toes. For example, if they end up creating an app with the same name it means one of the teams overrides the app of the other team because there can't be two apps in Kubernetes with the same name (in the same namespace).

[Table of Contents](#Kubernetes)

## In the following file which service and in which namespace is referred?
    apiVersion: v1
    kind: ConfigMap
    metadata:
    name: some-configmap
    data:
    some_url: silicon.chip
    Answer - It's referencing the service "silicon" in the namespace called "chip".

[Table of Contents](#Kubernetes)

## What is an Operator?
"Operators are software extensions to K8s which make use of custom resources to manage applications and their components. Operators follow Kubernetes principles, notably the control loop."

[Table of Contents](#Kubernetes)

## Why do we need Operators?
The process of managing applications in Kubernetes isn't as straightforward as managing stateless applications, where reaching the desired status and upgrades are both handled the same way for every replica. In stateful applications, upgrading each replica might require different handling due to the stateful nature of the app, each replica might be in a different status. As a result, we often need a human operator to manage stateful applications. Kubernetes Operator is supposed to assist with this.
This will also help with automating a standard process on multiple Kubernetes clusters

[Table of Contents](#Kubernetes)

## What is GKE?
GKE is Google Kubernetes Engine that is used for managing and orchestrating systems for Docker containers. With the help of Google Public Cloud, we can also orchestrate the container cluster.

[Table of Contents](#Kubernetes)

## What is Ingress Default Backend?
It specifies what to do with an incoming request to the Kubernetes cluster that isn't mapped to any backend i.e what to do when no rules being defined for the incoming HTTP request If the default backend service is not defined, it's recommended to define it so that users still see some kind of message instead of an unclear error.

[Table of Contents](#Kubernetes)

## How to run Kubernetes locally?
Kubernetes can be set up locally using the Minikube tool. It runs a single-node bunch in a VM on the computer. Therefore, it offers the perfect way for users who have just ongoing learning Kubernetes.

[Table of Contents](#Kubernetes)

## What is Kubernetes Load Balancing?
Load Balancing is one of the most common and standard ways of exposing the services. There are two types of load balancing in K8s and they are:
Internal load balancer – This type of balancer automatically balances loads and allocates the pods with the required incoming load.
External Load Balancer – This type of balancer directs the traffic from the external loads to backend pods.

[Table of Contents](#Kubernetes)

## What the following in the Deployment configuration file mean?
    spec:
    containers:
    - name: USER_PASSWORD
      valueFrom:
      secretKeyRef:
      name: some-secret
      key: password
      Explanation -

USER_PASSWORD environment variable will store the value from the password key in the secret called "some-secret" In other words, you reference a value from a Kubernetes Secret.

[Table of Contents](#Kubernetes)

## What is the difference between Docker Swarm and Kubernetes?
Below are the main difference between Kubernetes and Docker:

The installation procedure of the K8s is very complicated but if it is once installed then the cluster is robust. On the other hand, the Docker swarm installation process is very simple but the cluster is not at all robust.
Kubernetes can process the auto-scaling but the Docker swarm cannot process the auto-scaling of the pods based on incoming load.
Kubernetes is a full-fledged Framework. Since it maintains the cluster states more consistently so autoscaling is not as fast as Docker Swarm.

[Table of Contents](#Kubernetes)

## How to troubleshoot if the POD is not getting scheduled?
In K8’s scheduler is responsible to spawn pods into nodes. There are many factors that can lead to unstartable POD. The most common one is running out of resources, use the commands like kubectl describe <POD> -n <Namespace> to see the reason why POD is not started. Also, keep an eye on kubectl to get events to see all events coming from the cluster.

[Table of Contents](#Kubernetes)

## How to run a POD on a particular node?
Various methods are available to achieve it.
nodeName: specify the name of a node in POD spec configuration, it will try to run the POD on a specific node.
nodeSelector: Assign a specific label to the node which has special resources and use the same label in POD spec so that POD will run only on that node.
nodeaffinities: required DuringSchedulingIgnoredDuringExecution, preferredDuringSchedulingIgnoredDuringExecution are hard and soft requirements for running the POD on specific nodes. This will be replacing nodeSelector in the future. It depends on the node labels.

[Table of Contents](#Kubernetes)

## What are the different ways to provide external network connectivity to K8?
By default, POD should be able to reach the external network but vice-versa we need to make some changes. Following options are available to connect with POD from the outer world.
Nodeport (it will expose one port on each node to communicate with it)
Load balancers (L4 layer of TCP/IP protocol)
Ingress (L7 layer of TCP/IP Protocol)
Another method is to use Kube-proxy which can expose a service with only cluster IP on the local system port.

$ kubectl proxy --port=8080 $ http://localhost:8080/api/v1/proxy/namespaces//services/:/

[Table of Contents](#Kubernetes)

## How can we forward the port 8080 container to 8080 service to 8080 ingress to 80 browser and how it can be done?
The ingress is exposing port 80 externally for the browser to access, and connecting to a service that listens on 8080. The ingress will listen on port 80 by default. An "ingress controller" is a pod that receives external traffic and handles the ingress and is configured by an ingress resource For this you need to configure the ingress selector and if no 'ingress controller selector' is mentioned then no ingress controller will manage the ingress.

Simple ingress Config will look like
host: abc.org
http:
paths:
backend:
serviceName: abc-service
servicePort: 8080
Then the service will look like
kind: Service
apiVersion: v1
metadata:
name: abc-service
spec:
ports:
protocol: TCP
port: 8080 # port to which the service listens to
targetPort: 8080

[Table of Contents](#Kubernetes)