# Federated Transfer Learning (FTL)

## Overview
Applied when both the sample IDs and the feature spaces have very little overlap across clients.

## Architecture Diagram
```mermaid
graph LR;
    A[Domain A Data] --> C[Common Representation Space];
    B[Domain B Data] --> C;
    C --> D[Federated Model];
```

[Back to README](../README.md)