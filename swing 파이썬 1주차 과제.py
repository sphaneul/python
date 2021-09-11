import random #답이 될 수를 정해줄 랜덤 모듈

answer=random.randint(1,100) #답 변수 랜덤 저장
num=1       # 시도 횟수
besttry=10  # 최고 기록
first=1     # 가능한 최소값
last=100    # 가능한 최대값
gamenum=0   # 게임 횟수
scoreboard=[] # 게임 기록

while True: #게임 메뉴 선택은 3번 선택하기 전에는 계속 반복되게 while로 설정
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    menu=int(input(">>")) #메뉴 선택
    if menu==1: # 1번 메뉴 선택시
        gamenum=gamenum+1 # 게임 횟수(맞추는 횟수x 전체 게임 플레이 횟수임)-기록확인에 필요
        while num < 11: #총 10번 이내
            print(num,"번째 숫자 입력(",first,"~",last,") :" ,end=' ')
            quiz=int(input()) #시도한 답
            if quiz==answer: #맞았을 때
                print("정답입니다!!")
                print(num,"번째만에 맞추셨습니다")
                scoreboard.append("%d %d" %(gamenum, num)) #현재 게임횟수 시도횟수 형식으로 scoreboard 리스트에 원소 추가
                if num<besttry: #최고기록 달성했을 때
                    print("최고기록 갱신~!")
                    besttry=num
                num=1 #초기화 진행
                first=1
                last=100
                break #다시 메뉴로 나가기
            elif quiz>answer: # 시도한 답이 정답보다 클 때
                print("DOWN")
                num=num+1 #시도횟수+1
                last=quiz-1 #최대값 범위 조정
            else: # 시도한 답이 정답보다 작을 때
                print("UP")
                num=num+1 #시도횟수+1
                first=quiz+1 #최소값 범위 조정

        if num==11: #10번 이내에 맞추지 못했을 때
            print("실패!")
            num=1 #초기화 진행
            first=1
            last=100
            scoreboard.append("%d 실패" %(gamenum)) #점수판에 실패로 기록
    elif menu==2: #2번 메뉴 선택시
        show=""
        for i in scoreboard:
            show=show+i+"\n" #띄어쓰기 형식으로 볼 수 있게 show에 저장
        print(show) #show 출력
    elif menu==3: #3번 메뉴 선택시
        break #종료
    else: #1~3말고 다른 메뉴를 눌렀을 때
        print("1~3까지만 선택해주세요")
    
