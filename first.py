hihim0hackingkr=int(input('봇 인지 확인, 7을 입력해 주십쇼.:'))
if hihim0hackingkr == 7 :
    print("해킹 진행합니다.")
    hihim0hackingkr2=int(input('해킹할 대상 수:'))
    print('공격 대상 설정 완료.')
    hihim0hackingkr3=int(input('해킹할 물량 수:'))
    if hihim0hackingkr3 < 10 :
        print("물량이 너무 부족합니다.")
    else :
        print("해킹 공격 진행중.....")
else :
    print("해킹 진행불가, 연결상태를 체크해 주십쇼.")
