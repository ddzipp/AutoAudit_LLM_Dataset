import time

import splitPHPDueToTokens

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def send_prompt(chrome, prompt):
    # 获取输入框、发送按钮的xpath表达式
    textarea = '//textarea[@class="home_chat-input__qM_hd"]'
    submit_button = '//button[@class="button_icon-button__BC_Ca undefined undefined home_chat-input-send__rsJfH clickable button_primary__7a7UW"]'
    # selenium自动发送prompt
    chrome.find_element(By.XPATH, textarea).clear()
    chrome.find_element(By.XPATH, textarea).send_keys(prompt)
    time.sleep(2)
    chrome.find_element(By.XPATH, submit_button).click()
    time.sleep(5)


def send_msg(chrome, msg):
    # 获取输入框、发送按钮的xpath表达式
    textarea = '//*[@id="prompt-textarea"]'
    submit_button = '/html/body/div[1]/div[1]/div[2]/div/main/div[3]/form/div/div[2]/button'
    # //*[@id="__next"]/div[1]/div/div/main/div[3]/form/div/div[1]/button
    # /html/body/div[1]/div[1]/div[2]/div/main/div[3]/form/div/div[2]/button
    # selenium自动获取输入框的内容，并发送
    chrome.find_element(By.XPATH, textarea).clear()
    chrome.find_element(By.XPATH, textarea).send_keys(msg)
    print("\nsleeping:")
    for i in range(25):
        time.sleep(1)
        print(i, end=" ")
    try:
        chrome.find_element(By.XPATH, submit_button).click()
    except:
        print("can't find click button, maybe the message has already sent... send_msg now automatically returns")
    # time.sleep(20)


def get_msg(file_path):
    data = []
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip(" ")
            data.append(line)
        return data


def split_text(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        parts = content.split('@@@@head@@@@')
        return parts


def get_answers(chrome, outputpath, beginIdx, endIdx, Mode='a'):
    Op = outputpath
    with open(Op, Mode, encoding='utf-8', errors='replace') as file:
        for i in range(beginIdx, endIdx + 2, 2):
            Xp = "/html/body/div[1]/div[1]/div[2]/div/main/div[2]/div/div/div/div[{idx}]/div/div[2]/div[1]/div/div/p".format(
                idx=i)
            text = chrome.find_element(By.XPATH, Xp).text
            file.write('\n' + text + ',')


# /html/body/div[1]/div[1]/div[2]/div/main/div[2]/div/div/div/div[4]/div/div[2]/div[1]/div/div/p
# /html/body/div[1]/div[1]/div[2]/div/main/div[2]/div/div/div/div[30]/div/div[2]/div[1]/div/div/p


def answers_get():
    print("Now get the answers from gpt and put them in a file...")
    get_answers(chrome=browser, outputpath="106_120.txt", beginIdx=4, endIdx=32)
    print("Done")


def submit_msg():
    data = get_msg('8.txt')
    zzz = 0
    for msg in data:
        send_msg(chrome=browser, msg=msg)
        zzz = zzz + 1
        print("zzz")


if __name__ == "__main__":
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9576")
    browser = webdriver.Chrome(options=options)

    # submit_msg()

    answers_get()

    while True:
        a = 1
        print("done!!")
    # chrome.quit()
