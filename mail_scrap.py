from bs4 import BeautifulSoup
import requests

import re

url = "https://snsce.ac.in"
req=requests.get(url)
print(req)
soup=BeautifulSoup(req.text,"html.parser")
res=(soup.get_text())


pat=re.compile("[a-z.A-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]+")
result=pat.findall(res)
print(result)
