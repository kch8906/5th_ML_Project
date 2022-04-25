import os
import warnings
warnings.filterwarnings(action='ignore')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

chromedriver = "C:/jupyter_home/Machine_Learning/ML_Project_5th/5th_ML_Project/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1920, 1080)
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")

elem = driver.find_element_by_name("query")
elem.send_keys("눈 감은 사진")
elem.send_keys(Keys.RETURN)



driver.find_elements_by_css_selector("._image._listImage")[0].click()
