# Test Automation Framework
This repository contains a test automation framework for running UI tests using Playwright and API tests using pytest. The framework is designed to be modular, scalable, and easy to use.


**Project Structure**:   
Project contains UI and API tests

/test_automation_framework  
├── /tests  
├── /reports # Test reports and logs  
├── /utils # Test logger implementation  
├── requirements.txt  
└── pytest.ini # Pytest configuration


**Setup Instructions**:  
Follow these steps to set up the framework on your local machine:
1. **Clone the repository**  
 git clone https://github.com/Kate-Surta/my_python_test_framework.git 
2. **Navigate into the project directory**:   
cd my_python_test_framework 
3. **Install dependencies**   
pip install -r requirements.txt 


**Running Tests**: 

To execute the tests, use the following commands:  
Run tests locally:  
pytest  
Generate an HTML report of the test results:  
pytest --html=reports/report.html  

 **Configuration**:  
The configuration for pytest can be managed via the pytest.ini file. Here you can set various pytest options according to your needs.  

**Contributing**:  
We are open to reviews and comments to enhance the framework!
