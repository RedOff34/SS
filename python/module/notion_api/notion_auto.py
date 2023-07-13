from curses import window
from xml.etree.ElementPath import xpath_tokenizer
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import CalendarUI
import NewUserCal

def view_cal_auto(DBID):
    #브라우저 숨김 옵션
    options = webdriver.EdgeOptions()
    options.add_argument('headless')

    #크롬
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")

    #엣지 드라이버 사용
    driver=webdriver.Edge(executable_path='./module/anyang_video/msedgedriver.exe', options=options)
    #크롬드라이버
    #driver=webdriver.Chrome('./module/anyang_video/chromedriver.exe', options=options)
    url='https://www.notion.so/login'

    driver.get(url)
    time.sleep(5)
    
    '''
    #노션 id 로그인
    xpathID=driver.find_element_by_xpath('//*[@id="notion-email-input-1"]')
    xpathID.send_keys('yhb0113@gs.anyang.ac.kr')
    driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/section/div/div/div/div[2]/div[1]/div[3]/form/div[3]').click()
    time.sleep(1)
    xpathPW=driver.find_element_by_xpath('//*[@id="notion-password-input-2"]')
    xpathPW.send_keys('yjh2017E!')
    driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/section/div/div/div/div[2]/div[1]/div[3]/form/div[3]').click()
    '''
    
    #구글로 로그인 임시
    driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div').click()
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])

    #xpaathID=driver.find_element_by_id('identifierId')
    xpaathID=driver.find_element_by_xpath('//*[@id="identifierId"]')
    xpaathID.send_keys('yhb0113@gs.anyang.ac.kr')
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(1)
    xpathPW=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    time.sleep(1)
    xpathPW.send_keys('yjh2017E!!')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
   

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.notion.so/"+DBID)
    time.sleep(5)
    
    driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div[4]').click()
    driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div[2]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]').click()
    time.sleep(2)
    driver.quit()
    return 0
