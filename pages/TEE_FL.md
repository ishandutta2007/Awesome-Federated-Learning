# Trusted Execution Environments (TEE-FL)

## Overview
Directs the aggregation phase to execute inside secure, hardware-isolated memory enclaves.

## Architecture Diagram
```mermaid
graph TD;
    A[Client 1] --> B[Cloud Provider Server];
    C[Client 2] --> B;
    subgraph B
    D[Intel SGX Enclave]
    end
    B --> D;
```

[Back to README](../README.md)