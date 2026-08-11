class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator('[name="username"]')
        self.password = page.locator('[name="password"]')
        self.login_button = page.locator('button[type="submit"]')

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        
        