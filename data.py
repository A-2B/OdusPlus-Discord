from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def data(ID,PASS):
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://odusplus-ss.kau.edu.sa/PROD/twbkwbis.P_WWWLogin")

  driver.implicitly_wait(5)

  IDs = driver.find_element_by_id("UserID")
  PASSs = driver.find_element_by_name("PIN")
  IDs.send_keys(ID)
  PASSs.send_keys(PASS)

  driver.implicitly_wait(5)

  LOGIN = driver.find_element(By.XPATH,"//*[@id='loginform']/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/a")
  LOGIN.click()

  driver.implicitly_wait(5)
  
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

  get_source = driver.page_source
  if "الحاسبات وتقنية المعلومات" in get_source:
    if "علوم الحاسبات" in get_source:
      return "CS"
    if "تقنية المعلومات" in get_source:
      return "IT"
    if "نظم المعلومات" in get_source:
      return "IS"