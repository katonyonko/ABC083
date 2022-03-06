from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="083"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc088_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  S=input()
  N=len(S)
  if N%2==0:
    ans=N//2
    t=S[N//2]
    l,r=N//2-1,N//2
    while l>=0 and S[l]==S[r]==t:
      ans+=1
      l-=1; r+=1
  else:
    ans=(N+1)//2
    t=S[N//2]
    l,r=N//2-1,N//2+1
    while l>=0 and S[l]==S[r]==t:
      ans+=1
      l-=1; r+=1
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])