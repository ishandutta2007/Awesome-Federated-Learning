# The System Heterogeneity Era

## Overview
Dealing with Non-IID data distributions and varying client hardware speeds, introducing tracking algorithms like FedProx and Scaffold.

## Architecture Diagram
```mermaid
graph TD;
    A[Server] -->|Send Model| B[Fast Client];
    A -->|Send Model| C[Slow Client];
    B -->|Proximal Term Optimization| B;
    C -->|Proximal Term Optimization| C;
    B -->|Update| A;
    C -->|Update| A;
```

[Back to README](../README.md)