# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:45:13 2022

@author: 24099
"""

import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import datetime
from dateutil.relativedelta import relativedelta

from lxml import etree
# # import pymysql
# import xlwt 

import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


## 登陆部分，并发送hello 


options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\bing_zhihu\\'}
options.add_experimental_option('prefs', prefs)
ziwu = webdriver.Chrome(options=options)

 
# try:
ziwu.get("https://claude.ai/chat/1934be9f-3577-4b66-a03a-473d2d36036d")
time.sleep(60)
ziwu.switch_to.active_element.send_keys('hello')

# ziwu.find_element(By.CLASS_NAME,"flex items-center flex-grow overflow-x-hidden").send_keys("hello word")
# ziwu.find_element(By.NAME,"username").send_keys("airglow2")
# ziwu.find_element(By.NAME,"password").send_keys("123456")
ziwu.find_element(By.XPATH,"/html/body/main/div/div/fieldset/div[2]/div").click()

time.sleep(5)

question = '请用知乎高赞的方式回答下列问题，请直接输出回答，不要输入任何与回答无关的话'

ziwu.switch_to.active_element.send_keys(str(question))



ziwu.find_element(By.XPATH,"/html/body/div[5]/div/div[5]/div/fieldset/div[2]/button").click()

time.sleep(60)

page_text = ziwu.page_source

ques_list = re.findall(r'<div class="contents"><p class="whitespace-pre-wrap">(.*?)</p></div>',page_text)

answer = ques_list[-1]

# print(str(answer))

ziwu.refresh()

time.sleep(5)

## 发送需要对话的内容,并获取回答

def ask_and_answer(question):
    
    ziwu.refresh()

    time.sleep(5)    
    
    question = str(question)
    
    

    ziwu.switch_to.active_element.send_keys(str(question))
    
    
    
    ziwu.find_element(By.XPATH,"/html/body/div[3]/div/div[5]/div/fieldset/div[2]/button").click()
    
    
    # /html/body/div[3]/div/div[5]/div/fieldset/div[2]/button/svg/path
    
    time.sleep(120)
    
    page_text = ziwu.page_source
    
    ques_list = re.findall(r'<div class="contents"><p class="whitespace-pre-wrap">(.*?)</p></div>',page_text,re.S)
    
    answer = re.sub('<(.*?)>','',ques_list[-1]).replace('\n','')
    
    print(str(answer))
    
    ziwu.refresh()
    
    time.sleep(5)
    
    return answer



## 询问正文内容




# def input_answer(iuput_char):
#     driver = webdriver.Edge('D:\conda\Scripts\MicrosoftWebDriver.exe') 
    
#     driver.get('https://www.tdchat.com/')
     
#     sleep(5)
#     input_key=driver.find_element(By.ID,"key").send_keys('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')
#     input_word=driver.find_element(By.NAME,"kw-target").send_keys(iuput_char)
#     clickkey=driver.find_element(By.ID,"ai-btn").click()
    
    
#     sleep(60)
#     page_text = driver.page_source  
#     tree = etree.HTML(page_text)
#     li_list=tree.xpath('/html/body/div[2]/article/div/ul/li[3]/pre/text()')
    
#     retstr = str(li_list).replace('[','').replace(']','')
    
#     return retstr

# answer = input_answer('中午吃什么')
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\bing_zhihu\\'}
options.add_experimental_option('prefs', prefs)
zhihu = webdriver.Chrome(options=options)
# driver = webdriver.Edge('D:\conda\Scripts\MicrosoftWebDriver.exe') 

zhihu.get('https://www.zhihu.com/creator/featured-question/recommend')
 
sleep(15)

# def zhizhu():

zhihu.get('https://www.zhihu.com/creator/featured-question/recommend')

sleep(20)
page_textzhi = zhihu.page_source  
ques_listzhi = re.findall(r'<div class="css-1rs9lm3"><a class="css-1s2rixt" href="(.*?) target=',page_textzhi)
req_listzhi = re.findall(r'" target="_blank">(.*?)</a><div class="css',page_textzhi)


# '<div class="css-1rs9lm3"><a class="css-1s2rixt" href="(.*?) target='

# '" target="_blank">(.*?)</a><div class="css'
link_list = []
for link in ques_listzhi:
    link = link.split(' ')[0].replace('?','/').replace('"','')
    link_list.append(link)
    
for num in range(0,len(link_list)-1):
    
    
    # ask_and_answer('如何评价放寒假')
    
    answerzhihu = ask_and_answer(req_listzhi[num].split('</div>')[-1])
    
    # answer = 'test'
    # driver.switch_to.active_element.send_keys(answer)
    zhihu.get(link_list[num])
    sleep(10)
    # try:
    #     driver.find_element(By.LINK_TEXT,"发布回答").click()
    #     sleep(5)
    # except:
    #     print('error')
    zhihu.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/div[1]/div[2]/div/div[2]/div/div/div[1]/a/button").click()
    sleep(2)    
    zhihu.switch_to.active_element.send_keys(answerzhihu.replace('\n','').replace("'",''))
    sleep(2)
    # driver.find_element(By.LINK_TEXT,"发布回答").click()
    # sleep(30)
    zhihu.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/button[2]").click()

            
    sleep(5)
# ask_and_answer('如何评价放寒假')
# ask_and_answer('如何评价放暑假')
# ask_and_answer('如何评价放秋假')
# time.sleep(10)

# /html/body/div/div/main/div/div/div[1]/div[1]/div/div[2]/div/div/div[1]/a/button





# /html/body/div[3]/div/div[5]/div/fieldset/div[2]/button
# lian = 'https://data.meridianproject.ac.cn/science-data/download-list/?file_type=file&ift_id=220&datetime1='+riqi+"000000&datetime2="+riqi+"235959&page_num=1"

# ziwu.get(lian)
# time.sleep(10)
# ziwu.find_element(By.XPATH,"//input[@onclick='javascript:downloadall()']").click()
# time.sleep(180)



        # mulu = os.listdir(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\SYS\\RNX")
        # mingzi = []
        # for wenjian in mulu:
        #     if wenjian[-3:] == "zip":
        #         mingzi.append(wenjian)
        # # for file_path in mingzi:
        #     try:
        #         z = zipfile.ZipFile(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\FKT\\RSF\\"+file_path, 'r')
        #         z.extractall(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\FKT\\RSF")        
        #         z.close()
        #     except:
        #         continue
    # except:
    #     j = 0.00
    #     while j <= 10:
    #         try:
    #             j = j + 1
# ziwu.get("https://data.meridianproject.ac.cn/")
# time.sleep(10)
# ziwu.find_element(By.NAME,"username").send_keys("airglow2")
# ziwu.find_element(By.NAME,"password").send_keys("123456")
# ziwu.find_element(By.XPATH,"//input[@value='登录']").click()
# time.sleep(10)

# lian = 'https://data.meridianproject.ac.cn/science-data/download-list/?file_type=file&ift_id=220&datetime1='+riqi+"000000&datetime2="+riqi+"235959&page_num=1"

# ziwu.get(lian)
# time.sleep(10)
# ziwu.find_element(By.XPATH,"//input[@onclick='javascript:downloadall()']").click()
# time.sleep(180)
        
        
        
        #         mulu = os.listdir(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\SYS\\RNX")
        #         mingzi = []
        #         for wenjian in mulu:
        #             if wenjian[-3:] == "zip":
        #                 mingzi.append(wenjian)
        #         # for file_path in mingzi:
        #         #     z = zipfile.ZipFile(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF\\"+file_path, 'r')
        #         #     z.extractall(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF")        
        #         #     z.close()
        #     except:
        #         continue
        # continue
        
        
    # mulu = os.listdir(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\FKT\\RSF")
    # mingzi = []
    # for wenjian in mulu:
    #     try:
    #         if wenjian[-3:] != "RSF":
    #             os.remove(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\FKT\\RSF\\"+wenjian)
    #     except:
    #         continue


    
# for aa in [115,116,20,21,14,15]:    
    
# for i in range(200,4600):
    # riqi = (datetime.datetime.now()- relativedelta(days=i)).strftime("%Y-%m-%d").replace('-','')
     
    # if os.path.isdir(riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF"):
    #     pass
    # else:
    #     os.makedirs(riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF")              

    # options = webdriver.ChromeOptions()
    
    # yuan = os.getcwd()    
    
    # options = webdriver.ChromeOptions()
    # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF"}
    # options.add_experimental_option('prefs', prefs)
    # ziwu = webdriver.Chrome(options=options)
    
    # ziwu.get("https://data.meridianproject.ac.cn/")
    # time.sleep(10)
    # ziwu.find_element(By.NAME,"username").send_keys("airglow2")
    # ziwu.find_element(By.NAME,"password").send_keys("123456")
    # ziwu.find_element(By.XPATH,"//input[@value='登录']").click()
    # time.sleep(10)
    
    # lian = 'https://data.meridianproject.ac.cn/science-data/download-list/?file_type=file&ift_id=19&datetime1='+riqi+"000000&datetime2="+riqi+"235959&page_num=1"

    # ziwu.get(lian)
    # time.sleep(10)
    # ziwu.find_element(By.XPATH,"//input[@onclick='javascript:downloadall()']").click()
    # time.sleep(180)


    # mulu = os.listdir(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF")
    # mingzi = []
    # for wenjian in mulu:
    #     if wenjian[-3:] == "zip":
    #         mingzi.append(wenjian)
    # for file_path in mingzi:
    #     z = zipfile.ZipFile(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF\\"+file_path, 'r')
    #     z.extractall(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF")        
    #     z.close()
        
    # mulu = os.listdir(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF")
    # mingzi = []
    # for wenjian in mulu:
    #     try:
    #         if wenjian[-3:] != "RSF":
    #             os.remove(yuan+"\\"+riqi[0:4]+"\\"+riqi[4:6]+"\\"+riqi[6:8]+"\\ZLT\\RSF\\"+wenjian)
    #     except:
    #         continue
# for aa in [115,116,20,21,14,15]:    
    
