#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests,time,random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_excel('C:/Users/arora/Desktop/onelogica/linkedin/employee.xlsx')
urls = df['pro_url'].tolist()

#creating an object for webdriver
driver=webdriver.Chrome()
driver.get("https://linkedin.com/uas/login")
time.sleep(5)
 
# entering username
username = driver.find_element(By.ID, "username")
 
# Enter Your Email Address
username.send_keys("rishikatec64@gmail.com") 
 
# entering password
pword = driver.find_element(By.ID, "password")
 
# Enter Your Password
pword.send_keys("Rishumona@2003")       
 
# Clicking on the log in button
driver.find_element(By.XPATH, "//button[@type='submit']").click() 
time.sleep(20)

for url in urls:
    #opening the profile using driver
    driver.get(url) 
    # scrolling down to the bottom of the page
    SCROLL_PAUSE_TIME=5
    last_height=driver.execute_script("return document.body.scrollHeight")

    for i in range(3):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height=driver.execute_script("return document.body.scrollHeight")
        if new_height==last_height:
            break
        last_height=new_height

    #using beautiful soup to extract the html tags
    src=driver.page_source
    soup=BeautifulSoup(src,'lxml')

    #extracting the html tags to find the name and place of work
    name_div=soup.find('div',{'class':'pv-text-details__left-panel'})
    #extracting html tags to find location
    intro=soup.find('div',{'class':'pv-text-details__left-panel mt2'})

    name_loc = name_div.find("h1") 
    # Extracting the Name
    name = name_loc.get_text().strip()
    # strip() is used to remove any extra blank spaces

    # this gives us the HTML of the tag in which the Company Name is present
    works_at_loc = name_div.find("div", {'class': 'text-body-medium'})
    # Extracting the Company Name
    works_at = works_at_loc.get_text().strip()
    print("\n"+name)
    print(works_at)

    # this gives us the HTML of the tag in which the location is present
    location_loc = intro.find_all("span", {'class': 'text-body-small'})
 
    # Ectracting the Location
    location = location_loc[0].get_text().strip()
    print(location)

    #extracting the html tags to find the number of connections
    conn_div = soup.find('li', {'class': 'text-body-small'})
    conn_loc = conn_div.find("span", {'class': 't-bold'})
    connection = conn_loc.get_text().strip()
    print("Connections: "+connection)

    #printing the about of the profile
    print("\nAbout:")
    abt_sec=soup.find('div',{'class':'display-flex full-width'})
    about=abt_sec.get_text().strip()
    print(about)

    print("\nExperience:")
    #extracting the html tags to find the experience of the profile
    exp_sec=soup.find('div',{'class':'pvs-list__outer-container'}).find('ul')
    job_loc=exp_sec.find('span',{'class':'visually-hidden'})

    #printing the job title, company name and duration from the experience section
    job_title=job_loc.get_text().strip()
    print(job_title)
    comp_loc=exp_sec.find('span',{'class':'t-14 t-normal'}).find('span')
    comp_title=comp_loc.get_text().strip()
    print(comp_title)
    time_loc=exp_sec.find('span',{'class':'t-14 t-normal t-black--light'}).find('span')
    time_title=time_loc.get_text().strip()
    print(time_title)
    
driver.quit()


# In[13]:





# In[ ]:




