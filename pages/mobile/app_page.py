def login(self, password):
    field = self.wait.until(
        EC.presence_of_element_located(AppLocators.TEXT_FIELD)
    )
    field.send_keys(password)

    self.click_first_button()
