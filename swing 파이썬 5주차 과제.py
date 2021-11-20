from selenium import webdriver
import time

path = "C:\chromedriver.exe" # 크롬드라이버가 저장된 경로
driver = webdriver.Chrome(path) # 웹드라이버 경로 지정
driver.get("http://zzzscore.com/1to50/") # 게임창 접속
button=driver.find_elements_by_xpath("//*[@id='grid']/div[*]") # button에 버튼들 정보 저장

for i in range (1, 51): # 총 50번 클릭
    for j in button: # 버튼(div)의 개수는 25개
        if j.text == str(i): # div가 i와 같을 경우 버튼 클릭
            j.click()
            print(str(i) + " 클릭") # n번 클릭 출력
