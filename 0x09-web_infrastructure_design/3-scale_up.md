To scale up our web infrastructure, we'll add one server, configure a load balancer (HAproxy) as a cluster with the existing one, and split components (web server, application server, database) onto separate servers for improved performance, scalability, and reliability. Here's why each additional element is added:

### Load Balancer Cluster (HAproxy):

Configuring HAproxy as a cluster with the existing load balancer enhances load balancing capabilities, distributes traffic more effectively, and provides redundancy and failover support, ensuring high availability and reliability.

### Split Components onto Separate Servers:

Separating components (web server, application server, database) onto dedicated servers improves resource utilization, isolation, and scalability.
