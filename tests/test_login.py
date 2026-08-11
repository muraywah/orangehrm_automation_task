from pages.login_page import LoginPage


def test_login(page):
    login_page = LoginPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.login("Admin", "admin123")
    
