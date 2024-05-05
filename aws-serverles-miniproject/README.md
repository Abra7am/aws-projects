# Student Data Management Portal

## Overview
This project is a web-based student data management system that utilizes AWS services including Lambda, API Gateway, S3, CloudFront, and Route 53. It allows users to add and view student data through a user-friendly web interface. The backend is serverless, utilizing AWS Lambda and API Gateway, with static website hosting on S3 and efficient content delivery via CloudFront.

## Installation

### Prerequisites
- AWS Account

### AWS Configuration

- **Lambda Functions:**
  1. Navigate to AWS Lambda and create new functions for `getStudents` and `insertStudentData`.
  2. Upload the Python scripts and set the handler information.
  3. Assign appropriate permissions (IAM roles) for accessing other AWS services as needed.

- **API Gateway:**
  1. Create a new API in AWS API Gateway.
  2. Set up resources and methods for each Lambda function.
  3. Deploy the API to receive an HTTPS endpoint that the frontend will interact with.

- **S3 Bucket:**
  1. Create an S3 bucket for hosting the static website (`index.html` and `scripts.js`).
  2. Enable static website hosting on the S3 bucket.

- **CloudFront:**
  1. Create a new CloudFront distribution.
  2. Set the S3 bucket as the origin.
  3. Configure the distribution settings according to your requirements (e.g., SSL/TLS certificate, CNAMEs).

- **Route 53:**
  1. Set up a new hosted zone for your domain (e.g., `xxxxxx.com`).
  2. Create record sets to point your domain to the CloudFront distribution, enabling users to access the site using your domain name.

### Frontend Setup
- Ensure that `scripts.js` is updated to communicate with the deployed API Gateway endpoints.

## Usage
- The web interface allows you to add and retrieve student data through a user-friendly GUI.

## AWS Resources Used
- **AWS Lambda:** Hosts the serverless backend functions (`getStudents` and `insertStudentData`).
- **AWS API Gateway:** Manages the APIs that trigger the Lambda functions.
- **AWS S3:** Hosts the static files of the project, serving as the website host.
- **AWS CloudFront:** Distributes the website content globally, ensuring faster load times and enhanced security.
- **AWS Route 53:** Manages the DNS settings for the domain, connecting the custom domain to the CloudFront distribution.

## Deployment
- The frontend is hosted on AWS S3 and delivered via AWS CloudFront.
- Backend functionality is managed through AWS Lambda and API Gateway.
- The custom domain is configured through AWS Route 53.

## Contributing
Contributions are welcome. Please fork the project and submit pull requests.

