

# In[165]:


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

MAX_COMMENTS = 100

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/')

sleep(4)

import pyautogui as pag
import win32gui


MAX_FOLLOWERS = 100


MAX_POSTS = 5
MAX_COMMENTS = 100


# In[ ]:


usrname_txtbox = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usrname_txtbox.send_keys('miniproj6.2')
psswrd_txtbox = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
psswrd_txtbox.send_keys('AP@4012')
psswrd_txtbox.send_keys(Keys.ENTER)
sleep(4)


# In[ ]:


target = 'miniproj6.2'
browser.get('https://www.instagram.com/' + target + '/followers/')
sleep(5)


# In[ ]:


sleep(5)
while True:
    pag.moveTo(895, 815, 0.1)
    pag.scroll(-5000)
    sleep(4)
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 895, 815)
    if color == 11053224:
        break


# In[ ]:


followers = []
for i in range(MAX_FOLLOWERS):
    try:
        follower = browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[{i + 1}]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div')
        followers.append(follower.text)
    except:
        pass


# In[ ]:


len(followers)


# In[ ]:


browser.get('https://www.instagram.com/' + target + '/following/')
sleep(5)
while True:
    pag.moveTo(895, 815, 0.1)
    pag.scroll(-5000)
    sleep(4)
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 895, 815)
    if color == 11053224:
        break


# In[ ]:


followers


# In[ ]:


friends = []
for i in range(MAX_FOLLOWERS):
    try:
        following = browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[{i + 1}]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div')
        if (following.text) not in followers:
            unflw_btn = browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i + 1}]/div/div/div/div[3]/div/button')
            unflw_btn.click()
            sleep(1)
            submit_unfollow = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
            submit_unfollow.click()
            sleep(2)
        else:
            friends.append(following.text)
    except:
        pass


# In[ ]:


true_friends = {frnd: 0 for frnd in friends}


# In[163]:

cnt = 0
browser.get('https://www.instagram.com/' + target + '/')
for j in range(MAX_COMMENTS):
    for i in range(3):
        cnt = 0
        try:
            ith_post = browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/article/div/div/div[{j + 1}]/div[{i + 1}]/a/div/div[2]')
            ith_post.click()
            sleep(2)

            cnt = 0
            while cnt < MAX_COMMENTS:
                more_comments_btn = browser.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/li/div/button')
                if more_comments_btn:
                    more_comments_btn[0].click()
                else:
                    break
            cnt += 15
            sleep(2)
            cmntrs = []
            for k in range(MAX_COMMENTS):
                try:
                    cmnt = browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul[{k + 1}]/div/li/div/div/div[2]/h3/div/div/div/a')
                    if cmnt.text in true_friends.keys():
                        true_friends[cmnt.text.split('\n')[0]] += 1
                except:
                    pass
            
            try:
                exit_btn = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div')
                exit_btn.click()
            except:
                print('reedam')
        except:
            pass


# In[ ]:
print('Your true friends are:')
for itm in true_friends:
    if true_friends[itm] > 5:
        print(itm)

# %%
