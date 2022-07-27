import time

import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='function')
def create_webdriver():
    wd = Chrome()
    wd.implicitly_wait(5)
    wd.maximize_window()
    wd.get('https://www.ketangpai.com/#/login')
    yield wd
    time.sleep(5)
    wd.quit()