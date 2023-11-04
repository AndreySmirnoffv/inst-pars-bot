from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
import pickle
import json
from aiogram import Bot, Dispatcher, executor

path = './contacts/contacts.json'

#PATH = '/Users/nikitamoussa/Documents/kwork/tg-inst-pars/chrome/chromedriver'
#PATH = '/Users/nikitamoussa/Documents/kwork/tg-inst-pars/chrome/chromedriver'

driver = webdriver.Chrome()
accounts = '/Users/nikitamoussa/Documents/kwork/tg-inst-pars/assets/db/accounts.json'
def instagram_login():
    print("вход выполняется")
    try:
        driver.get('https://instagram.com')
        time.sleep(10)
        # button = driver.find_element(By.CLASS_NAME, '_a9-- _a9_0')
        # button.click()
        time.sleep(10)
        for cookie in pickle.load(open("nikky.kuznetsov@gmail.com_cookies", "rb")):
            driver.add_cookie(cookie)
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
        find_posts()
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
        
                # time.sleep(10) 
instagram_login()

async def find_posts():
    try:
        async with open(path, 'r') as file:
            data = await json.load(file)
            account = [obj["account"] for obj in data]
            print(account)
            for account in accounts:
                driver.get(account)
                current_time = datetime.now()
                if current_time < current_time * (24*7):
                    post = driver.find_element(By.CLASS_NAME, '')
                    post.screenshot()
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
    # while True:
    #     now = datetime.now()
    #     current_time = now.strftime('%D:%H')
    #     week = now.weekday()
    #     if current_time < week:
    #         post.screenshot()
            
# def process_telegram_login():
#     print("блок try запущен")
#     try:
#         print("операция начала свое выполнение")
#         driver.get('https://web.telegram.org')
#         time.sleep(15)
#         cont = driver.find_element(
#             By.XPATH, "/html/body/div[2]/div/div/div/div/button[1]")
#         time.sleep(5)
#         cont.click()
#         time.sleep(10)
#         enter_phonenumber = driver.find_element(
#             By.XPATH, "/html/body/div[2]/div/div[1]/div/div/form/div[2]/input")
#         enter_phonenumber.send_keys('15227542724')
#         time.sleep(5)
#         next_button = driver.find_element(
#             By.XPATH, "/html/body/div[2]/div/div[1]/div/div/form/button[1]")
#         next_button.click()
#         time.sleep(15)
#         code_input = driver.find_element(By.CLASS_NAME, "form-control")
#         code = input("enter code: ")
#         code_input.send_keys(code)
#         time.sleep(5)
#         password_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/form/div/input")
#         password_input.send_keys("N18112005k")
#         password_input.send_keys(Keys.ENTER)
#         time.sleep(5)
#     except Exception as e:
#         print(e)

# def process_telegram_contact_to_two_w(driver):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     try:
#         with open(path, 'r') as file:
#             data = json.load(file)
#             contact_name = [obj["username"] for obj in data]
#             print(contact_name)
#         # Получаем значения поля "username" для каждого объекта
#         # Выводим значения на экран
#         for username in contact_name:
#             print(username)
#             if not ' 2в' in username:
#                 find_contact = driver.find_element(
#                     By.ID, "telegram-search-input")
#                 time.sleep(5)
#                 find_contact.send_keys(username)
#                 time.sleep(5)
#                 find_contact.send_keys(Keys.ENTER)
#                 time.sleep(5)
#                 name_input = driver.find_element(
#                     By.CLASS_NAME, "Button smaller translucent round")
#                 name_input.click()
#                 time.sleep(5)
#                 client_name = driver.find_element(
#                     By.CLASS_NAME, "Button smaller translucent round")
#                 client_name.click()
#                 time.sleep(5)
#                 driver.find_element(
#                     By.CLASS_NAME, "icon icon-add-user").click()
#                 time.sleep(5)
#                 change_user_info_icon = driver.find_element(
#                     By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div/div/section/button")
#                 change_user_info_icon.click()
#                 time.sleep(5)
#                 change_username = driver.find_element(
#                     By.CLASS_NAME, "form-control")
#                 change_username.send_keys(" 2в")
#                 print(username)
#                 with open (path, 'w') as file:
#                     data = json.load(file)
            
#                 data.append(contact_name)

#                 with open (path, 'w') as file:
#                     json.dump(data, file, indent=4)
#                 return contact_name
#     except Exception as e:
#         print(e)
#     finally:
#         driver.close()
#         driver.quit()



# def process_telegram_contact_to_three_w(driver):
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     try:
#         with open(path, 'r') as file:
#             data = json.load(file)
#             contact_name = [obj["username"] for obj in data]
#             print(contact_name)
#         # Получаем значения поля "username" для каждого объекта
#         # Выводим значения на экран
#         for username in contact_name:
#             print(username)
#             if not ' 3в' in username:
#                 find_contact = driver.find_element(
#                     By.ID, "telegram-search-input")
#                 time.sleep(5)
#                 find_contact.send_keys(username)
#                 time.sleep(5)
#                 find_contact.send_keys(Keys.ENTER)
#                 time.sleep(5)
#                 name_input = driver.find_element(
#                     By.CLASS_NAME, "Button smaller translucent round")
#                 name_input.click()
#                 time.sleep(5)
#                 client_name = driver.find_element(
#                     By.CLASS_NAME, "Button smaller translucent round")
#                 client_name.click()
#                 time.sleep(5)
#                 driver.find_element(
#                     By.CLASS_NAME, "icon icon-add-user").click()
#                 time.sleep(5)
#                 change_user_info_icon = driver.find_element(
#                     By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div/div/section/button")
#                 change_user_info_icon.click()
#                 time.sleep(5)
#                 change_username = driver.find_element(
#                     By.CLASS_NAME, "form-control")
#                 change_username.send_keys(" 3в")
#                 with open (path, 'w') as file:
#                     data = json.load(file)
                    
#                 data.append(contact_name)
        
#                 with open (path, 'w') as file:
#                     json.dump(data, file, indent=4)
#                 return contact_name
#     except Exception as e:
#         print(e)
#     finally:
#         driver.close()
#         driver.quit()


# process_telegram_login()
    
# # with open(path, 'r', encoding='UTF-8') as file:
# #     data = json.load(file)
# #     print(file.read())
#     # process_telegram_contact(driver=driver)

# # Пример использования функций

# # Здесь можно выполнить другие операции или вызвать другие функции

# # Здесь можно выполнить другие операции или вызвать другие функции