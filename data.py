from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Once it has the inputs, it makes a webdriver chrome from selenium to navigate and login.
def data(ID,PASS):
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

#Chrome enters the URL and waits 5 seconds just to make sure everything is loaded.
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://odusplus-ss.kau.edu.sa/PROD/twbkwbis.P_WWWLogin")

  driver.implicitly_wait(5)

#Inputs the ID and PASS into the correct elements.  
  IDs = driver.find_element_by_id("UserID")
  PASSs = driver.find_element_by_name("PIN")
  IDs.send_keys(ID)
  PASSs.send_keys(PASS)

  driver.implicitly_wait(5)

#Navigates via XPATH
  LOGIN = driver.find_element(By.XPATH,"//*[@id='loginform']/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/a")
  LOGIN.click()

  driver.implicitly_wait(5)
  
#Returns False if the current URL which is incorrect ID or PASS.
  url = driver.current_url
  if url == "https://odusplus-ss.kau.edu.sa/PROD/twbkwbis.P_ValLogin":
    return False
    
  driver.implicitly_wait(15)
  
  SEARCH = driver.find_element(By.XPATH,"/html/body/div[5]/table[2]/tbody/tr[2]/td[2]/a")
  SEARCH.click()
    
  driver.implicitly_wait(15)

  SEARCH = driver.find_element(By.XPATH,"/html/body/div[5]/table[1]/tbody/tr[8]/td[2]/a")
  SEARCH.click()

  driver.implicitly_wait(15)
  
  SEARCH = driver.find_element(By.XPATH,"/html/body/div[5]/table[1]/tbody/tr[2]/td[2]/a")
  SEARCH.click()

  driver.implicitly_wait(10)

#Once it reaches the destination, It simply finds the certain string to return certain major.
  get_source = driver.page_source
  if "الحاسبات وتقنية المعلومات" in get_source:
    if "علوم الحاسبات" in get_source:
      return "CS"
    if "تقنية المعلومات" in get_source:
      return "IT"
    if "نظم المعلومات" in get_source:
      return "IS"
