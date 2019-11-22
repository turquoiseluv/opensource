from parameter import *

# 사용자 입력
def getuser(username):
   u_sort = input("분류: ")
   u_content = input("내용: ")
   u_date = input("기한: ")
   u_class = input("과목: ")

   u_save = ["개인", u_sort, username, "학과", u_class, u_content, u_date]
   sch(u_save)
   return
