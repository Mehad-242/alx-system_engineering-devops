Postmortem Report: Web-01 Outage on August 20, 2024
Issue Summary:  

 Duration:  August 20, 2024, 09:00 AM - 11:30 AM UTC
- Impact: The web application hosted on `web-01` experienced a complete outage,rendering it inaccessible to all users. Approximately 75% of our user base was affected, as `web-02` was handling minimal traffic due to load balancing misconfiguration
- Root Cause: The outage was caused by an unexpected server crash on `web-01`due to an exhausted disk space issue, exacerbated by a lack of monitoring on disk usage

: Timeline
09:00 AM UTC: Issue detected by monitoring alert indicating that `web-01` was unreachable
09:05 AM UTC: Incident escalated to the on-call engineer, who began investigating the cause.
09:10 AM UTC: Initial assumption was that the issue was network-related; network diagnostics were run but showed no abnormalities.
09:30 AM UTC: Logs from `web-01` were reviewed, revealing repeated disk I/O errors.
09:45 AM UTC: Disk space usage on `web-01` was checked and found to be at 100% capacity.
10:00 AM UTC: Incident escalated to the DevOps team for further investigation and resolution.
10:15 AM UTC: Temporary resolution applied by freeing up disk space on `web-01` by deleting unnecessary logs and files.
10:30 AM UTC: `web-01` restarted, services began to recover, but users experienced intermittent issues due to high traffic load on `web-02`.
11:00 AM UTC: Traffic rerouted correctly between `web-01` and `web-02` to balance the load.
11:30 AM UTC: Full service restored, and all systems operational.



Root Cause and Resolution:

- Root Cause: The primary cause of the outage was the exhaustion of disk space on `web-01`. The server had accumulated large log files over time, which were not rotated or archived, leading to the disk reaching full capacity. This triggered server crashes and made the application inaccessible. 

- Resolution: The issue was resolved by manually deleting old log files to free up space. After freeing up space, the server was rebooted, and services were restored. The load balancer configuration was also corrected to ensure that `web-02` could properly handle traffic in case of future failures.

Corrective and Preventative Measures 

Improvements:
- Implement regular log rotation and archiving to prevent disk space exhaustion
- Enhance monitoring to include disk space usage alerts for all servers
- Review and update load balancing configurations to ensure failover works as expected

TODO List:
- Patch `web-01` to automate log rotation and configure log archiving 
- Set up monitoring alerts for disk space thresholds on both `web-01` and `web-02'
- Test and validate the load balancer configuration under different failure scenarios
- Conduct a review of disk usage policies and ensure all servers comply with them
- Train the on-call engineering team on troubleshooting steps for disk space-related issues



This postmortem report highlights the importance of proactive monitoring and regular maintenance to prevent outages. By implementing the corrective measures outlined, we aim to reduce the risk of similar incidents in the future.

