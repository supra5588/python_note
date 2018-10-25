"""
slenium

"""

from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/ethanlin/PycharmProjects/Hello/chromedriver')
driver.fullscreen_window()  # if you use mac must add this code
driver.get('https://www.google.com.tw')

# """find_element_by_id"""
# # driver.find_element_by_id("cellphone").send_keys('0965109929')

# """find_element_by_name"""
# # driver.find_element_by_name("q").send_keys('hello\n')  # \n換行外也代表enter

# """find_element_by_link_text"""
# driver.find_element_by_link_text("Gmail").click()  # You can find it in html <a class = xxx href = URL>link_text</a>
# driver.back()

# """find_element_by_partial_link_text"""
# driver.find_element_by_partial_link_text("mail").click()  # The partial link text mean incomplete text
# time.sleep(5)  # Wait for 5 sec ,Rember import time module first

# """find_elements_by_tag_name"""
# elments = driver.find_elements_by_tag_name('a')  # find_elements_by_tag_name tag 太多難以尋找到正確目標
# for elment in elments:
#     if '登入' in elment.text:  # 尋找包含：登入 的tag
#         elment.click()

# """find_element_by_class_name"""
# driver.find_element_by_class_name("gb_P").click()

# """find_element_by_xpath"""
# driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()  # Xml type use ChroPath to find it

"""find_element_by_css_selector"""
driver.find_element_by_css_selector("#lst-ib").send_keys('hello world\n')
driver.back()
time.sleep(3)
driver.quit()  # Close browser
