from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import pyautogui

path = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
hashtags = ["#programming", "#coding", "#programmer", "#python", "#java", "#c++", "#c", "#programmingmemes", "#programminghumor"]
commentlist = []

def login():
    driver.get("https://www.instagram.com/")
    driver.maximize_window()

    time.sleep(3)
    driver.find_element_by_xpath("//input[@name=\'username\']").send_keys("coders.arena_")
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys("aditya@123")
    driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

    time.sleep(3)

def search():
    input = random.choice(hashtags)
    search = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/input")
    search.send_keys(input)

    time.sleep(4)
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]").click()

def getposts():
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[1]/div/div/div[1]/div[1]").click()

    count = 0
    while count < 10:
        time.sleep(2)
        like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span")
        like.click()

        time.sleep(0.5)
        pyautogui.press("down")
        time.sleep(2)

        commentlist = ["nice", "helpful", "good"]
        comment_box = driver.find_element_by_class_name("Ypffh")
        comment_box.click()
        for i in random.choice(commentlist):
            pyautogui.press(i)
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div[1]/form/button").click()
        count += 1
        time.sleep(2)
        driver.find_element_by_link_text("Next").click()
        time.sleep(1)

if __name__ == '__main__':
    login()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)
    search()
    time.sleep(2)
    getposts()