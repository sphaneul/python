import os.path
import random #답이 될 수를 정해줄 랜덤 모듈
from datetime import date

num=1       # 시도 횟수
besttry=10  # 최고 기록
first=1     # 가능한 최소값
last=100    # 가능한 최대값
scoreboard=[] # 게임 기록 불러오기

file='./scoreboard.txt'

if os.path.isfile(file): #파일 있을 때
    f=open('./scoreboard.txt','r')
    while True:
        line=f.readline()
        if not line : break
        scoreboard.append(line.strip('\n'))
    f.close()
    if len(scoreboard)!=0:
        temp=scoreboard[0]
        besttry=int(temp[0:2]) #파일 속 최고기록 불러오기(이것 때문에 출력 이상하게 되었음)
elif os.path.exists(file)==False: #파일 없을 때 생성
    f=open('./scoreboard.txt','w')
    f.close()

nickname="" #닉네임 변수 선언

while True: #게임 메뉴 선택은 3번 선택하기 전에는 계속 반복되게 while로 설정
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    menu=int(input(">>")) #메뉴 선택
    if menu==1: # 1번 메뉴 선택시
        answer=random.randint(1,100) #답 변수 랜덤 저장
        while num < 11: #총 10번 이내
            print(num,"번째 숫자 입력(",first,"~",last,") :" ,end=' ')
            quiz=int(input())
            
            while first>quiz or last<quiz:
                print("다시 입력해주세요")
                quiz=int(input())
                
            try: #try~except문 사용
                first>quiz or last<quiz
            except:
                print("error")
                
            else:
                
                if quiz==answer: #맞았을 때
                    print("정답입니다!!")
                    print(num,"번째만에 맞추셨습니다")
                    if num<besttry: #최고기록 달성했을 때
                        print("최고기록 갱신~!")
                        besttry=num
                        nickname=str(input())
                        today=date.today()
                        scoreboard.insert(0,"%d %s %s" %(num, nickname, today.isoformat())) #최고기록 달성시 게임기록(1위일 테니까 0번째 자리에) #4번 피드백 반영(1)
                        
                    num=1 #초기화 진행
                    first=1
                    last=100
                    break #다시 메뉴로 나가기
                elif quiz>answer: # 시도한 답이 정답보다 클 때
                    print("DOWN")
                    num=num+1 #시도횟수+1
                    if last>quiz:
                        last=quiz-1 #최대값 범위 조정
                elif quiz<answer: # 시도한 답이 정답보다 작을 때
                    print("UP")
                    num=num+1 #시도횟수+1
                    if first<quiz:
                        first=quiz+1 #최소값 범위 조정


            if num==11: #10번 이내에 맞추지 못했을 때
                print("실패!")
                num=1 #초기화 진행
                first=1
                last=100
                break
            
    elif menu==2: #2번 메뉴 선택시
        rank=1
        for i in scoreboard:
            print("%d %s" %(rank,i))
            rank=rank+1
    elif menu==3: #3번 메뉴 선택시
        with open('scoreboard.txt','w') as f:
            for i in scoreboard:
                f.write(i+"\n")
        break #종료
    else: #1~3말고 다른 메뉴를 눌렀을 때
        print("1~3까지만 선택해주세요")
    
