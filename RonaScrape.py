from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException

from selenium import webdriver

import time

check = 0

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

driver = webdriver.Chrome()
driver.get('https://massvax.maryland.gov/')
dates = []
time.sleep(1)
# while check == 0: 
while check == 0: 
# click radio button
	time.sleep(1)
	python_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[2]/div[2]/button')
	python_button.click()

	time.sleep(1)

	python_button = driver.find_elements_by_xpath('//*[@id="root"]/div/main/div/div/form/span[1]/div/label/input')[0]
	python_button.click()
	python_button = driver.find_elements_by_xpath('//*[@id="root"]/div/main/div/div/form/span[2]/div/label/input')[0]
	python_button.click()
	python_button = driver.find_elements_by_xpath('//*[@id="root"]/div/main/div/div/form/span[3]/div/fieldset/div[3]/label[1]/input')[0]
	python_button.click()
	python_button = driver.find_elements_by_xpath('//*[@id="root"]/div/main/div/div/form/span[4]/div/fieldset/div[2]/label[2]/input')[0]
	python_button.click()
	python_button = driver.find_elements_by_xpath('//*[@id="root"]/div/main/div/div/form/div/button[1]')[0]
	python_button.click()
	time.sleep(1.5)

	python_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/p')
	python_button.click()
	time.sleep(1.5)
	python_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/button')
	python_button.click()
	time.sleep(1.7)

	for x in range(20):
		python_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/button')
		python_button.click()
		time.sleep(0.3)
		python_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/button')
		python_button.click()
		time.sleep(0.3)
		for i in range(1,8):
			dates.append(['//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[{i}]/span'])
			print(date)
		date = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]/span')
		prop = date.get_property('disabled')
		print(prop)
		if prop != None: 
			print("Worked")
			check = 1
			break
	driver.refresh()


	if check == 1:
		break

# dates = []
# for i in range(1,8):
# 	for z in range(1,6):
# 		dates.append([f'//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{z}]/td[{i}]/span'])

# dates.remove([f'//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{5}]/td[{4}]/span'])
# dates.remove([f'//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{5}]/td[{5}]/span'])
# dates.remove([f'//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{5}]/td[{6}]/span'])
# dates.remove([f'//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[{5}]/td[{7}]/span'])

# print(len(dates))