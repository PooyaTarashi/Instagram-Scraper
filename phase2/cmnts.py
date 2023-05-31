
# In[2]:


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

MAX_COMMENTS = 100

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/')

sleep(4)


# In[3]:


usrname_txtbox = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usrname_txtbox.send_keys('miniproj6')
psswrd_txtbox = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
psswrd_txtbox.send_keys('AP@4012')
psswrd_txtbox.send_keys(Keys.ENTER)
sleep(6)


# In[76]:


target_post = 'https://www.instagram.com/p/CsrAn4zIkCV/'
browser.get(target_post)
sleep(5)


# In[77]:


cnt = 0

while cnt < MAX_COMMENTS:
    more_comments_btn = browser.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/li/div/button')
    if more_comments_btn:
        more_comments_btn[0].click()
    else:
        break
    cnt += 15
    sleep(2)



# In[78]:


import pandas as pd
import re


# In[87]:


def manipulate_comment(cmnt:list) -> pd.Series:
    # print('arg:', cmnt)
    commenter = cmnt[0]
    cmnt.pop(0)
    likes = 0
    for exp in reversed(cmnt):
        if 'likesReply' in exp:
            likes = (re.findall(r"\d+", exp))[1]
    i = 0
    for exp in reversed(cmnt):
        if 'View replies' in exp:
            cmnt.remove(exp)
        if 'likesReply' in exp:
            cmnt.remove(exp)
        if 'See translation' in exp:
            cmnt.remove(exp)
        if i > 5:
            break
        i += 1
        
    return pd.Series({'NAME': commenter, 'COMMENT': '\n'.join(cmnt), 'LIKES': likes})


# In[89]:


cmnts_ls = []

for i in range(MAX_COMMENTS):
    try:
        cmnt = browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/ul[{i + 1}]')
        cmnt = cmnt.text.split('\n')
        cmnts_ls.append(manipulate_comment(cmnt))
    except:
        pass


# In[91]:


df = pd.DataFrame(cmnts_ls)


# In[93]:

df.to_csv('output_comments.csv', index=False)

