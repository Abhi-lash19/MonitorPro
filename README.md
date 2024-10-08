# MonitorPro

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
├── requirements.txt
└── README.md
```

## Features

- **Real-Time Monitoring**: Uses Flask-SocketIO to deliver system data such as CPU, memory, and battery stats in real-time.
- **System Information**: Leverages the `psutil` library to fetch up-to-date system statistics.
- **Interactive Charts**: Displays data via a radar chart using Chart.js.
- **Dark/Light Mode**: The interface supports dark and light themes, making it user-friendly across environments.

## Technologies Used

- **Flask**: A lightweight web framework for backend.
- **Flask-SocketIO**: For enabling real-time WebSocket connections.
- **psutil**: To gather system statistics such as CPU, memory, and battery data.
- **Chart.js**: For creating dynamic radar charts to visualize system metrics.
- **HTML, CSS, JS**: For the frontend interface, including responsiveness for various devices.

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

## Libraries in use

- **Flask-SocketIO**: Handles WebSocket communication.
- **psutil**: Fetches system metrics.
- **Chart.js**: For rendering charts in the browser.
- **Flask**: Backend framework for building the API and server.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
