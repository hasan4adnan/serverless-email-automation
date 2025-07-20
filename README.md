# 📁 Serverless File Upload Notification System

A serverless AWS project built with **Terraform** that detects file uploads to an **S3 bucket**, triggers a **Lambda function**, and sends **email notifications** via **Amazon SES**. Optional **SNS** support included.

<img width="1119" height="678" alt="Ekran Resmi 2025-07-20 17 31 24" src="https://github.com/user-attachments/assets/5d261950-d838-4083-964c-9fd0d8516d0e" />



---

## 🚀 Features

- 📥 Upload detection via **S3 Event Notifications**
- 🧠 Processing with **AWS Lambda**
- 📧 Email alerts via **Amazon SES**
- 🛡️ IAM with Least Privilege
- 🔁 Fully automated deployment with **Terraform**
- 🧪 Logs via **CloudWatch**
- 📦 Modular file structure

---

## 📦 Project Structure

```
serverless-email-automation/
├── main.tf                 # AWS provider config
├── s3.tf                   # S3 bucket + event notification
├── lambda.tf               # Lambda function, execution role, permissions
├── iam.tf                  # IAM policies for SES/S3
├── variables.tf            # Variables (e.g., bucket name)
├── outputs.tf              # Output values (optional)
├── lambda/
│   └── lambda_handler.py   # Python code for Lambda
├── lambda.zip              # Deployment package (zipped Lambda)
└── README.md               # This file
```

---

## 🧠 How It Works

```
User uploads file to S3
     ↓
S3 triggers event → Lambda executes
     ↓
Lambda extracts file info from event
     ↓
Lambda sends email via SES (optional: SNS/SMS)
```

## 🛠️ Deployment Instructions

Make sure you have Terraform CLI and AWS CLI configured.

### 1️⃣ Clone this repository

```bash
git clone https://github.com/your-username/serverless-email-automation.git
cd serverless-email-automation
```

### 2️⃣ Build the Lambda package

```bash
cd lambda
zip ../lambda.zip lambda_handler.py
cd ..
```

### 3️⃣ Deploy with Terraform

```bash
terraform init
terraform apply
```

## ✉️ How to Configure Email Notification (Amazon SES)

1. Go to AWS SES Console
2. Navigate to Verified Identities
3. Click Create Identity
4. Choose Email Address, enter your address (e.g., you@example.com)
5. Confirm verification email from AWS
6. In lambda_handler.py, update:

```python
TO_ADDRESS = "you@example.com"  # Verified address
```

7. Re-zip and re-apply:

```bash
zip lambda.zip lambda/lambda_handler.py -f
terraform apply
```

📌 **Note**: SES in sandbox mode can only send to verified addresses. To remove this limit, request Production Access from AWS Support.

## 📄 Sample Lambda Log Output

```json
{
  "Records": [
    {
      "eventName": "ObjectCreated:Put",
      "s3": {
        "bucket": { "name": "upload-bucket-serverless-notify" },
        "object": { "key": "contract-2025.pdf" }
      }
    }
  ]
}
```

## 🌟 Potential Enhancements

- 📌 Use SES Templates
- 🔄 Log all uploads in DynamoDB
- 🔗 Generate pre-signed S3 upload URLs
- 📲 Add SMS or mobile push via SNS
- 🌍 Support multi-language notifications

## ✅ Tech Stack

| Component | Purpose |
|-----------|---------|
| S3 | File storage and event source |
| Lambda | Event processing logic |
| SES | Email notifications |
| SNS | (Optional) SMS or other endpoints |
| IAM | Access control and security |
| CloudWatch | Logs and monitoring |
| Terraform | Infrastructure as code |

## 📬 Author

**Built by Hasan Adnan** 🚀

- 📧 Email: [hassanmoaid44@gmail.com]
- 💼 LinkedIn: [Let's connect on LinkedIn!](https://www.linkedin.com/in/hasan-adnan-6091292bb)
- 🐙 GitHub: [hasan4adnan](https://github.com/hasan4adnan)


**License**: MIT
