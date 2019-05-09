from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import src.FileOrder as fo
#NOTE: PLEASE IMPORT YOUR ACCOUNT AND TO DO LIST INFORMATION BY HAND ALSO CHECK FileOrder.py
#you can find where you need to write infos by searching "by hand" in code


theList = fo.get_aa()

driver_path = "../drivers/chromedriver.exe"
driver = webdriver.Chrome(driver_path)
link ="https://login.live.com/oauth20_authorize.srf?response_type=token&client_id=000000004C18365E&redirect_uri=ht" \
      "tps%3A%2F%2Fto-do.microsoft.com%2Fauth%2Fcallback&scope=https://substrate.office.com/Todo-Internal.ReadWrite&state=eyJ0b2tlblR5cGUiOiJzeW" \
      "5jVG9rZW4iLCJmbG93VHlwZSI6Im1zYSJ9&aadredir=1"

driver.get(link)
sleep(2)

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")

#DONT FORGET TO IMPORT YOUR ACCOUNT INFORMATION HERE BY HAND
driver.find_element_by_name("loginfmt").send_keys("ENTER YOUR MAIL HERE")
driver.find_element_by_id("idSIButton9").click()
driver.find_element_by_name("passwd").send_keys("ENTER YOUR PASSWORD HERE")
sleep(2)
driver.execute_script('document.getElementsByClassName("btn btn-block btn-primary")[0].click()')
# sleep(9)

i = 0
while True:
    try:

        xx = driver.execute_script('return document.getElementsByClassName("listItem-titleParsed")[{0}].innerText'.format(i))
        #ENTER THE EXACT NAME OF YOUR TO DO LIST HERE BY HAND
        if xx == "EXAMPLE: Movie List":
            driver.execute_script('document.getElementsByClassName("listItem-titleParsed")[{0}].click()'.format(i))
            break
        else:
            i += 1
    except:
        continue
sleep(3)
for t in theList:

    driver.find_element_by_id("baseAddInput-addTask").send_keys(str(t))
    driver.find_element_by_class_name("baseAdd-icon").send_keys()
    driver.execute_script('document.getElementsByClassName("baseAdd-icon")[1].click()')
    sleep(1)

sleep(8)
driver.quit()
