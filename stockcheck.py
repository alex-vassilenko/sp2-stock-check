from BeautifulSoup import BeautifulSoup
import urllib2
import logging

# Check the Microsoft Store

sites = {'64': 'http://www.microsoftstore.com/store/msca/en_CA/html/pbPage.PDPS/productID.288933100',
		'128': 'http://www.microsoftstore.com/store/msca/en_CA/html/pbPage.PDPS/productID.288933200',
		'256': 'http://www.microsoftstore.com/store/msca/en_CA/html/pbPage.PDPS/productID.288933300',
		'512': 'http://www.microsoftstore.com/store/msca/en_CA/html/pbPage.PDPS/productID.288933400'}

def stockCheck():
	for size in sites:
		u = sites[size]
		try:
			page = urllib2.urlopen(u)
			soup = BeautifulSoup(page.read())
		except urllib2.URLError:
			from details import username, passw, proxy
			proxy_url = 'http://' + username + ':' + passw + '@' + proxy
			proxy_support = urllib2.ProxyHandler({"http":proxy_url})
			opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
			urllib2.install_opener(opener)
			
		page = urllib2.urlopen(u)
		soup = BeautifulSoup(page.read())
			
		if (soup.find(title = "Out of Stock") != None):	# Out of Stock button present
			print size + 'GB is out of stock!'
		else:
			print size + 'GB is in stock!'

stockCheck()
		
raw_input("Press any key to close.")