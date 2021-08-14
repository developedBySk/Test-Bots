from time import sleep
from alive_progress import alive_bar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from retrying import retry
# import pyautogui

class ambot():
    def __init__(self):
        self.bot = webdriver.Firefox()

    def open(self):
        bot = self.bot
        bot.get('https://www.amazon.in/')

    @retry
    def search(self):
        tripod = 'B09CCSM3T9'
        bot = self.bot
        productSearch = bot.find_element_by_name('field-keywords')
        productSearch.clear()
        sleep(0.3)
        productSearch.send_keys(tripod)
        productSearch.send_keys(Keys.RETURN)

    @retry
    def click(self):
         bot = self.bot
         product = bot.find_element_by_class_name('s-image')
         sleep(1)
         product.click()
        # pyautogui.click(x=362,y=510)

    @retry
    def tabs(self):
        bot = self.bot
        ProductID = ['B09CGG1JZ1','B09B5VHWJT','B09CG181X1','B09CCSXFKV','B09CCY1D1F','B09C34VF11','B09B4WWF75','B09B3K28VK','B09B2QQL95','B09B233DM6']

        for i in range(len(ProductID)-1):
            handles = bot.window_handles
            x = len(handles)
            handle = handles[x-1]
            bot.switch_to.window(handle)
            sleep(2)
            retry(stop_max_delay = 3)
            productSearch = bot.find_element_by_name("field-keywords")
            productSearch.clear()
            sleep(0.5)
            productSearch.send_keys(ProductID[i])
            productSearch.send_keys(Keys.RETURN) 
            self.click()
            
        for j in reversed(handles):
            bot.switch_to.window(j)
            if j == handles[0]:
                self.search()
            bot.close() 
         
        sleep(0.5)
        # if bot.title != "Amazon.in : B09CCSM3T9":
            # bot.close()
            # bot.switch_to.window(main)
    
    @retry
    def close(self):
        bot = self.bot
        bot.quit()

        
def perform():
    start = ambot()
    start.open()
    start.search()
    sleep(3)
    start.click()
    sleep(2)
    with alive_bar(100) as bar:
        for i in range(100):
            start.tabs()
            if i == 99:
                print("Task Completed\n")
                start.close()
            sleep(0.5)
            bar()
perform()
