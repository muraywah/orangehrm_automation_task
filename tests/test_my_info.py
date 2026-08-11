from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage


def test_update_my_info(page):
    login_page = LoginPage(page)
    my_info_page = MyInfoPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.login("Admin", "admin123")

    page.get_by_text("My Info").click()

    my_info_page.first_name.fill("Oluwamurewa")
    my_info_page.middle_name.fill("Titobiloluwa")
    my_info_page.last_name.fill("Adakomola")

    my_info_page.employee_id.fill("OLUWAMAD")
    my_info_page.other_id.fill("20082345")
    my_info_page.drivers_license.fill("54321")

    my_info_page.marital_status_dropdown.click()
    my_info_page.married_option.click()

    my_info_page.save_button.click()