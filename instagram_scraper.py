from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/')

sleep(4)

usrname_txtbox = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usrname_txtbox.send_keys('miniproj6')
psswrd_txtbox = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
psswrd_txtbox.send_keys('AP@4012')
psswrd_txtbox.send_keys(Keys.ENTER)
sleep(6)
target = 'alidaei'
browser.get('https://www.instagram.com/' + target + '/')
sleep(5)
usr_id = browser.find_elements(By.TAG_NAME, 'h2')
print('*******************************', usr_id[0].text, '*****************************')
usr_name = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[1]/span')
print('*******************************', usr_name.text, '*****************************')
usr_bio = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1')
print('*******************************', usr_bio.text, '*****************************')
usr_flwrs = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span')
print('*******************************', usr_flwrs.text, '*****************************')
usr_flwngs = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span')
print('*******************************', usr_flwngs.text, '*****************************')
usr_psts = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span')
print('*******************************', usr_psts.text, '*****************************')
usr_photo = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/div/div/span/img')
print('*******************************', usr_photo.get_attribute('src'), '*****************************')


sleep(200)