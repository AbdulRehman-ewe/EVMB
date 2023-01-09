import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
service = Service("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
service.start()
driver = webdriver.Chrome(service=service)
driver.get("https://demo.evalmybrand.com/#/app/main/customer/dashboard")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys("B.K.Goenka@yopmail.com")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys("P@$$W0rd1")
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/app-root/app-login/div/div/div[1]/div/div/div[1]/div[2]/app-eval-form-button/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="main-data"]/div[1]/app-common-header/div/div/div[2]/div/button').click()
time.sleep(2)
driver.execute_script("document.querySelector('.d-flex.flex-column.overflow-auto').scrollBy(0, 500)")
time.sleep(4)
button= driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/mat-dialog-container/app-date-picker/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/div[1]/div[2]/button[7]")
# Make the button visible
driver.execute_script("arguments[0].style.display='block'", button)
# Click the button
button.click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/mat-dialog-container/app-date-picker/div/div[2]/mat-tab-group/div/mat-tab-body/div/div/div[2]/div/ngx-daterangepicker-material/div/div[3]/div/button[2]").click()
time.sleep(4)
for x in range(15):
  path ="#overall_data > svg > rect.mybar.pageBar"+str(x)+".pageBar"
  time.sleep(2)
  try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, path)))
    actions = ActionChains(driver)
    # Use the move_to_element() method to move the mouse cursor to the element
    actions.move_to_element(element).perform()
    element.click()
    Fromdate=driver.find_element(By.CSS_SELECTOR,'#pdf > div > app-glasdoor-dashboard > div > div.p-2.ng-star-inserted > mat-card > div.cursor-pointer.ng-star-inserted > app-glasdoor-overall-page > div > div > div')
    time.sleep(5)
    list1= Fromdate.text
    print(list1)
    driver.find_element(By.CSS_SELECTOR, "#overall_data > svg > text:nth-child(3)").click()
    time.sleep(2)
  except NoSuchElementException:
    print("No Data")
    time.sleep(4)
  except Exception as e:
    print(f'Exception:{e}')

# Create a dataframe from the list
df = pd.DataFrame(list1, columns='columns')

# Write the dataframe to an Excel file
df.to_excel('my_list.xlsx', index=False)




