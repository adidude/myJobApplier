import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_size(1254,1047)
driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_AL%3Dtrue%26geoId%3D101165590%26keywords%3Dgraduate%2520software%2520engineer%26location%3DUnited%2520Kingdom%26sortBy%3DR&trk=public_jobs_nav-header-signin")

driver.find_element_by_id("username").send_keys("menon.or.adithya@gmail.com")
driver.find_element_by_id("password").send_keys("")
# Click log in
driver.find_element_by_class_name("btn__primary--large").click()

# Create webdriverwait to wait for page to load
pageLoader = WebDriverWait(driver,300,2,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
pageLoader.until(EC.visibility_of_any_elements_located((By.CLASS_NAME,"artdeco-pagination__indicator")))

# Gets all the page change buttons
pageCollector = driver.find_elements_by_class_name("artdeco-pagination__indicator")

# The total number of pages
totalPages = int(pageCollector[len(pageCollector)-1].get_attribute("data-test-pagination-page-btn"))

newCount = 0
errorChecker = WebDriverWait(driver,5,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

def openNextPage(currPage, newCount):
	pageLoader.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "artdeco-pagination__indicator")))
	pageCollector = driver.find_elements_by_class_name("artdeco-pagination__indicator")

	if (currPage < 9):
		pageCollector[currPage].click()
	else:
		pageCollector[newCount + 6].click()
		newCount += 1
		if (newCount > 2):
			newCount = 0

for currPage in range(0, totalPages):
	try:
		errorChecker.until(EC.element_to_be_clickable((By.CLASS_NAME,"jobs-search-no-results__reload")))
		driver.find_element_by_class_name("jobs-search-no-results__reload").click()
		openNextPage(currPage, newCount)
	except:
		openNextPage(currPage, newCount)
		
		""" 
		pageLoader.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "artdeco-pagination__indicator")))
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
 		"""
