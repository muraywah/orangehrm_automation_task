from pages.admin_page import AdminPage
from pages.login_page import LoginPage


def test_delete_first_record(page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page.login("Admin", "admin123")

    admin_page.admin_menu.click()

    page.wait_for_selector(".oxd-table-row", timeout=10000)

    rows = page.locator(".oxd-table-row")
    
    for i in range(1, rows.count()):
        row = rows.nth(i)
        username = row.locator(".oxd-table-cell").nth(1).inner_text()
    
        print(f"Row {i} username: {username}")
    
        if username != "Admin":
            print("Selected row:", username)
    
            delete_button = row.locator("i.bi-trash").locator("..")
            delete_button.click()
    
            print("Delete button clicked")
            break
    
    admin_page.confirm_delete_button.click()