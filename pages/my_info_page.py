class MyInfoPage:

    def __init__(self, page):
        self.page = page

        # Employee name
        self.first_name = page.locator('[name="firstName"]')
        self.middle_name = page.locator('[name="middleName"]')
        self.last_name = page.locator('[name="lastName"]')

        # Employee ID
        self.employee_id = (
            page.get_by_text("Employee Id")
            .locator("..")
            .locator("..")
            .locator("input")
        )

        # Other ID
        self.other_id = (
            page.get_by_text("Other Id")
            .locator("..")
            .locator("..")
            .locator("input")
        )

        # Driver's License Number
        self.drivers_license = (
            page.get_by_text("Driver's License Number")
            .locator("..")
            .locator("..")
            .locator("input")
        )

        # Marital Status
        self.marital_status_dropdown = (
            page.get_by_text("Marital Status")
            .locator("..")
            .locator("..")
            .locator(".oxd-select-text")
        )

        self.married_option = page.get_by_role("listbox").get_by_text("Married", exact=True)

        # Save button
        self.save_button = page.locator("form").first.get_by_role(
        "button", name="Save"
        )