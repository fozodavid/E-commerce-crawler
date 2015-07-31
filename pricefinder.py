"""
This program fetches the first 'supposed to be most relevant' price from a given product search on Ebay and Amazon
After start it asks the user for input. Then it shows how much it costs in either Amazon and Ebay. At the end evaluates
which price is cheaper.
"""

from lxml import html							#importing modules
import requests

def findprice(url,xpathstr,search):				#the function returns the one and most relevant price (the first of the list)
	site = requests.get(url)					#opens url
	sitetree = html.fromstring(site.text)		#converts into xpath accessible format
	siteprices = list(map(str.strip,(sitetree.xpath(xpathstr))))		#with a given xpath query,it returns all relevant text into a list
																		#then the map function eliminates all whitespace
	return [x for x in siteprices if '.' in x][0]						#filters the list; only items contains a dot remains(easier than pound sign)

if __name__ == '__main__':
	raw_search = input('What product are you looking for?')
	search = raw_search.replace(' ','+')								#for the url all spaces need to be replaced to '+'

	ebayurl = 'http://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={0}&_sacat=0'.format(search)	#url; the search is popped into
	amazonurl = 'http://www.amazon.co.uk/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords={0}&rh=i%3Aaps%2Ck%3A{0}'.format(search)

	ebayxpath = '//span[@class="bold"]/text()' # xpath query
	amazonxpath = '//div[@id="resultsCol"]//span/text()'

	ebayprice = findprice(ebayurl,ebayxpath,search) # request prices
	amazonprice = findprice(amazonurl,amazonxpath,search)

	print('\nPrice of:', raw_search,'\n')
	print('Ebay:  ',ebayprice)
	print('Amazon:',amazonprice)

	if float(ebayprice[1:]) > float(amazonprice[1:]):
		print("\nThis product is cheaper on Amazon.")
	else:
		print("\nThis product is cheaper on Ebay.")