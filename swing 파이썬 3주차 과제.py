import urllib.request
from bs4 import BeautifulSoup

web=urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup=BeautifulSoup(web,'html.parser')
dep=soup.findAll("a") #학과 정보 추출 (<a>~~학과</a> 이 부분)

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과\t\t\t\t\t홈페이지")

for i in dep:
    if i.text=="자율전공학부" or i.text=="공동기기실" or "대학원" in i.text or "(*)" in i.text:
        continue #학과 외 기관 제외
    else:
        web=urllib.request.urlopen("http://www.swu.ac.kr" + i['href'])
        soup=BeautifulSoup(web, 'html.parser')
        link=soup.find("a",{"class","btn btn_xl btn_blue_gray"})

        if "홈페이지" in link.text:
            print(i.text + "\t\t\t\t" + link['href'])
        else:
            print(i.text + "\t\t\t\t" + "홈페이지가 존재하지 않음")
