import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.logger import log
from common.path import ERROR_IMG_DIR


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, locator, describe=None):
        """
        查找元素
        :param locator: 定位器
        :param describe: 元素描述
        :return:元素
        """
        WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(locator))
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            log.error('元素【{}】查找失败'.format(describe))
            self.save_error_img(describe)
            raise e
        else:
            log.info('元素【{}】查找成功'.format(describe))
        return ele

    def click_element(self, locator, describe):
        """
        点击元素
        :param locator: 定位器
        :param describe: 元素描述
        :return:
        """
        ele = self.get_element(locator, describe)
        WebDriverWait(self.driver, 5, 0.5).until(EC.element_to_be_clickable(locator))
        try:
            # ele.click()
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception as e:
            log.error('元素【{}】点击失败'.format(describe))
            self.save_error_img(describe)
            raise e
        else:
            log.info('元素【{}】点击成功'.format(describe))

    def save_error_img(self, describe):
        """
        保存错误截图
        :param describe: 描述
        :return:
        """
        now_time = time.strftime('%Y%m%d%H%M%S')
        img_name = now_time + describe + '.png'
        img_path = os.path.join(ERROR_IMG_DIR, img_name)
        try:
            self.driver.save_screenshot(img_path)
        except Exception as e:
            log.error('保存截图{}失败'.format(describe))
            raise e
        else:
            log.info('保存截图{}成功'.format(describe))

    def get_text(self, locator, describe):
        """
        获取元素文本信息
        :param locator: 定位器
        :param describe: 描述
        :return: 文本信息
        """
        ele = self.get_element(locator, describe)
        try:
            msg = ele.text
        except Exception as e:
            log.error('获取【{}】文本信息失败'.format(describe))
            raise e
        else:
            log.info('获取【{}】文本信息成功'.format(describe))

        return msg

    def input_send_keys(self, locator, value, describe):
        ele = self.get_element(locator, describe)
        try:
            ele.send_keys(value)
        except Exception as e:
            log.error('元素【{}】输入内容失败'.format(describe))
            raise e
        else:
            log.info('元素【{}】输入内容成功'.format(describe))
