#!/usr/bin/python3
import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()
#opts.headless=True
driver=Firefox(options=opts)
url='https://www.orbitz.com'

input_values=[
    'Costa Rica',
    '03/30/2021',
    '04/7/2021',
    '1',
    '2',
    '0'
    ]

input_id=[
    'hotel-destination-hp-hotel',
    'hotel-checkin-hp-hotel',
    'hotel-checkout-hp-hotel',
    'hotel-rooms-hp-hotel',
    'hotel-1-adults-hp-hotel',
    'hotel-1-children-hp-hotel'
    ]

try: 
    driver.get(url)
    element=None
    for value,id in zip(input_values,input_id):
        element=driver.find_element_by_id(id)
        element.send_keys(value)
    element=driver.find_element_by_css_selector('#gcw-hotel-form-hp-hotel > div:nth-child(11) > label:nth-child(1) > button:nth-child(1)')
    element.send_keys(Keys.ENTER)
    

    
finally:
    time.sleep(30)
    driver.quit()
