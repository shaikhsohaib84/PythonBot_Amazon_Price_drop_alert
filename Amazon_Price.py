import requests #pip install requests bs4
from bs4 import BeautifulSoup #Implementing Web Scraping in Python with BeautifulSoup
import smtplib
#slack,suppervisord,sqllite
#way2sms,
URL = 'https://www.amazon.in/Samsung-Galaxy-Charcoal-Black-Storage/dp/B07HGKHV8Y?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_EAIaIQobChMIz7ey6Pzz5AIVVByPCh311AExEAQYAiABEgLqa_D_BwE_k_&gclid=EAIaIQobChMIz7ey6Pzz5AIVVByPCh311AExEAQYAiABEgLqa_D_BwE' 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}#info abt browser

def chk_price():
        page = requests.get(URL,headers=headers)

        soup = BeautifulSoup(page.content,'html.parser') 

        title = soup.find(id="productTitle").get_text()#getting info of product/item from web page

        price = soup.find(id="priceblock_dealprice").get_text()#getting info of product/item price from web page

        converted_price = (price[1:4])

        if (converted_price > "10000.00"):
            send_mail()
            print(converted_price)
            print(title.strip()) #strip is use to remove blank spaceses

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()#command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. ... The EHLO command tells the receiving server it supports extensions compatible with ESMTP.
    server.starttls()
    server.ehlo()

    server.login('shaikhsohaib84@gmail.com','Zebion@007')

    sub = 'mail from python .....u have won lottery..'

    body = 'chk this amazon link https://www.amazon.in/Samsung-Galaxy-Charcoal-Black-Storage/dp/B07HGKHV8Y?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_EAIaIQobChMIz7ey6Pzz5AIVVByPCh311AExEAQYAiABEgLqa_D_BwE_k_&gclid=EAIaIQobChMIz7ey6Pzz5AIVVByPCh311AExEAQYAiABEgLqa_D_BwE'

    msg = f"subject:{sub}\n\n{body}"

    server.sendmail(
        'shaikhsohaib84@gmail.com',
        'shaikhsohaib84@gmail.com',
        msg
    )

    print("sohaib  ..mail has been send")

chk_price()