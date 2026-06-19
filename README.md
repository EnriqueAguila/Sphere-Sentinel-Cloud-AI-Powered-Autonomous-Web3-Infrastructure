# Sphere-Sentinel-Cloud-AI-Powered-Autonomous-Web3-Infrastructure
Sphere Sentinel es un proyecto de infraestructura B2B (negocio a negocio) 
# 🛡️ Sphere Sentinel: AI-Powered Autonomous Web3 Infrastructure

[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Web3](https://img.shields.io/badge/Web3-Infrastructure-blueviolet?style=for-the-badge)](https://spherecloudsolutions.com)
[![AI-Agent](https://img.shields.io/badge/AI--Agent-Amazon--Bedrock-orange?style=for-the-badge)](https://aws.amazon.com/bedrock/)

**Sphere Sentinel** is an autonomous orchestration and security layer for Web3 Validator Nodes and Decentralized Physical Infrastructure Networks (**DePIN**). Developed by **SphereCloud Solutions** for the AWS Activate Hackathon.

---

## 🚀 Overview

The management of blockchain validator nodes is currently reactive and manually intensive. **Sphere Sentinel** transforms this by using **Amazon Bedrock (Claude 3)** to create an AI-driven "Digital Nervous System" that predicts failures, automates scaling on **AWS EKS**, and secures private keys using **AWS Nitro Enclaves**.

### Key Features
*   **🧠 AI-Driven Predictive Sentinel:** Analyzes real-time node logs to predict downtime or DDoS attacks before they happen.
*   **🛡️ Institutional Security:** Implementation of **AWS Nitro Enclaves** for isolated validator signing.
*   **📈 Elastic Orchestration:** Automated node scaling using **Terraform** and **Amazon EKS**.
*   **💰 Cost Efficiency:** Optimized for **AWS Graviton4** instances, reducing TCO for node operators.

---

## 🏗️ Architecture

Sphere Sentinel leverages a **Well-Architected** AWS native stack:

1.  **Ingestion:** Node telemetry is collected via CloudWatch and stored in **Amazon Timestream**.
2.  **Intelligence:** **Amazon Bedrock (Claude 3 Haiku)** processes logs to identify anomalies.
3.  **Action:** AWS Lambda triggers auto-scaling groups or instance migrations in **Amazon EKS**.
4.  **Security:** Private keys are managed within **AWS Nitro Enclaves** and encrypted with **AWS KMS**.

---

## 🛠️ Quick Start (MVP Prototype)

### Prerequisites
*   AWS Account with **Amazon Bedrock** access enabled (Anthropic Claude 3).
*   Python 3.9+
*   Terraform 1.5+

### 1. Infrastructure Deployment
```bash
cd terraform/
terraform init
terraform apply -auto-approve
