"""
slenium

"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('/Users/ethanlin/PycharmProjects/Hello/chromedriver')
driver.get('https://www.google.com/')
driver.fullscreen_window()  # if you use mac must add this code

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

# """find_element_by_css_selector"""
# driver.find_element_by_css_selector("#lst-ib").send_keys('hello world\n')
# driver.back()
# time.sleep(3)

# driver.maximize_window()  # fullscreen windows it's use on windoes
# driver.minimize_window()    # Mac 執行會報錯 windows 正常

# time.sleep(2)
# titleName = driver.title
# print(titleName)
#
# currentUrl = driver.current_url
# print(currentUrl)
#
# driver.get('https://www.w3schools.com/html/default.asp')    #會覆蓋先前網址
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# urlSource = driver.page_source
# print(urlSource)

# selectElements = driver.find_element_by_id('month')
# months = Select(selectElements)
# months.select_by_visible_text('December')
#
# countriesElement = driver.find_element_by_id('country')
# countries = Select(countriesElement)
# countries.select_by_visible_text('Taiwan')
#
# driver.find_element_by_xpath("//form[@id='cf']//input[@value='View Calendar']").click()
#
# time.sleep(5)

driver.find_element_by_id('lst-ib').send_keys("hello")

driver.save_screenshot('截圖.jpg')  # 未指定路徑會存在當前資料夾下

driver.quit()  # Close browser
