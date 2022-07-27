from page.login_page import LoginPage
from page.locator import Login
from common.logger import log


class TestLogin:
    def test_login_error(self, create_webdriver):
        webdriver = create_webdriver
        wd = LoginPage(webdriver)
        wd.login('123456789', '123456789')
        text = wd.get_text(Login.login_error_username_no_existent, '登录错误弹窗-用户名未注册')
        try:
            assert "用户不存在" == text
        except AssertionError as e:
            log.error('用例：【登录错误弹窗】测试失败')
            raise e
        else:
            log.info('用例：【登录错误弹窗】测试通过')
