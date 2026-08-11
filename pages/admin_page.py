class AdminPage:

    def __init__(self, page):
        self.page = page

        self.admin_menu = page.locator(
            'a[href="/web/index.php/admin/viewAdminModule"]'
        )

        self.confirm_delete_button = page.locator(
            "button.oxd-button--label-danger"
        )