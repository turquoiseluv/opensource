from parameter import *
from cleantext import *
from getuser import *
from getidpw import *
from webcrawling import *
from dbedit import *

global username, password

# 시작 메뉴
while(x != '3'):
   print("\n0. 사용자 정보 등록")
   print("1. 개인 일정 입력")
   print("2. 이러닝 자동 검색")
   print("3. 프로그램 종료")
   x = input("(0 ~ 3) 메뉴를 선택하시오: ")

   if x == '0':
      getidpw()
   elif x == '1':
      getuser(username, password)
   elif x == '2':
      getlms()
   elif x == '3':
      driver.quit()
   else:
      print("\n해당 메뉴가 없습니다.")
