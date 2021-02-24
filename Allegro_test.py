import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r"C:\Users\mnagr\PycharmProject\AllegroSelenium\drivers\chromedriver.exe")
wait = WebDriverWait(driver, 10)
driver.get("http://allegro.pl")
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-role="accept-consent"]')))
driver.find_element_by_css_selector('[data-role="accept-consent"]').click()
searchEntry = driver.find_element_by_css_selector('[placeholder="czego szukasz?"]')
searchEntry.send_keys("Iphone 11")
searchEntry.submit()
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "czarny")))
driver.find_element_by_link_text("czarny").click()
wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, '[data-analytics-view-custom-page="1"]')))
listElements = len(driver.find_elements_by_css_selector('[data-analytics-view-custom-page="1"]'))
print(listElements)
page = requests.get('https://allegro.pl/kategoria/smartfony-i-telefony-komorkowe-apple-48978?string=Iphone%2011&kolor=czarny&bmatch=baseline-cl-eyesa2-engag-dict43-ele-1-4-0306')
html = BeautifulSoup(page.content, "html.parser")
terms = html.find_all('[class="_9c44d_1zemI"]')
print(terms)