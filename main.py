from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import PIL.Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import time 
import datetime
from time import strftime


# Initialize WebDriver for Chrome
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

username = 'for_testing_opp' # you have to change it
password = 'XXXXX' # you have to change it

# Define XPaths
username_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input'
password_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input'
login_button_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button'
not_now_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
change_pp_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div/div[2]/div[1]/div[2]/div'
upload_pp_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]'
file_input_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/form/input'  

driver.get("https://www.instagram.com/accounts/edit/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, username_xpath)))
username_field = driver.find_element(By.XPATH, username_xpath)
username_field.send_keys(username)

password_field = driver.find_element(By.XPATH, password_xpath)
password_field.send_keys(password)

login_button = driver.find_element(By.XPATH, login_button_xpath)
login_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, not_now_xpath)))
not_now_button = driver.find_element(By.XPATH, not_now_xpath)
not_now_button.click()

while True:
	if int(strftime("%S")) == 00:
		print(f"Starting the time -> {strftime('%H-%M')}")
		img = PIL.Image.open("bg.jpeg")
		img = img.resize((110, 110))
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("arialbd.ttf", 16)
		draw.text((15, 38), f"{strftime('%Y-%m-%d')}", (0, 0, 0), font=font)
		draw.text((33.5, 60), f"{strftime('%H:%M')}", (0, 0, 0), font=font)
		img.save('sample-out.jpeg')

		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, change_pp_xpath)))
		change_pp_button = driver.find_element(By.XPATH, change_pp_xpath)
		change_pp_button.click()

		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, file_input_xpath)))
		file_input = driver.find_element(By.XPATH, file_input_xpath).send_keys('C:\\Users\\yaqub\\OneDrive\\Masaüstü\\ig\\sample-out.jpeg')
		time.sleep(1)

driver.quit()
