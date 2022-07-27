import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

wd = Chrome()
wd.implicitly_wait(5)
wd.maximize_window()

wd.get('https://www.baidu.com/')

input_box = (By.ID, 'kw')
input_box_ele = wd.find_element(*input_box)
input_box_ele.send_keys('python')
wd.find_element(By.ID, 'su').click()

loc_help = (By.XPATH, '//a[text()="帮助"]')
WebDriverWait(wd, 5, 0.5).until(expected_conditions.presence_of_element_located(loc_help))
ele = wd.find_element(*loc_help)
# ele.location_once_scrolled_into_view
# wd.execute_script("arguments[0].scrollIntoView(false);", ele)
ele.click()

time.sleep(5)
wd.quit()
