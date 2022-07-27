from selenium.webdriver.common.by import By


class Login:
    """登录页面元素定位器"""
    # 账号输入框
    user_input = (By.XPATH, '//input[@placeholder="请输入邮箱/手机号/账号"]')
    # 密码输入框
    pwd_input = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登录按钮
    login_button = (By.XPATH, '//button[@class="el-button el-button--primary el-button--medium"]')
    # 登录失败弹窗-填写用户名未注册
    login_error_username_no_existent = (By.XPATH, '//p[text()="用户不存在"]')