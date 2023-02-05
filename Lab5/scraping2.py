from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

service = Service('webdriver/chromedriver.exe')
driver = webdriver.Chrome(service = service)

driver.get('https://www.printables.com/pl/model?period=month')




#onetrust-accept-btn-handler
#button = driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler')

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
button.click()


elements = []
for i in range(1, 11):
    selector = '#app-root > app-baselayout > div > ng-component > ng-component > app-market-list > app-sticky-sidebar > main > div > div > app-load-more-infinity-with-placeholder > div > div > print-card:nth-child('+str(i)+') > div > div.card > h3 > a'
    element = driver.find_element(By.CSS_SELECTOR, selector)
    elements.append(element.text)

print("A list of 10 currently popular 3D printing models:")
for value in elements:
    print(value)

#time.sleep(1000)

plik = "3Dprint_models.json"

with open('Lab5/'+plik, 'w') as f:
    json.dump(elements, f)

driver.close()

