import requests
from bs4 import BeautifulSoup

r =requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup=BeautifulSoup(r.text,'html.parser')##html.parser is in python. Beautiful soup is parsing text to obtain data nad putting it in soup.

results=soup.find_all('span',attrs={'class':'short-desc'})## this line is searching soup object for all span tags with attribute class=short-desc.
                                                          ##It will return the result set which will act like a list

firstresult=results[0]##this is not a string but a tag. a abeautiful soup object

#print(firstresult.find('strong').text[0:-1]+',2017')

record=[]
for result in results:
    date=result.find('strong').text[0:-1]
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    record.append((date,lie,explanation,url))
    
import pandas as pd

df=pd.DataFrame(record,columns=['date','lie','explanation','url'])
#df.head() #df.tail()
df.to_csv('Lies.csv',index=False,encoding='utf-8')
print("I know your lies")
