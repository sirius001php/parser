import sys
import time

import requests
# from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# your login
login = 'qwe'
# your password
password = 'qwe'
person_num = 2
# your site
url = 'https://'


def start_after_given_time(start_time):
    # Розділити рядок часу на годину, хвилини та секунди
    hours, minutes, seconds = map(int, start_time.split(':'))

    # Отримати поточний час
    current_time = time.localtime()
    current_hours = current_time.tm_hour
    current_minutes = current_time.tm_min
    current_seconds = current_time.tm_sec

    # Обчислити різницю між поточним часом та часом старту
    time_difference = (hours - current_hours) * 3600 + (minutes - current_minutes) * 60 + (seconds - current_seconds)

    # Перевірити, чи час старту ще не минув
    if time_difference > 0:
        print("Програма почне працювати через {} секунд".format(time_difference))
        time.sleep(time_difference)
        print("Програма почала працювати о {}:{}".format(hours, minutes))
        # Тут ви могли б додати вашу основну логіку програми
    else:
        print("Вказаний час вже минув")

def login_func(driver, item, value):
    log = driver.find_element(By.ID, item)
    log.clear()
    log.send_keys(value)
    time.sleep(2)

def auth(driver):
    login_func(driver, 'username', login)
    login_func(driver, 'password', password)
    login_button = driver.find_element(By.ID, 'loginButton').click()
    time.sleep(2)


def wait_element(driver, by, el):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((by, el))
        )
        element.click()
        print("Елемент було успішно клікнуто.")
    except Exception as e:
        print("Помилка під час очікування або кліку на елемент taskAmount:", e)


def command(driver):
    zx = True
    while zx == True:
        com = input("Enter command (exit or start) = ")
        if com == 'exit':
            zx = False
        elif com == 'start':
            start_time = input("Input time ")
            start_after_given_time(start_time)
            for i in range(12):
                refresh_button = driver.find_element(By.CLASS_NAME, "refreshDataTableBtn").click()
                try:
                    accept = driver.find_element(By.CLASS_NAME, 'tasks-modal-btn').click()

                    for j in range(200):
                        try:
                            totalTaskAmount = driver.find_element(By.CLASS_NAME, 'taskAmount')
                            totalTaskAmount.clear()
                            totalTaskAmount.send_keys('1')
                            break
                        except:
                            print("total task amount not found")
                        time.sleep(0.05)

                    wait_element(driver, By.ID, 'saveChanges')
                    time.sleep(3)
                    break
                except:
                    print("Not found")
                time.sleep(0.25)
            time.sleep(2)
        else:
            print("Not fount command, try again")

def start_work():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    try:
        driver.get(url=url)
        auth(driver)
        command(driver)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

start_work()
