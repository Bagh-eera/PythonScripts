import requests
from bs4 import BeautifulSoup

"""Combat Sports: MMA Boxing Thread"""
url = 'https://boards.4channel.org/wsg/thread/3786167'

def get_webm_links(url):
	#create a request
	req = requests.get(url)

	#create beautiful soup object
	soup = BeautifulSoup(req.content, 'html5lib')

	#find the link
	links = soup.find_all("a", class_ = "fileThumb")
	webm_links = [ "http:" + link.get('href') for link in links ]

	return webm_links

def download_webms(webm_links):
	
	for link in webm_links:
		file_name = link.split('/')[-1]

		print("Downloading file:%s"%file_name)

		#create response object
		r = requests.get(link, stream = True)

		#download started
		with open(file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024*1024):
				if chunk:
					f.write(chunk)

		print("%s downloaded!\n"%file_name)

	print("All videos downloaded!")
	return

if __name__ == "__main__":
	#get video links
	webm_links = get_webm_links(url)

	#download webms
	download_webms(webm_links)

