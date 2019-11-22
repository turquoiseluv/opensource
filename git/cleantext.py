from parameter import *
import re

# 제목 형식 정리 함수
def cleanName(readData):
   text = re.sub("\n|\t|\xa0", "", readData)
   text = text.replace("[일반 과제]", "")
   text = text.replace("[진행중]", "")
   text = text.replace("[진행예정]", "")
   text = text.replace("[마감]", "")
   text = text.strip()
   return text

# 날짜 형식 정리 함수
def cleanDate(readData):
   text = re.sub("\n|\t|\xa0", "", readData)
   text = text.replace("작성일 : ", "")
   text = text.strip()
   return text
