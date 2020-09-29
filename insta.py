from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome(executable_path = 'chromedriver.exe')	

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(5)
		email = bot.find_element_by_name('username').send_keys(self.username)
		password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)

		time.sleep(5)

	def searchHashtag(self,hashtag):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/tags/' + hashtag)

	def likePhotos(self,amount):
		bot = self.bot

		bot.find_element_by_class_name('v1Nh3').click()

		i = 1
		while i <= amount:
			time.sleep(3)
			bot.find_element_by_class_name('fr66n').click()
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			time.sleep(3)

			i += 1

		
		bot.get('https://www.instagram.com/' + self.username)





insta = InstagramBot('username', 'password')
insta.login()
insta.searchHashtag('photography')
insta.likePhotos(50)
