from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from os.path import join, dirname
#import cv2
#import numpy as np
#import pytesseract
#import re
import webbrowser
import json

import datetime
from datetime import date
from bs4 import BeautifulSoup
import requests
from coinmodels import Platform, GiftCard


net_url = "https://www.netflix.com/BillingActivity"
amz_url = "https://www.amazon.com/mc?_encoding=UTF8&ref_=nav_youraccount_prime"
spot_url = "https://www.spotify.com/us/account/overview/"



def getMemberLst(lst):

	empty = []

	for i in lst:

		b = i.text
		c = b.split()

		if b.count(" ") == 0:			
			empty.append(''.join(letter for letter in b.lower() if ('a' <= letter <= 'z' or letter == ' ') ).capitalize())
		else: 
			empty.append(' '.join(c))
	#print("****************************")
	#print(empty)

	return empty

def getSrcData(url): 
 
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument("--test-type")
	options.add_argument("user-data-dir=C:/Users/jkona/AppData/Local/Google/Chrome/User Data/Megame")
	#options.binary_location = "/usr/bin/chromium"
	driver = webdriver.Chrome("C:/megame/chromedriver.exe", chrome_options=options)

	driver.get(url)
	while not(url in driver.current_url):
	    print("Login!")

	page_source = driver.page_source

	driver.close()
	return page_source

net_pg = getSrcData(net_url)
net_soup = BeautifulSoup(net_pg, 'html.parser')
net_data = [item.get_text() for item in net_soup.find_all() if "data-uia" in item.attrs]
net_dt = net_data[7].replace(',','')
# netflix amount and date
net_amount = net_data[5].replace('Premium for ', '').replace('/month','')
net_date = datetime.datetime.strptime(net_dt, '%B %d %Y').strftime("%Y/%m/%d")
print("netflix amount = " + net_amount)

amz_pg = getSrcData(amz_url)
amz_soup = BeautifulSoup(amz_pg, 'html.parser')
amz_data = [item.get_text() for item in amz_soup.find_all('div', class_="mcx-menu-item__heading mcx-weight-lighter a-size-large")]
amz_dt = amz_data[1].replace(',','')
# amazon date and amount
amz_date = datetime.datetime.strptime(amz_dt, '%B %d %Y').strftime("%Y/%m/%d")
amz_amount = amz_data[0].replace('Annual ', '')
print("amazon amount = " + amz_amount)


spot_pg = getSrcData(spot_url)
spot_soup = BeautifulSoup(spot_pg, 'html.parser')
spot_dt = spot_soup.find('b', class_="recurring-date").get_text()
#spotify date and amount
spot_amount = spot_soup.find('b', class_="recurring-price").get_text()
spot_date = datetime.datetime.strptime(spot_dt, '%m/%d/%y').strftime("%Y/%m/%d")
print("spotify amount = " + spot_amount)


hulu_amount = spot_amount

platforms = []
x = Platform("Netflix", net_amount, net_date, net_url)
platforms.append(x)
y = Platform("Amazon", amz_amount, amz_date, amz_url)
platforms.append(y)
z = Platform("Spotify", spot_amount, spot_date, spot_url)
platforms.append(z)
mg_amt = "$200.00"
mg_date = "2019/11/10"
a = Platform("MoneyGrubbr", mg_amt, mg_date,"moneygrubbr.html")
platforms.append(a)


def createMessage():
	message="""
		<!DOCTYPE html>
		<html lang="en" class="no-js">
			<head>
				<meta charset="UTF-8" />
				<meta http-equiv="X-UA-Compatible" content="IE=edge"> 
				<meta name="viewport" content="width=device-width, initial-scale=1"> 
				<title>CoinHero!</title>
				<meta name="description" content="Page Preloading Effect: Re-creating the effect seen on fontface.ninja" />
				<meta name="keywords" content="page loading, effect, initial, logo, sliding, web design, css animation, transform" />
				<meta name="author" content="Codrops" />
				<link rel="shortcut icon" href="../favicon.ico">
				<link rel="stylesheet" type="text/css" href="css/normalize.css" />
				<link rel="stylesheet" type="text/css" href="css/demo.css" />
				<link rel="stylesheet" type="text/css" href="css/effect1.css" />
				<script src="js/modernizr.custom.js"></script>
			</head>
			<body class="demo-1">
				<div id="ip-container" class="ip-container">
					<!-- initial header -->
					<header class="ip-header">
						<h1 class="ip-logo">
							<img src="img/coinherologo.gif" style="margin:0 auto;"/>
						</h1>
						<div class="ip-loader">
							<svg class="ip-inner" width="60px" height="60px" viewBox="0 0 80 80">
								<path class="ip-loader-circlebg" d="M40,10C57.351,10,71,23.649,71,40.5S57.351,71,40.5,71 S10,57.351,10,40.5S23.649,10,40.5,10z"/>
								<path id="ip-loader-circle" class="ip-loader-circle" d="M40,10C57.351,10,71,23.649,71,40.5S57.351,71,40.5,71 S10,57.351,10,40.5S23.649,10,40.5,10z"/>
							</svg>
						</div>
					</header>
					<!-- top bar -->
					<!-- main content -->
					<div class="ip-main">
						<nav class="codrops-demos">
							<a class="current-demo" href="index.html">Demo 1</a>
							<a href="index2.html">Demo 2</a>
						</nav>
						<h2 style="text-align: center">Get to your bank account before your subscriptions do!</h2>
						<h3 style="text-align: center;"> A project by Janice Konadu &amp; Cristian Teran</h3> 
						<div class="browser clearfix">"""
	for i in platforms:

		message += """
		<div class="card" style="border-radius: 20px; margin-bottom: 15px; background-color: #5c0379; padding-left:25px"">
			<h2 style="font-size: 34pt; color:#ad3ad2; text-align: left; letter-spacing: 3px; text-transform:uppercase; ">"""
		message += i.name + "</br>" + i.amount + "</br>" + i.getDate()

		message+="""</h3></div>"""

		message +=""" """

	message +="""
								<h3 style=""></h3>
							</div>
						</div>
					</div>
				</div><!-- /container -->
				<script src="js/classie.js"></script>
				<script src="js/pathLoader.js"></script>
				<script src="js/main.js"></script>
			</body>
		</html>



	"""

	return message

f = open('coinhero.html','w')

message = createMessage()
# print (message)
f.write(message)
f.close()

filename = 'C:/Users/jkona/Desktop/projects/megame-master/megame/coinhero/' + 'coinhero.html'
webbrowser.open_new_tab(filename)


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("user-data-dir=C:/Users/jkona/AppData/Local/Google/Chrome/User Data/Megame")
#options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome("C:/megame/chromedriver.exe", chrome_options=options)

driver.get("https://www.spotify.com/us/account/subscription/")

link = driver.find_element_by_xpath("//*[@id=\"btn-cta-subscription-card\"]")
link.click()
#xpath = ""

delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'cardnumber')))
    print ("Page is ready!")

except TimeoutException:
    print ("Loading took too much time!")
