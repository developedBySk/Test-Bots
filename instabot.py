from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

class Jarvis():
	def __init__ (self,username,password):
		self.username = username
		self.password = password
		print("Initializing Jarvis.....")
		self.bot = webdriver.Firefox()
		print("Welcome,starting my job, Mr.Tony Stark")

	def login(self):
		bot = self.bot 
		bot.get('https://www.instagram.com/accounts/login/?next=/direct/t/340282366841710300949128348198171523470/')
		time.sleep(3)
		username = bot.find_element_by_name('username')
		password = bot.find_element_by_name('password')
		username.clear()
		password.clear()
		username.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(7)
		
		#to click on DM
		pyautogui.moveTo(x=990,y=107)
		pyautogui.click(x=990,y=107)
		time.sleep(2)
		#to remove notification box
		pyautogui.moveTo(x=681,y=531)
		pyautogui.click(x=681,y=531)

		
		#to click on DM id
		pyautogui.moveTo(x=337,y=241)
		time.sleep(2)
		pyautogui.click(x=337,y=241)
		time.sleep(1)
		#to click on message
		pyautogui.moveTo(x=657,y=647)
		time.sleep(2)
		pyautogui.click(x=657,y=647)
		#to write message
		time.sleep(3)

		# that part didn't worked
		'''f = "hello"
		for word in f:
			pyautogui.typewrite(word)
			pyautogui.press("enter")'''
sanjay = Jarvis('')
sanjay.login()
