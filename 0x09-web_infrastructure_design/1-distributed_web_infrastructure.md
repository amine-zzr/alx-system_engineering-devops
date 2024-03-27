## Here's why each element is added:

### Replication of Servers:
Replicating the web server, application server, and database provides redundancy and failover capability. If one server fails, the replicated server can take over to ensure continuous service availability.

### Load Balancer (HAproxy):
Added to distribute incoming traffic across Server 1 and Server 2, balancing the load between them. It enhances performance and scalability by utilizing multiple servers efficiently.

### Load Balancer Configuration:
The HAproxy load balancer is configured with a round-robin distribution algorithm. This algorithm evenly distributes incoming requests among the available servers (Server 1 and Server 2) in a circular manner, ensuring balanced workload distribution.

### Active-Active Setup:
In this setup, both Server 1 and Server 2 are actively serving requests simultaneously. This configuration maximizes resource utilization and provides high availability by distributing the workload across multiple servers.

For Active-Passive setup, one server is actively serving requests, while the other remains in standby mode. In case of failure, the passive server takes over. This setup ensures high availability but may lead to underutilization of resources.

### Primary-Replica (Master-Slave) Database Cluster:

The Primary node handles write operations and serves as the main database for the application.
The Replica node replicates data from the Primary node and handles read operations, reducing the load on the Primary node and providing data redundancy.

## Issues with This Infrastructure:

### Single Point of Failure (SPOF):
The load balancer, if not configured redundantly, can become a single point of failure.

### Security Issues:
Lack of firewall configurations and HTTPS encryption can expose the infrastructure to security risks.

### No Monitoring:
Without monitoring tools, it's challenging to detect and address performance or availability issues proactively.
