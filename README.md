# my_python_test_framework
This repository contains a test automation framework for running UI tests using Playwright and API tests using pytest. The framework is designed to be modular, scalable, and easy to use.


**Project Structure**: 

Project contains UI and API tests

/test_automation_framework 

├── /tests  
├── /reports # Test reports and logs  
├── requirements.txt  
└── pytest.ini # Pytest configuration


**Setup Instructions**:
1. **Clone the repository**
 git clone https://github.com/Kate-Surta/my_python_test_framework.git

2. **Install dependencies**
pip install -r requirements.txt


**Running Tests**: 

run tests locally:
pytest  
provide results into html page:
pytest --html=reports/report.html

 **Configuration**: 
Pytest configuration is managed via pytest.ini.   
**Contributing**: 
We are open to reviews and comments to enhance the framework!
