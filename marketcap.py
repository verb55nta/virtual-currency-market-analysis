import requests
from bs4 import BeautifulSoup
import re

currency_name=[]
price_usd=[]
volume_usd=[]
market_cap=[]
change=[]
supply=[]



def scraping(soup):

    for a in soup.find_all('tr'):
        if(a.get('id') is not None):
            for b in a.find_all('td'):
                #print(b)
                if(b.get('class') is not None):
                    for c in b.get('class'): # c is class
                        #print(c)
                        if(re.match("currency-name",c)):
                            for c_name in b.select("a"):
                                #print(c_name)
                                if(c_name.get("class") is not None):
                                    #print(c_name.text) # currency name
                                    currency_name.append(c_name.text)
                        elif(re.match("market-cap",c)):
                            #print(b.get('data-usd').strip()) #market capacity
                            market_cap.append(b.get('data-usd').strip())
                        elif(re.match("percent",c)):
                            #print(b.get('data-usd').strip()) # 24 h percent
                            change.append(b.get('data-usd').strip())
                        elif(re.match("circula",c)):
                            for temp_supply in b.select("a"):
                                if(temp_supply.get("data-supply") is not None):
                                    #print(temp_supply.get("data-supply")) #currency supply
                                    supply.append(temp_supply.get("data-supply"))
                                #if(c_name.get("class") is not None):
                for other in b.select("a"):
                    #print(other)
                    if(other.get("class") is not None):
                        for c2 in other.get('class'): # c is class                 
                            if(re.match("price",c2)):
                                #print(other.get('data-usd').strip()) #price
                                price_usd.append(other.get('data-usd').strip())
                            elif(re.match("volume",c2)):
                                #print(other.get('data-usd').strip()) #volume
                                volume_usd.append(other.get('data-usd').strip())
                    #if(re.match("price",other.get("class"))):


for i in range(1,11,1):
    #print(i)
    base_url = 'https://coinmarketcap.com/'
    target_url = base_url + str(i)
    r = requests.get(target_url)
    tmp_soup = BeautifulSoup(r.text,'lxml')
    scraping(tmp_soup)

#print(len(currency_name))
#print(len(price_usd))
#print(len(volume_usd))
#print(len(market_cap))
#print(len(change))

#print("currency_name[i],market_cap[i],price_usd[i],volume_usd[i],change[i]")
print("currency_name[i],market_cap[i],price_usd[i],volume_usd[i]")

for i in range(0,1000,1):
    #print(currency_name[i],market_cap[i],price_usd[i],volume_usd[i],change[i])
    #print(currency_name[i],",",market_cap[i],",",price_usd[i],",",volume_usd[i],",",change[i])
    print(currency_name[i],",",market_cap[i],",",price_usd[i],",",volume_usd[i])
#print(len(supply))
