from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

ST_DOWN = 100
ST_UP = 10
# CHROME_DRIVER_PATH = "/Users/rustam/Desktop/py_projects/practice_bootcamp/selenium_pars"
T_EMAIL = "e"
T_PASS = "p"
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = ""
        self.down = ""

    # def get_internet_speed(self):
    #     self.driver.get(url=SPEED_URL)
    #     go_button = self.driver.find_element(By.CSS_SELECTOR, value="a.js-start-test.test-mode-multi")
    #     go_button.click()
    #     sleep(60)
    #     self.down = (self.driver.find_element(By.CSS_SELECTOR, value="span.result-data-large.number.result-data-value.download-speed")).text
    #     self.up = (self.driver.find_element(By.CSS_SELECTOR, value="span.result-data-large.number.result-data-value.upload-speed")).text

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        sleep(10)

        # logging in to twitter with direct url
        email_field = self.driver.find_element(By.CSS_SELECTOR, value="input[type='text']")
        email_field.click()
        email_field.send_keys(T_EMAIL, Keys.ENTER)
        sleep(4)
        pass_field = self.driver.find_element(By.CSS_SELECTOR, value="input[type='password'].r-30o5oe.r-1dz5y72.r-13qz1uu")
        pass_field.click()
        pass_field.send_keys(T_PASS, Keys.ENTER)
        sleep(5)

        # opening post form
        post_button = self.driver.find_element(By.CSS_SELECTOR, value="a[aria-label='Post'].css-175oi2r.r-sdzlij")
        post_button.click()
        sleep(3)

        # field of form
        post_form = self.driver.find_element(By.CSS_SELECTOR, value="div.notranslate.public-DraftEditor-content[role='textbox']")
        post_form.click()
        sleep(5)
        post_form.send_keys(f"Hey Internet Provider, why my internet speed {self.down}down/{self.up}up when I pay for {ST_DOWN}down/{ST_UP}up?")

        sleep(5)

        # post/send tweet
        send_button = self.driver.find_element(By.CSS_SELECTOR, value="div[role='button'].css-175oi2r.r-sdzlij[data-testid='tweetButton']")
        send_button.click()
        sleep(3)
        # check result
        print("Tweet successful")


speed_bot = InternetSpeedTwitterBot()

speed_bot.tweet_at_provider()
