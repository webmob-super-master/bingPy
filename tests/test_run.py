from bing import manipulateBing

def main():
	for i in range(1,4):
		chrome = manipulateBing()
		chrome.login(i)
		time.sleep(5)
		chrome.search()
		chrome.logout()

main()
