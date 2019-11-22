from parameter import *

# 사용자 입력 저장
def sch(save):
   cur.execute('insert into schedule(type, sort, userId, userMaj, crsNum, contents, deadline) values (%s, %s, %s, %s, %s, %s, %s)', save)
   conn.commit()
   return

# DB 표준 출력
def printdb(save):
   # DB 생성
   for i in range(len(save)):
      if save[i][0] == '과제':
         cur.execute('insert into assignment(type, crsName, contents, deadline) values (%s, %s, %s, %s)', save[i])
      elif save[i][0] =='공지':
         cur.execute('insert into notice(type, crsName, contents, deadline) values (%s, %s, %s, %s)', save[i])
      elif save[i][0]   =='자료':
         cur.execute('insert into material(type, crsName, contents, deadline) values (%s, %s, %s, %s)', save[i])
   conn.commit()
   # DB 종료
   return