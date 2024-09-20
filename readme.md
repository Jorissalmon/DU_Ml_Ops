# ML-Ops Project - Prediction Model with Flask, Docker, and AWS

## Project Overview

This project is designed to showcase a Machine Learning pipeline using **Flask** for the web interface, **Docker** for containerization, and **AWS ECR** for hosting and deploying the Docker image. The model deployed is a **Random Forest** classifier, used to predict whether a client is at risk of defaulting on a loan based on various financial features. Additionally, we use **Arize** to monitor the model's performance in a production environment.
 
## Features

- **Flask Web Application**: A simple web interface where users can input client information and receive predictions on loan default risk.
- **Machine Learning Model**: A pre-trained Random Forest model to predict loan default risk.
- **Docker**: Containerization of the entire application for easy deployment.
- **AWS ECR**: Hosting the Docker images in Amazon's Elastic Container Registry.
- **Arize Integration**: For logging predictions and monitoring the model's performance over time.
- **GitHub CI/CD Pipeline**: Automatically deploys updated models to AWS ECR when changes are pushed.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Docker Setup](#docker-setup)
  - [AWS ECR](#aws-ecr)
- [Arize Integration](#arize-integration)
- [GitHub CI/CD Pipeline](#github-cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8+**
- **Docker**
- **AWS CLI** (version 2.x)
- **Git**
- **Flask**

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Jorissalmon/DU_Ml_Ops.git
   cd DU_Ml_Ops
2. **Set up a virtual environment**:
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install required Python libraries**:
pip install -r requirements.txt
4. **Set environment variables**:
Create a .env file in the project root and add your API keys:
SPACE_KEY=<your_arize_space_key>
API_KEY=<your_arize_api_key>

### Usage
Once everything is set up, you can run the application locally using:
flask run

Navigate to http://127.0.0.1:5000 in your browser. You'll be able to enter client financial information and get a prediction on loan default risk.

### Deployment
#### Docker Setup
To containerize and run your application with Docker:
1. Build the Docker image:
docker build -t ml-project:latest .
2. Run the Docker container:
docker run -p 5000:5000 ml-project:latest
Your Flask app will now be running on http://localhost:5000.

## AWS ECR
To push your Docker image to Amazon ECR for deployment:
1. Log in to AWS ECR:
aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin <your_aws_account_id>.dkr.ecr.eu-north-1.amazonaws.com
2. Tag the Docker image:
docker tag ml-project:latest <your_aws_account_id>.dkr.ecr.eu-north-1.amazonaws.com/ml-project:latest
3. Push the image to ECR:
docker push <your_aws_account_id>.dkr.ecr.eu-north-1.amazonaws.com/ml-project:latest

## Arize Integration
Arize is integrated to log predictions and actual labels, allowing for model performance monitoring over time. You need to set up your API keys in the .env file for Arize to function correctly.

To log predictions, the following block of code sends your model's predictions and actual labels to Arize for monitoring:
response = arize_client.log(
    dataframe=dataframe,
    model_id="Random_Forest_Model",
    model_version="v1",
    model_type=ModelTypes.SCORE_CATEGORICAL,
    environment=Environments.PRODUCTION,
    schema=schema
)
Make sure to update the model_id, model_version, and other parameters as needed for your specific model setup.

GitHub CI/CD Pipeline
This project leverages GitHub for Continuous Integration (CI) and Continuous Deployment (CD). A CI/CD pipeline is set up such that whenever changes are pushed to the repository, the following happens:

Continuous Integration: GitHub Actions automatically runs tests and ensures that the updated code is valid. This ensures that no broken code is deployed.

Continuous Deployment: When changes are made to the Machine Learning model or any part of the project, the updated Docker image is rebuilt and automatically pushed to AWS ECR. From there, the updated container is redeployed, ensuring that the latest model version is always live.

This pipeline allows for seamless integration and deployment of any updates to the model, providing a streamlined way to continuously improve and update the application.

To view or modify the GitHub Actions workflow, navigate to the .github/workflows/ directory.

Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push the changes to your forked repository (git push origin feature-branch).
Open a pull request to the main repository.


