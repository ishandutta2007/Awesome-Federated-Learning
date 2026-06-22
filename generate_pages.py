import os

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Federated-Learning"
os.makedirs(os.path.join(base_dir, 'pages'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'assets'), exist_ok=True)

svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8A2387;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#E94057;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#F27121;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" rx="15" />
  <text x="50%" y="45%" font-family="Arial, sans-serif" font-size="42" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">Awesome Federated Learning</text>
  <text x="50%" y="65%" font-family="Arial, sans-serif" font-size="20" fill="white" text-anchor="middle" dominant-baseline="middle">Evolution, Variants, Types, &amp; Applications</text>
</svg>'''

with open(os.path.join(base_dir, 'assets', 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_content)

concepts = {
    'FedAvg': ('The Foundation Era (FedAvg)', 'A detailed overview of Federated Averaging (FedAvg), the foundational algorithm for FL. Synchronous rounds of local Stochastic Gradient Descent (SGD) on client devices, followed by averaging of model updates on a central coordinator server.', 'graph TD;\n    A[Central Server] -->|Broadcast Global Model| B[Client 1];\n    A -->|Broadcast Global Model| C[Client 2];\n    B -->|Local Training| B;\n    C -->|Local Training| C;\n    B -->|Upload Local Weights| A;\n    C -->|Upload Local Weights| A;\n    A -->|Aggregate (FedAvg)| A;'),
    'System_Heterogeneity': ('The System Heterogeneity Era', 'Dealing with Non-IID data distributions and varying client hardware speeds, introducing tracking algorithms like FedProx and Scaffold.', 'graph TD;\n    A[Server] -->|Send Model| B[Fast Client];\n    A -->|Send Model| C[Slow Client];\n    B -->|Proximal Term Optimization| B;\n    C -->|Proximal Term Optimization| C;\n    B -->|Update| A;\n    C -->|Update| A;'),
    'Fully_Decentralized': ('The Fully Decentralized & Trustless Era', 'Eliminates the central coordinator server entirely. Clients communicate over a peer-to-peer mesh network, often utilizing blockchain ledgers.', 'graph TD;\n    A[Node 1] <--> B[Node 2];\n    A <--> C[Node 3];\n    B <--> C;\n    B <--> D[Node 4];\n    C <--> D;'),
    'Horizontal_FL': ('Horizontal Federated Learning', 'Datasets share the exact same feature space but differ significantly in their sample IDs.', 'graph LR;\n    A[Bank A: Features X, Users 1-100] <--> C[Federated Aggregator];\n    B[Bank B: Features X, Users 101-200] <--> C;'),
    'Vertical_FL': ('Vertical Federated Learning', 'Datasets share overlapping sample IDs but differ in their feature spaces.', 'graph LR;\n    A[Bank: Users 1-100, Financial Data] <--> C[Alignment & Encryption];\n    B[E-commerce: Users 1-100, Retail Data] <--> C;'),
    'Federated_Transfer_Learning': ('Federated Transfer Learning (FTL)', 'Applied when both the sample IDs and the feature spaces have very little overlap across clients.', 'graph LR;\n    A[Domain A Data] --> C[Common Representation Space];\n    B[Domain B Data] --> C;\n    C --> D[Federated Model];'),
    'Cross_Device_FL': ('Cross-Device Federated Learning', 'Scales to millions of highly unstable, resource-constrained mobile or IoT devices.', 'graph TD;\n    A[Server] --> B[Mobile 1];\n    A --> C[Mobile 2];\n    A --> D[IoT Device];\n    A -.-> E[Offline Device];'),
    'Cross_Silo_FL': ('Cross-Silo Federated Learning', 'Involves a small, fixed number of highly reliable institutional organizations.', 'graph TD;\n    A[Server] <--> B[Hospital 1];\n    A <--> C[Hospital 2];\n    A <--> D[Hospital 3];'),
    'Differential_Privacy': ('Differential Privacy (DP) FL', 'Adds mathematical noise directly to local gradients before sending them to the aggregator.', 'graph LR;\n    A[Client Data] --> B[Local Training];\n    B --> C[Add Laplacian Noise];\n    C --> D[Send to Server];'),
    'SMPC': ('Secure Multi-Party Computation (SMPC)', 'Uses cryptographic secret sharing protocols to keep individual updates unreadable.', 'graph LR;\n    A[Client 1] -->|Secret Share| C[Aggregator];\n    B[Client 2] -->|Secret Share| C;\n    C -->|Compute Sum w/o Seeing Parts| D[Global Model];'),
    'TEE_FL': ('Trusted Execution Environments (TEE-FL)', 'Directs the aggregation phase to execute inside secure, hardware-isolated memory enclaves.', 'graph TD;\n    A[Client 1] --> B[Cloud Provider Server];\n    C[Client 2] --> B;\n    subgraph B\n    D[Intel SGX Enclave]\n    end\n    B --> D;'),
    'Smart_Keyboard': ('Smart Keyboard Next-Word Prediction', 'Modern smartphones collaboratively train autocomplete and text correction models locally.', 'graph TD;\n    A[Global Language Model] --> B[Phone A];\n    A --> C[Phone B];\n    B -->|Learn from Typing| B;\n    C -->|Learn from Typing| C;\n    B -->|Send Gradient| A;'),
    'Medical_Image': ('De-Identified Medical Image Diagnostics', 'Hospitals worldwide train a unified deep neural network to detect rare tumors.', 'graph TD;\n    A[Global Diagnostic Model] <--> B[Hospital A X-Rays];\n    A <--> C[Hospital B MRIs];'),
    'Autonomous_Fleet': ('Autonomous Fleet Learning', 'Self-driving vehicle fleets process edge-case driving data locally.', 'graph TD;\n    A[Global Autopilot Model] <--> B[Car 1];\n    A <--> C[Car 2];\n    B -->|Night driving data| B;\n    C -->|Snow driving data| C;')
}

for key, (title, desc, mermaid) in concepts.items():
    content = f"# {title}\n\n## Overview\n{desc}\n\n## Architecture Diagram\n```mermaid\n{mermaid}\n```\n\n[Back to README](../README.md)"
    with open(os.path.join(base_dir, 'pages', f'{key}.md'), 'w', encoding='utf-8') as f:
        f.write(content)

readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

link_mapping = {
    '**The Foundation Era (FedAvg)**': '[**The Foundation Era (FedAvg)**](pages/FedAvg.md)',
    '**The System Heterogeneity Era**': '[**The System Heterogeneity Era**](pages/System_Heterogeneity.md)',
    '**The Fully Decentralized & Trustless Era**': '[**The Fully Decentralized & Trustless Era**](pages/Fully_Decentralized.md)',
    '**Horizontal Federated Learning (Sample-Based)**': '[**Horizontal Federated Learning (Sample-Based)**](pages/Horizontal_FL.md)',
    '**Vertical Federated Learning (Feature-Based)**': '[**Vertical Federated Learning (Feature-Based)**](pages/Vertical_FL.md)',
    '**Federated Transfer Learning (FTL)**': '[**Federated Transfer Learning (FTL)**](pages/Federated_Transfer_Learning.md)',
    '**Cross-Device Federated Learning**': '[**Cross-Device Federated Learning**](pages/Cross_Device_FL.md)',
    '**Cross-Silo Federated Learning**': '[**Cross-Silo Federated Learning**](pages/Cross_Silo_FL.md)',
    '**Differential Privacy (DP) Federated Learning**': '[**Differential Privacy (DP) Federated Learning**](pages/Differential_Privacy.md)',
    '**Secure Multi-Party Computation (SMPC)**': '[**Secure Multi-Party Computation (SMPC)**](pages/SMPC.md)',
    '**Trusted Execution Environments (TEE-FL)**': '[**Trusted Execution Environments (TEE-FL)**](pages/TEE_FL.md)',
    '**Smart Keyboard Next-Word Prediction**': '[**Smart Keyboard Next-Word Prediction**](pages/Smart_Keyboard.md)',
    '**De-Identified Medical Image Diagnostics**': '[**De-Identified Medical Image Diagnostics**](pages/Medical_Image.md)',
    '**Autonomous Fleet Learning**': '[**Autonomous Fleet Learning**](pages/Autonomous_Fleet.md)'
}

for k, v in link_mapping.items():
    readme = readme.replace(k, v)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)
