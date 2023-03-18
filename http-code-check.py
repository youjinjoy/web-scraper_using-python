# 웹사이트 서버 상태 확인하여 딕셔너리로 출력하는 프로그램

import requests
from requests import get
"""
- pypi에서 requests 패키지 설치
- request 예시: 내 브라우저는 google 서버에 request를 보내고 google 서버는 나한테 웹사이트를 보내준다.
- get: webstie를 가져오는 기능
"""

websites=(
"google.com",
"airbnb.com",
"https://twitter.com",
"facebook.com",
"https://tiktok.com"
)
#코드는 http 또는 https에 ://를 붙인 웹사이트로 주소로만 이동이 가능하다.

results=dict()

for website in websites:
  if not website.startswith('https://'):
    website=f'https://{website}'
  response=get(website)

  """
  <Response [200]>이란 웹사이트가 성공적으로 응답했다는 뜻.
  인터넷은 HTTP protocol에 기반한다. 그래서 컴퓨터들이 서로 소통하는 방식은 당연하게도 HTTP request이다.
  request가 정상인지 아닌지 결과를 알 수 있는 수단으로 HTTP 코드를 사용한다.
  (HTTP code mdn 검색)
  """


  #상태 코드에 따른 경우의 수
  if response.status_code>=100 and response.status_code<200:
    results[website]='INFORMATION'
  elif response.status_code>=200 and response.status_code<300:
    results[website]='SUCCESS'
  elif response.status_code>=300 and response.status_code<400:
    results[website]='RE-DIRECTION'
  elif response.status_code>=400 and response.status_code<500:
    results[website]='CLIENT-ERROR'
  elif response.status_code>=500 and response.status_code<600:
    results[website]='SERVER-ERROR'
  else:
    results[website]='UNKNOWN-ERROR'

print(results)
