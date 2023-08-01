import re

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data_from_url(url):
    browser = webdriver.Chrome()

    browser.get(url)

    table = browser.find_element(By.CLASS_NAME, "table-tab-widget")
    room_rows = table.find_elements(By.CLASS_NAME, "unit-container")

    parsed_room_data = []

    for row in room_rows:
        dict = {"room number": re.search("(.*)#(\d\d\d\d)",row.find_element(By.CLASS_NAME, "td-card-name").get_attribute("innerHTML")).group(2),
         "price": re.search("(.*)\$(\d,\d\d\d)(.*)", row.find_element(By.CLASS_NAME, "td-card-rent").get_attribute("innerHTML")).group(2)}

        parsed_room_data.insert(0,dict)

    return parsed_room_data
