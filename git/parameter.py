from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pymysql as s
import datetime
import bcrypt

d=datetime.datetime.now()
username = 0
password = 0
x = 0


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome('chromedriver', options=options)


conn = s.connect(
    host="172.31.38.135",
    user="root",
    passwd="123456",
    database="todo"
)
cur = conn.cursor()