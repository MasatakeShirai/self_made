from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

#あらゆる環境でSeleniumが動作できるように設定
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')

#chrome driverへのパス
DRIVER_PATH = os.path.expanduser('~/chromedriver_win32/chromedriver.exe')
#スクレイピングするURL
URL = 'https://www.deepl.com/ja/translator'

#英文を入力するフォームのセレクタ
textarea = '#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div > textarea'

#chromeを起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

#DeepLのページへアクセス
driver.get(URL)

#フォームに英文を入力する
element = driver.find_element_by_css_selector(textarea)
element.send_keys('Hello world!')