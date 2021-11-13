import os
import urllib.request
from bs4 import BeautifulSoup

web=urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=732988&weekday=tue') #웹툰 링크 접근
soup=BeautifulSoup(web,'html.parser')

title=soup.head.title.text #웹툰 제목 가져오기
title=title.replace(" :: 네이버 만화","") #실질적 웹툰 제목 부분만 저장하기

os.mkdir(title) #웹툰 제목 폴더 생성
os.chdir(title) #웹툰 제목 폴더로 작업 디렉토리 변경

opener=urllib.request.build_opener() #오프너 객체 생성으로 헤더 추가
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')]
urllib.request.install_opener(opener)

episode=soup.findAll("td",{"class","title"}) #회차 제목 가져오기

for i in episode:
    ep=i.text.replace("\n","") #회차 제목 저장
    os.mkdir(ep) #회차 제목 폴더 생성
    os.chdir(ep) #회차 제목 폴더로 작업 디렉토리 변경

    url=urllib.request.urlopen('https://comic.naver.com'+i.a['href']) #회차별 링크 접근
    soup2=BeautifulSoup(url,'html.parser')

    image=soup2.find("div",{"class","wt_viewer"}).findAll("img") #이미지 접근
    img=1 #이미지 저장할 이름

    for j in image:
        urllib.request.urlretrieve(j['src'],"./"+str(img)+".jpg") #이미지 저장
        img=img+1

    print(ep+" 완료") #회차별 끝나면 회차이름+완료 실행창에 출력
    os.chdir("..") #한 회차 작업 끝나면 상위 디렉토리로 이동(=웹툰 제목인 폴더로)
