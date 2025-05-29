# Automated Phishing URL Detection & Alert System

## Overview

This project delivers a robust, multi-technology system designed to **automatically detect phishing URLs** and provide timely alerts and visual analytics. The system combines traditional URL parsing, advanced machine learning classification, user-friendly web interface, real-time notification handling, and strategic data visualization.

---

## Architecture

| Component            | Technology        | Responsibility                              |
|----------------------|-------------------|---------------------------------------------|
| **URL Parser**       | C++               | Efficient URL syntax parsing & preliminary filtering |
| **ML & NLP Service** | Python (Flask)    | Machine learning classification & natural language processing |
| **User Portal**      | HTML, CSS, JS     | Interactive web interface for URL submission and reports |
| **API Gateway**      | Go                | Central API routing, real-time notification integration |
| **Visualization**    | R                 | Data visualization of phishing trends and threat intelligence |

---

## Repository Structure

```plaintext
phishing_detection_system/
├── cpp_url_parser/
│   ├── include/
│   │   └── url_parser.h
│   ├── src/
│   │   └── url_parser.cpp
│   ├── tests/
│   │   └── test_url_parser.cpp
│   └── CMakeLists.txt
│
├── python_ml_nlp/
│   ├── models/
│   │   └── phishing_classifier.pkl
│   ├── src/
│   │   ├── classifier.py
│   │   ├── nlp_processing.py
│   │   └── train_model.py
│   ├── app/
│   │   ├── app.py  # Flask API for prediction
│   │   └── requirements.txt
│   ├── data/
│   │   ├── phishing_urls.csv
│   │   └── legitimate_urls.csv
│   └── tests/
│       └── test_classifier.py
│
├── web_portal/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   ├── templates/
│   │   └── index.html
│   
│
├── go_api_gateway/
│   ├── cmd/
│   │   └── main.go
│   ├── internal/
│   │   ├── handlers.go
│   │   ├── notifications.go
│   │   └── router.go
│   ├── go.mod
│   └── go.sum
│
├── r_visualization/
│   ├── scripts/
│   │   └── phishing_trends.R
│   ├── data/
│   │   └── phishing_stats.csv
│   
│
└── README.md

```
--------------------------------
--------------------------------
## Setup & Installation

### 1. C++ URL Parser

- Requires a C++17 compliant compiler and CMake.
- Build instructions:

```bash
cd cpp_url_parser
mkdir build && cd build
cmake ..
make
 
 --------

 -Usage: Integrate liburlparser.a or link directly with your application.

 2. Python ML & Flask API
Requires Python 3.8+.

Install dependencies:

'''
cd python_ml_nlp/app
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
 
 ```
-Run the Flask API:
 ```
python app.py
 ```
-The API will listen on http://localhost:5000/predict.

3. Web Portal
The portal is static and interacts with the Flask or Go API.

Open web_portal/templates/index.html in any modern browser.

Ensure the backend API is running for full functionality.

4. Go API Gateway
Requires Go 1.18+ installed.

Build and run:
```
cd go_api_gateway/cmd
go mod tidy
go run main.go
```
Listens by default on port 8080.

Routes ```/api/predict``` requests to Python Flask API.

5. R Visualization
Requires R with ```ggplot2, readr, and dplyr``` packages installed.

Run visualization script:
```
source("r_visualization/scripts/phishing_trends.R")

```
- Generates phishing trend charts saved in ```r_visualization/output/```.

**Usage**
Use the Web Portal or any HTTP client to submit URLs for phishing detection.

Requests are routed via the Go API Gateway to the Python ML API, which returns prediction results.

The C++ module can be integrated for preprocessing or standalone analysis.

Use the R visualization tools to analyze aggregated detection data for trends and reporting.

**Contribution**

Contributions are welcome. Please follow standard coding conventions and submit pull requests for any improvements or new features. Ensure all modules pass their respective unit tests.

**Future Enhancements**

Real-time alert system integration with WebSocket or push notification services.

Automated model retraining pipeline using fresh URL datasets.

Deployment automation using Docker and Kubernetes.

Expanded NLP feature extraction for enhanced detection accuracy.

Comprehensive dashboard combining visualization with live detection metrics.





