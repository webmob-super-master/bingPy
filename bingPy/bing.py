#! /usr/bin/env python3
#Built-ins
import os
import webbrowser, time

#Externals imports
from selenium import webdriver

#Internal imports
import bingCredentials as bing


class manipulateBing:
	"""
	Creates a Chrome webdriver instance and uses it to search Bing
	
	Args: None
	
	Usage: Call login method then search method to complete 30 searches for that account.  Logout when finished.
	"""
	
	def __init__(self):
		chromedriver = "..."
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.browser = webdriver.Chrome(chromedriver)

	def login(self,num):	
		self.browser.get('https://login.live.com/')
		username = self.browser.find_element_by_id('i0116')
		password = self.browser.find_element_by_id('i0118')

		cred = bing.getCredentials(num)

		username.send_keys(cred[0])
		password.send_keys(cred[1])

		submit = self.browser.find_element_by_id('idSIButton9')
		submit.click()

	def logout(self):
		self.browser.close()

	def search(self):
		searchTerm = []
		for i in range(0,30):
			searchTerm.append(str(i))
			time.sleep(1)
			self.browser.get('https://www.bing.com/search?q=' + searchTerm[i])
