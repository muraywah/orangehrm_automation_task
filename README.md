# OrangeHRM Automation Testing

Automated testing project for the OrangeHRM demo application using Playwright, Python, and Pytest.

The project uses the Page Object Model (POM) to separate page locators and actions from the test cases.

## Application Under Test

OrangeHRM Open Source Demo

URL: https://opensource-demo.orangehrmlive.com/

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest HTML
- Page Object Model (POM)
- Git & GitHub

## Project Structure

```text
Orangehrm_automation/
│
├── pages/
│   ├── login_page.py
│   ├── my_info_page.py
│   └── admin_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_my_info.py
│   └── test_admin.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md