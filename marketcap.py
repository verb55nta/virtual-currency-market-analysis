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
                if(b.get('class') is not None):
                    for c in b.get('class'): # c is class
                        if(re.match("currency-name",c)):
                            for c_name in b.select("a"):
                                if(c_name.get("class") is not None):
                                    currency_name.append(c_name.text)
                        elif(re.match("market-cap",c)):
                            market_cap.append(b.get('data-usd').strip())
                        elif(re.match("percent",c)):
                            change.append(b.get('data-usd').strip())
                        elif(re.match("circula",c)):
                            for temp_supply in b.select("a"):
                                if(temp_supply.get("data-supply") is not None):

                                    supply.append(temp_supply.get("data-supply"))
                for other in b.select("a"):
                    if(other.get("class") is not None):
                        for c2 in other.get('class'): # c is class                 
                            if(re.match("price",c2)):
                                price_usd.append(other.get('data-usd').strip())
                            elif(re.match("volume",c2)):
                                volume_usd.append(other.get('data-usd').strip())



for i in range(1,21,1):
    #print(i)
    base_url = 'https://coinmarketcap.com/'
    target_url = base_url + str(i)
    r = requests.get(target_url)
    tmp_soup = BeautifulSoup(r.text,'lxml')
    scraping(tmp_soup)

#print("debug")
#print(len(currency_name),len(price_usd),len(volume_usd),len(market_cap),len(change))

volatility={}

def is_float_str(num_str, default=0):
    try:
        return {"is_float": True ,"val": float(num_str)}
    except ValueError:
        return {"is_float": False , "val": default}

for i in range(0,len(currency_name),1):
    if( is_float_str(volume_usd[i])["is_float"] and is_float_str(market_cap[i])["is_float"] ):
        volatility[currency_name[i]]=(float(volume_usd[i]) / float(market_cap[i]))
    else:
        volatility[currency_name[i]]=0

num=0

for k,v in sorted( volatility.items(),key=lambda x:-x[1]  ):

    #if(float(market_cap[currency_name.index(k)]) < 1e8 ):
    if(v < 0.1): break
    if(float(market_cap[currency_name.index(k)]) < 1e7 ):    
        #print( str(currency_name.index(k)) + ":" + str( float(market_cap[currency_name.index(k)])  )  + ":" + str(k) + ":" + str(v)  )
        print( str(currency_name.index(k)) + "\t\t" + str( float(market_cap[currency_name.index(k)])  )  + "\t\t" + str(k) + "\t\t" + str(v)  )
        num+=1

#print("num:"+ str(num))
        
#print("currency_name[i],market_cap[i],price_usd[i],volume_usd[i],change[i]")
#print("currency_name[i],market_cap[i],price_usd[i],volume_usd[i]")

#for i in range(0,1000,1):
    #print(currency_name[i],market_cap[i],price_usd[i],volume_usd[i],change[i])
    #print(currency_name[i],",",market_cap[i],",",price_usd[i],",",volume_usd[i],",",change[i])
    #print(currency_name[i],",",market_cap[i],",",price_usd[i],",",volume_usd[i])
#print(len(supply))
