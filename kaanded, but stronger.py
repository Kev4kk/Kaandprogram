import os

try:#vajadusel installib moodulid
  import requests
except ImportError:
  print("Hakkan laadima moodulit: requests\n")
  os.system('python -m pip install requests')
from urllib.request import urlopen

try:
  import bs4
except ImportError:
  print("Hakkan laadima moodulit: bs4\n")
  os.system('python -m pip install beautifulsoup4')
from bs4 import BeautifulSoup


def OnInt(vaadeldav):
    try:
        int(vaadeldav)
    except ValueError:
        return False
    return True

sone = input("Mis sõna otsida?: ")
link = "https://www.eki.ee/dict/qs/index.cgi?Q="+sone+"&F=M"
html = urlopen(link)
soup = BeautifulSoup(html, "lxml")

AAd = soup.find_all("a")
print(AAd)
num = ""
i = 1
tyybid=[]
while i < int(len(AAd)+1):
    tyyp = AAd[0-i]
    for content in tyyp:
        num+=str(content)
    print(num)
    if OnInt(num) == True and int(num) < 40:
        tyybid.append(int(num))
    i+= 1
    num = ""    
print("Tüüpnumbrid on:", tyybid, "\n\n\n\n\n")

spanstr = ""
span = soup.find_all("span")
for j in range(0, len(span)):
    osa = span[j]
    for sisu in osa:
      spanstr += str(sisu)
    print(spanstr)
    spanstr = ""
for t in range()

