from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time 

class Jarvis:
	def __init__(self):
		print("Initializing Jarvis.....")
		self.bot = webdriver.Firefox()
		print("Welcome,starting my job, Mr.Tony Stark")

	def entry(self):
		bot = self.bot
		action = ActionChains(bot)
		bot.get('localhost:3000')
		time.sleep(3)
		input = bot.find_element_by_class_name('input')
		submit = bot.find_element_by_class_name('submit')
		Lists=['hello','test','success','relaunch','complete','delete','himanshu chadarmod']
		for list in Lists:
			input.send_keys(list)
			time.sleep(1)
			submit.send_keys(Keys.RETURN)
			time.sleep(1)
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')

		todo = bot.find_element_by_class_name('todo')
		complete = todo.find_element_by_class_name('complete-btn')
		delete = bot.find_element_by_class_name('trash-btn')

		complete.click()
		time.sleep(5)
		print("Task completed sir, Shutting Down")
		bot.close()
todo = Jarvis()
todo.entry()