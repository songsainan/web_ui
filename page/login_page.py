from page.base_page import BasePage
from page.locator import Login


class LoginPage(BasePage):
    def login(self, username, password):
        self.input_send_keys(Login.user_input, username, '账号输入框')
        self.input_send_keys(Login.pwd_input, password, '密码输入框')
        self.click_element(Login.login_button, '登录按钮')