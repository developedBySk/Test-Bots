from time import sleep
from alive_progress import alive_bar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# import pyautogui

class ambot():
    def __init__(self):
        self.bot = webdriver.Firefox()

    def open(self):
        bot = self.bot
        bot.get('https://www.amazon.in/')

    def search(self):
        mobile_lens_ASIN = 'B09CCSM3T9'
        bot = self.bot
        productSearch = bot.find_element_by_name('field-keywords')
        productSearch.clear()
        sleep(0.3)
        productSearch.send_keys(mobile_lens_ASIN)
        productSearch.send_keys(Keys.RETURN)

    def click(self):
         bot = self.bot
         product = bot.find_element_by_class_name('s-image')
         sleep(0.3)
         product.click()
        # pyautogui.click(x=362,y=510)

    def tabs(self):
        bot = self.bot
        mobile_lens_ASIN = 'B09CCSM3T9'
        handles = bot.window_handles
        main = bot.current_window_handle
        for handle in handles:
            bot.switch_to.window(handle)
            sleep(1)
        bot.close()
        productSearch = bot.find_element_by_name('field-keywords')
        productSearch.clear()
        sleep(0.5)
        productSearch.send_keys(mobile_lens_ASIN)
        productSearch.send_keys(Keys.RETURN)
        sleep(1)
        self.click()
        sleep(0.5)
        if bot.title != "Amazon.in : B09CCSM3T9":
            bot.close()
            bot.switch_to.window(main)
    
    def close(self):
        bot = self.bot
        bot.quit()

        
def perform():
    start = ambot()
    start.open()
    start.search()
    sleep(2)
    start.click()
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(0.1)
            bar()
            start.tabs()
            if i == 499:
                print("\n\t Task Completed")
                start.close()
            
perform()