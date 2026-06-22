# The Foundation Era (FedAvg)

## Overview
A detailed overview of Federated Averaging (FedAvg), the foundational algorithm for FL. Synchronous rounds of local Stochastic Gradient Descent (SGD) on client devices, followed by averaging of model updates on a central coordinator server.

## Architecture Diagram
```mermaid
graph TD;
    A["Central Server"] -->|Broadcast Global Model| B["Client 1"];
    A -->|Broadcast Global Model| C["Client 2"];
    B -->|Local Training| B;
    C -->|Local Training| C;
    B -->|Upload Local Weights| A;
    C -->|Upload Local Weights| A;
    A -->|Aggregate (FedAvg)| A;
```

[Back to README](../README.md)