# MonitorPro

MonitorPro is a real-time system monitoring dashboard that displays vital system metrics such as CPU utilization, memory usage, and battery status in a visually appealing way. It uses Flask for the backend, HTML and JavaScript for the frontend, and integrates with Flask-SocketIO for real-time data updates.

## Project Structure

```
MonitorPro/
├── template/
│   ├── cpu.html
│   ├── battery.html
│   ├── memory.html
│   ├── index.html
├── .gitignore
├── app.py
├── ecr.py
├── eks.py
├── Dockerfile
├── requirements.txt
└── README.md

```

## Features

- **Real-Time Monitoring**: Uses Flask-SocketIO to deliver system data such as CPU, memory, and battery stats in real-time.
- **System Information**: Leverages the `psutil` library to fetch up-to-date system statistics.
- **Interactive Charts**: Displays data via a radar chart using Chart.js.
- **Dark/Light Mode**: The interface supports dark and light themes, making it user-friendly across environments.

## Technologies Used

- **Flask**: A lightweight web framework for the backend.
- **Flask-SocketIO**: For enabling real-time WebSocket connections.
- **psutil**: To gather system statistics such as CPU, memory, and battery data.
- **Chart.js**: For creating dynamic radar charts to visualize system metrics.
- **HTML, CSS, JS**: For the frontend interface, including responsiveness for various devices.
- **Amazon ECR**: For container image storage.
- **Amazon EKS**: For managing containerized applications using Kubernetes.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhi-lash19/MonitorPro.git
   cd MonitorPro
   ```

2. **Create a Virtual Environment** (if using `venv`):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   Navigate to `http://localhost:5000` in your browser to view the system dashboard.

## Libraries in Use

- **Flask-SocketIO**: Handles WebSocket communication.
- **psutil**: Fetches system metrics.
- **Chart.js**: For rendering charts in the browser.
- **Flask**: Backend framework for building the API and server.

## Issues Faced

During the development of MonitorPro, several challenges were encountered:

- **EKS Node Creation Delays**: The EKS nodes were taking longer than expected (over 10 minutes) to create. Troubleshooting involved checking AWS console logs and events to identify potential bottlenecks or misconfigurations.
- **Networking Configuration**: Setting up VPC, security groups, and IAM roles for EKS and ECR required careful attention to ensure that the application could communicate effectively across services.
- **Image Deployment**: Pushing Docker images to Amazon ECR and ensuring they were correctly configured for deployment in EKS involved several iterations to resolve authentication and permission issues.
- While creating this project, I encountered an issue with connecting to the Kubernetes API server. The error message I received was:
  
```dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it```

This error occurs when kubectl is trying to connect to a local Kubernetes API server that isn’t running or isn’t reachable. It typically indicates that the Kubernetes configuration is not set up correctly on the machine, or the connection to the correct Kubernetes cluster (in this case, the EKS cluster) is not established.

## Amazon ECR and EKS Setup

1. **ECR Setup**: Integrated with the project to store Docker images. The ecr.py script manages the connection and interactions with Amazon Elastic Container Registry (ECR) for pushing and pulling images as needed for deployment.
   
   - Created a repository in Amazon Elastic Container Registry (ECR) to store the Docker images for the application.
   - Used the `aws ecr get-login-password` command to authenticate Docker with the ECR registry.
   - Built the Docker image locally and pushed it to the ECR repository.



3. **EKS Setup**: The project is deployed on Amazon Elastic Kubernetes Service (EKS). The eks.py script handles interactions with EKS, including cluster management and pod deployment.
   
   - Provisioned an EKS cluster using the AWS Management Console.
   - Configured a node group with appropriate instance types and autoscaling policies.
   - Deployed the application by creating Kubernetes deployment and service manifests, ensuring proper networking and security configurations.

