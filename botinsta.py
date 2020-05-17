from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\babil\Desktop\PROJETOS\BOT INSTAGRAM\chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_elements = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_elements.clear()
        password_elements.send_keys(self.password)
        password_elements.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtirFotos('woman')


    def curtirFotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath(
                    '//button[@class="wpO6b "]').click()
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                time.sleep(5)



barbaraBot = InstagramBot('babilsa', '123barbara098')
barbaraBot.login()
