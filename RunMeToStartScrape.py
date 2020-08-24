import sys

print('Mulai scraping website Badung...')
try:
	import ScrapeBadung
except:
	print('Error occurred in scraping Badung website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeBadung
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Bali...')
try:
	import ScrapeBali
except:
	print('Error occurred in scraping Bali website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeBali
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Buleleng...')
try:
	import ScrapeBuleleng
except:
	print('Error occurred in scraping Buleleng website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeBuleleng
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Denpasar...')
try:
	import ScrapeDenpasar
except:
	print('Error occurred in scraping Denpasar website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeDenpasar
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Gianyar...')
try:
	import ScrapeGianyar
except:
	print('Error occurred in scraping Gianyar website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeGianyar
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Tabanan...')
try:
	import ScrapeTabanan
except:
	print('Error occurred in scraping Tabanan website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeTabanan
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Karangasem')
try:
	import ScrapeKarangasem
except:
	print('Error occurred in scraping Karangasem website')
	print(sys.exc_info()[0], 'occurred.') 
	try:
		print('Trying to re-scrape...')
		import ScrapeKarangasem
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Jembrana')
try:
	import ScrapeJembrana
except:
	print('Error occurred in scraping Jembrana website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeJembrana
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Klungkung')
try:
	import ScrapeKlungkung
except:
	print('Error occurred in scraping Klungkung website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeKlungkung
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Mulai scraping website Bangli...')
try:
	import ScrapeBangli
except:
	print('Error occurred in scraping Bangli website')
	print(sys.exc_info()[0], 'occurred.')
	try:
		print('Trying to re-scrape...')
		import ScrapeBangli
	except:
		print(sys.exc_info()[0], 'occurred.')
		print('Error occurred again. Please check the error later.')
		print('Going on to the next script...')

print('Scraping selesai.')
