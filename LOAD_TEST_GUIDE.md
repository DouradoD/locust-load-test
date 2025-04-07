
### 📌 Before Starting the Load Test

```markdown
1. Define Clear Objectives

- What’s the goal? (E.g., validate 1,000 concurrent users, identify breaking points, meet SLA of ≤2s response time).

- Example: "We need to ensure the checkout API handles 500 orders/minute during peak sales."(Check the avg, P90 and P95)

2. Understand the System Architecture

- Map dependencies (APIs, databases, CDNs, third-party services).

- Critical: Know scalability mechanisms (auto-scaling, load balancers).

3. Set Up a Production-Like Environment

 - Mirror hardware, network, data volume (anonymized production data if possible).

 - Pitfall: Testing on underpowered VMs skews results.

4. Prepare Test Data

 - Realistic user scenarios (e.g., mix of guest/logged-in users, varied payloads).

 - Tool Tip: Use CSV files in JMeter for dynamic data (usernames, product IDs).

5. Configure Key Metrics & Thresholds

 - Define pass/fail criteria (e.g., error rate <1%, P95 response time <3s).

 - Example SLA: "95% of login requests must complete in ≤1.5s."

6. Baseline Testing

 - Run a low-load test (e.g., 10 users) to verify scripts and sanity-check the system.

7. Notify Stakeholders

 - Warn DevOps/infra teams to monitor resources during tests.
```
### 🔍 During Execution: What to Analyze

```markdown
1. Real-Time Metrics Dashboard

Must-Monitor:

Response Times (Avg, P90, P95).

Throughput (Requests/sec dropping? Bottleneck likely).

- Error Rates (Spikes → check logs for 5xx errors, timeouts).

- Tool Example: Grafana dashboard with Prometheus metrics.

2. System Resources

CPU/RAM: Sustained >80% usage → inefficiency or need to scale.

Database: High query latency or deadlocks → optimize indexes/queries.

Network: Latency between microservices?

3. Thread/Connection Pools

Exhausted DB connections (e.g., PostgreSQL max_connections hit)?

 - Symptom: Errors like Timeout awaiting connection from pool.

4. Garbage Collection (GC) Logs

 - Frequent Full GC cycles → memory leaks (common in soak tests).

5. External Dependencies

 - Third-party APIs slowing down? Implement circuit breakers/retries.

6. Correlate Metrics

 - Example: High response times + low CPU → likely DB/network issue.

 - Example: Throughput drops while errors rise → system throttling.

7. Logs & APM Traces

 - Trace slow requests end-to-end (e.g., New Relic, Dynatrace).

 - Critical: Look for patterns (e.g., /search?q=* is slow → missing index).
```
### 🚨 Red Flags During Execution
````markdown
 - Errors Spike (>5%): Pause and investigate (don’t waste time on invalid tests).

 - Throughput Plateaus: System can’t handle more load (vertical/horizontal scaling needed).

 - Memory Leaks: RAM usage grows indefinitely (soak test failure).
````
