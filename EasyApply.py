import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import *

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_size(1254,1047)
driver.get("https://www.linkedin.com")
driver.find_element_by_id("session_key").send_keys("menon.or.adithya@gmail.com")
driver.find_element_by_id("session_password").send_keys("")
driver.find_element_by_css_selector(".sign-in-form__submit-button").click()



pageLoader = WebDriverWait(driver,300,2,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
pageLoader.until(EC.element_to_be_clickable((By.CLASS_NAME, "msg-overlay-bubble-header__control")))
closeMessages = driver.find_elements_by_class_name("msg-overlay-bubble-header__control")
closeMessages[1].click()
jobsButton = driver.find_elements_by_class_name("global-nav__primary-link")
jobsButton[2].click()

pageLoader.until(EC.element_to_be_clickable((By.CLASS_NAME,"jobs-search-box__text-input")))
inputBoxes = driver.find_elements_by_class_name("jobs-search-box__text-input")

inputBoxes[0].send_keys("graduate software engineer")
inputBoxes[3].send_keys("United Kingdom")

driver.find_element_by_class_name("jobs-search-box__submit-button").click()

pageLoader.until(EC.element_to_be_clickable((By.CLASS_NAME,"artdeco-pill")))
options = driver.find_elements_by_class_name("artdeco-pill")
options[7].click()

easyToggle = pageLoader.until(EC.element_to_be_clickable((By.CLASS_NAME,"artdeco-toggle")))
easyToggle.click()

driver.find_element_by_class_name("reusable-search-filters-buttons").click()

time.sleep(5)

total_results = driver.find_element_by_class_name("display-flex.t-12.t-black--light.t-normal")
total_results_int = int(total_results.text.split(' ',1)[0].replace(",",""))
#print("Jobs available:" + str(total_results_int))



pageCollector = driver.find_elements_by_class_name("artdeco-pagination__indicator")

print("Number of pages: " + str(len(pageCollector)))
totalPages = int(pageCollector[len(pageCollector)-1].get_attribute("data-test-pagination-page-btn"))

newCount = 0

for currPage in range(0, totalPages):
	time.sleep(2)
	pageCollector = driver.find_elements_by_class_name("artdeco-pagination__indicator")

	if (currPage < 9):
		pageCollector[currPage].click()
	else:
		try:
			pageCollector[newCount + 6].click()
			newCount += 1
			if (newCount > 2):
				newCount = 0
		except IndexError:
			driver.find_element_by_class_name("jobs-search-no-results__reload").click()
			time.sleep(1)
			pageCollector[newCount + 6].click()
			newCount += 1
			if (newCount > 2):
				newCount = 0




#isFirst = True
#for page in pages:
#	time.sleep(0.5)
#	jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
#	jobs[len(jobs)-1].click()
#	if (isFirst):
#		isFirst = False
#		continue
#	page.click()

#driver.quit()
