#셀레니움 라이브러리
from asyncio.windows_events import NULL
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#윈도우 cmd 라이브러리
import os
from tkinter import filedialog
import tkinter
import threading
from urllib import parse

#안양대 영상 다운 버튼 UI
import anyangvideo

OkUiObj=NULL


#크롬 디버깅 모드로 실행
def chrome_using():
    
    root=tkinter.Tk()
    root.withdraw()
    
    os.chdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
    os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeTest"')

def anyang_url():
    
    #크롬디버깅 모드 멀티스레드
    tread1= threading.Thread(target=chrome_using)
    tread1.start()

    time.sleep(1)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    #안양대 사이버 강의실 접속
    global driver
    driver = webdriver.Chrome(r"C:\Users\xctkt\Desktop\파이썬 프로젝트\22.10.21\module\anyang_video\chromedriver.exe", options= chrome_options)
    driver.get('https://cyber.anyang.ac.kr')

    # 여기서 멈춰서 동영상 값을 받아오고 아래 부분이 실행되면 됨

def anyang_down():
    #강의 보기 new 탭 핸들 선택
    driver.switch_to.window(driver.window_handles[1])

    #new 탭의 iframe 선택
    element = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(element)
    url = driver.find_element_by_tag_name('video').get_attribute("src") #video scr 추출 

    #새로 실행되는 창 닫기
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    print('--------------------------------------')
    print('\n\n추출된강의 영상 URL: '+url)

    #url 영상이름 지정
    file_name=url.split('/')
    
    fine_name=parse.unquote(file_name[len(file_name)-1]) #url ASCII 디코딩
    print('\n\n 다운로드 중... ▶다운로드되는 파일명: '+fine_name)

    os.chdir(os.path.dirname(os.path.realpath(__file__))) #현재 파이썬 실행중인 디렉토리로 경로 지정
    os.chdir('..\..\\')
    response = requests.get(url)           
    with open(fine_name, 'wb') as f:
        f.write(response.content)
    print("다운로드 완료")
    driver.quit()
    
    return fine_name
