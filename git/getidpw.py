from parameter import *

# 이러닝 자동 등록
def getidpw():
   global username, password
   if username != 0 and password != 0:
      print("\n사용자 '"+username+"'의 정보가 이미 존재합니다.")
      return

   username = input("\nDKU 학번을 입력하시오: ")
   password = input("비밀번호를 입력하시오: ")
   salt = bcrypt.gensalt()
   hashed = bcrypt.hashpw(password.encode('utf-8'),salt)
   cur.execute('insert into user(userId, userPw) values (%s, %s)', (username, hashed))
   conn.commit()
   # 이러닝 로그인
   driver.get('https://portal.dankook.ac.kr/web/portal')
   driver.find_element_by_class_name('id_input').send_keys(username)
   driver.find_element_by_class_name('pw_input').send_keys(password)
   #if hashed == bcrypt.hashpw(password.encode('utf-8'),salt)
   driver.find_element_by_class_name('btn_login').click()
   # 로그인 실패 확인
   if driver.current_url == 'https://webinfo.dankook.ac.kr/member/logon.do?returnurl=http%3A%2F%2Fportal.dankook.ac.kr%2Fsso%2Findex.jsp%3Freturnurl%3Dhttp%253A%252F%252Fportal.dankook.ac.kr%253A80%252Fweb%252Fportal&sso=ok':
      print("\n회원 아이디 또는 비밀번호가 일치하지 않습니다.")
      username = 0
      password = 0
      return
   print("\n사용자 '"+username+"'의 정보가 등록되었습니다.")
   return
