from parameter import *

def getlms(username, password):
   if username == 0 or password == 0:
      print("\n등록된 유저가 없습니다.")
      return

   course_num = []
   course_name = []
   assignments = []
   materials = []
   notices = []

   ### 과목번호 및 과목명 추출
   driver.get('http://lms.dankook.ac.kr/index.jsp')
   driver.get('https://lms.dankook.ac.kr/Main.do?cmd=moveMenu&mainDTO.parentMenuId=menu_00026&mainDTO.menuId=menu_00031')
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')
   courses = soup.find("select",{"name":"courseDTO.courseId"})
   clist_inc = courses.findAll("option")
   clist = clist_inc[1:]
   for c in clist:
      save = c['value']
      num = re.findall("\d+",save)
      if len(num[0]) == 12:
         course_num.append(num[0])
         course_name.append(c.text[1:-2])
   ###

   for crs_num in range(len(course_num)):
      ## 해당 과목의 과제 탭 소제목과 제출 기간 조회
      driver.get('http://lms.dankook.ac.kr/Report.do?cmd=viewReportInfoPageList&boardInfoDTO.boardInfoGubun=report&courseDTO.courseId='+course_num[crs_num]+'&mainDTO.parentMenuId=menu_00104&mainDTO.menuId=menu_00063')
      html = driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      info = soup.findAll("div",{"class":"listContent pb20"})
      for a_info in info:
         a_name = a_info.find("dl", "element").dt.h4.text
         a_due = a_info.find("table", "boardListInfo").tbody.tr.td.text
         assignments.append(['과제', crs_num, cleanName(a_name), cleanDate(a_due)])
      # 스크래핑한 정보 리스트화
      printdb(assignments)
      # 저장 리스트 초기화
      del assignments[:]

   for crs_num in range(len(course_num)):
      ## 해당 과목의 자료실 탭 소제목과 업로드 날짜 조회
      driver.get('http://lms.dankook.ac.kr/Course.do?cmd=viewBoardContentsList&boardInfoDTO.boardInfoGubun=pds&boardInfoDTO.boardInfoId='+course_num[crs_num]+'-P&boardInfoDTO.boardClass=pds&boardInfoDTO.boardType=course&courseDTO.courseId='+course_num[crs_num]+'&mainDTO.parentMenuId=menu_00048&mainDTO.menuId=menu_00056')
      html = driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      info = soup.findAll("div",{"class":"listContent"})
      for a_info in info:
         a_name = a_info.find("dl", "element").dt.h4.a.text
         a_due = a_info.select("ul.fr.mr10 > li:nth-child(2)")[0].text
         materials.append(['자료', crs_num, cleanName(a_name), cleanDate(a_due)])
      ##
      # 스크래핑한 정보 리스트화
      printdb(materials)
      # 저장 리스트 초기화
      del materials[:]

   for crs_num in range(len(course_num)):
      ## 해당 과목의 공지사항 탭 소제목과 업로드 날짜 조회
      driver.get('http://lms.dankook.ac.kr/Course.do?cmd=viewBoardContentsList&boardInfoDTO.boardInfoGubun=notice&boardInfoDTO.boardInfoId='+course_num[crs_num]+'-N&boardInfoDTO.boardClass=notice&boardInfoDTO.boardType=course&courseDTO.courseId='+course_num[crs_num]+'&mainDTO.parentMenuId=menu_00048&mainDTO.menuId=menu_00056')
      html = driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      info = soup.findAll("div",{"class":"listContent"})
      for a_info in info:
         a_name = a_info.find("dl", "element").dt.h4.a.text
         a_due = a_info.select("ul.fr.mr10 > li:nth-child(2)")[0].text
         notices.append(['공지', crs_num, cleanName(a_name), cleanDate(a_due)])
      ##
      # 스크래핑한 정보 리스트화
      printdb(notices)
      # 저장 리스트 초기화
      del notices[:]
   return