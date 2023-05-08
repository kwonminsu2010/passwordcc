print("안녕하세요..")
print('권호연의 파이썬 해킹 툴입니다.')
print('설명서를 보시고 시작해주세요.')


text=input('공격 대상 입력하기 : ')
print('공격대상은' ,text, '입니다.')
print('해킹 진행중... SYN FLOOD 공격에 맞게 vpn을 준비해주세요.')

if text.isupper() :
    print("공격대상을 소문자로 입력해주세요.")
else :
    print('동작 실패, 인터넷 연결을 확인해주세요.')