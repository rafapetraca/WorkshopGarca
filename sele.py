from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.google.com.br')

elemento = browser.find_element_by_xpath('//*[@id="lst-ib"]')
elemento.click()
elemento.send_keys('big data fatec')

pesquisa = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]')
pesquisa.click()

