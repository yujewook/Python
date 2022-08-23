#네이버 환율정보
import urllib.request as req
from bs4 import BeautifulSoup as bs
# url = "https://finance.naver.com/marketindex/exchangeList.naver"
# #데이터 받아오기
# data = req.urlopen(url).read().decode("euc-kr")
# #데이터 저장하기
# req.urlretrieve(url, "exchangeList.txt")
#
# #짤라오기
# soup = bs(data,"html.parser")
#             #여러개 갖고오기 tit class에 갖고 있는 것 <td> 안에 <a> 태그
# exchange = soup.select(".tit a") #리스트로 갖고온다 select
# # td에 sale이라는 클래스
# sale = soup.select("td.sale")   #리스트로 갖고온다 select
#
# # for e in exchange : #strip 여백지워 주기
# #     print(e.string.strip())
#
# for i in range(len(exchange)) :
#         # a태그 하나 
#     print(exchange[i].string.strip(), "\t",sale[i].string.strip()
#           , sale[i].next_sibling.next_sibling.string.strip() )
#


import time
#다음 실시간뉴스
# url = "https://news.daum.net/"
# data = req.urlopen(url).read().decode("utf-8")
# soup = bs(data,"html.parser")
# #변수
# titles = soup.select("strong.tit_g a")
# #데이터와 인덱스 같이 나온다
# for i, title in enumerate(titles):
#     if i > 4:
#         break
#     print("<<"+title.string.strip()+">>" )
#     time.sleep(1)
#                     #title안 <a>태그안 href속성을 꺼내기 위해
#     article_url = title.attrs["href"]
#     #print(article_url)
#     #주소안에 들어가서 데이터를 갖고 읽어와라
#     article_data = req.urlopen(article_url).read().decode("utf-8")
#     #print (article_data)
#
#     #article_data에 있는 데이터를 다시 parser해줘라 기사 내용을 갖고오게 하기 위해서 
#     soup = bs(article_data,"html.parser")
#                                         # 바로 자식 컨테이너의 p 테그
#     ps = soup.select("div#harmonyContainer section >p")
#
#     for p in ps:
#         if p.string != None:
#             print(p.string)
#     time.sleep(3)

## requests
import requests
#request는 get이라는 함수를 사용한다. setter / getter가 아니라 servlet doget [dopost] 방식을 의미한다.
# text 는 text , 바이너리는 wb
# req = requests.get("http://www.goolge.co.kr/robots.txt")
# #데이터를 갖고오기 쉽다.
# text = req.text
# #print(text)
# #바이너리 형식으로 만들기 .content 함수를 사용해야한다
# #bin = req.content
# print(bin)
# #이미지 갖고오기 
# requests.get("https://img3.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202208/22/joongang/20220822094309182vvxf.jpg")
# #이미지 파일저장하기
# with open("test.jpg","wb") as f:
#     # 바이너리이기 때문에 content
#     f.write(req.content)
    
    
#한빛미디어 로그인 해서 데이터 얻어오기
#처리하는 페이지 #로그인을 처리를 pro 에서 한다 
# url = "https://www.hanbit.co.kr/member/login_proc.php" 
# #주소에다 id랑 passwd 줘도 되지만 변경하기 편하게 하기 위해서 변수 설정
# login_info={
#     "m_id":"filmal",
#     "m_passwd":"abcd1234"
#     }
# #접속을 하면 session이 생긴다 그 session이라고하는것 jsp session이 아니다
# session=requests.session()
# #접속하기위해
# con = session.post(url,login_info)
# #접속해서 상태유지를 하기 위해서
# con.raise_for_status()
#
#
# #마이페이지 주소    
# url="https://www.hanbit.co.kr/myhanbit/myhanbit.html"    
# #데이터 받아오기
# data = session.get(url)
# #데이터를 받아오고 유지하고,
# data.raise_for_status()
# #데이터를 뭐로 읽을꺼냐 바이너리 or text -> 여기서는 text 데이터 파싱하기위해
# soup = bs(data.text , "html.parser")
#
# mileage_title = soup.select_one("dl.mileage_section1 dt")
# milage = soup.select_one("dl.mileage_section1 dd span")
# print(mileage_title.string , ":" , milage.string)
#
#
# ecoin_title = soup.select_one("dl.mileage_section2 dt")
# ecoin = soup.select_one("dl.milage_section2 span")
# print(ecoin_title ,":", ecoin)
# #여러개 데이터
# trs = soup.select("div.sm_myorder tr")
# #print(trs)
# # 두번째 tr 부터 가라
# for i in range(1 ,len(trs)) : 
#     #tr 안에 td를 문자열로 바꿔서 
#     print(trs[i].td.string,"\t",trs[i].a.string,"\t",trs[i].span.string)
#


#셀레늄 selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#
# #Chromeoptino()은 클래스이다.
# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install() ),
#                           options=chrome_options )
# url = "http://naver.com"
# driver.get(url)
# time.sleep(5)
# driver.save_screenshot("naver.png")
# driver.quit()


# 구글로그인                        
from webdriver_manager.core.utils import ChromeType
#                                생성자로 준다
# driver = webdriver.Chrome( service = Service( ChromeDriverManager(chrome_type = ChromeType.BRAVE).install() ) )
#
# url = "https://accounts.google.com/signin/v2/identifier"
# #3초 기다려라
# driver.implicitly_wait(3)
# driver.get(url)
#
# #로그인 하는것
# driver.find_element("id","identifierId").send_keys("instructor.set")
# idbutton = driver.find_element("id","identifierNext")
# time.sleep(2)
# idbutton.click()
# time.sleep(5)

#한빛 미디어 로그인
# url = "https://www.hanbit.co.kr/member/login.html"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type= ChromeType.BRAVE).install() ) )
# driver.implicitly_wait(3)
# driver.get(url)
# driver.find_element("id","m_id").send_keys("filmal")
# driver.find_element("id","m_passwd").send_keys("abcd1234")
# time.sleep(2)
#
# loginbutton = driver.find_element("id","login_btn")
# loginbutton.click()
#
# time.sleep(5)
#마일리지 하고 싶으면 위에 했던거 그대로 하면 됨.

#공공데이터 포털 - 국토교통부_아파트매매 실거래 상세 정보
import urllib.request as req
import urllib.parse as pa#url 간단하게 변경하기위한 것 
url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=41135&DEAL_YMD=202207&serviceKey=OUwSlot%2BeCADq1M9zzdj8Sh1Ni9C4Iiaj9VqSEnyvikodjynkoS1hrbUsP6mSENccvTJH%2FDe3s3y7i836Lk7ew%3D%3D"

#url 간단하게 변경하기위한 것 
# url="http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?"
# values={
#     "LAWD_CD" : 11545,
#     "DEAL_YMD": 202207,
#     "serviceey":"OUwSlot%2BeCADq1M9zzdj8Sh1Ni9C4Iiaj9VqSEnyvikodjynkoS1hrbUsP6mSENccvTJH%2FDe3s3y7i836Lk7ew%3D%3D"
#     }
# params = pa.urlencode(values)
# url = url + "?" + params
# 
data=req.urlopen(url).read().decode("utf-8")

#print(data)

#파일로 만들어서 저장
with open("apar202207.txt","w" , encoding="utf-8") as f :
    f.write(data)
#beautiful soup는 영어만 된다
data = data.replace("거래금액","price")
data = data.replace("법정동","dong")
data = data.replace("아파트","apartname")
data = data.replace("월","month")
data = data.replace("일","day")

soup = bs(data,"html.parser")
items = soup.select("item")
for item in items :
    #print(item)
    #dong     그옆에 정보 
    print(item.dong.string , item.month.string, "-",item.day.string,
          item.apartname.string,item.price.string)

















