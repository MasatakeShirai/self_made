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
import time


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
before_textarea = '#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div > textarea'
after_textarea = '#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea'
CopyButton = '#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__target_toolbar.lmt__target_toolbar--visible > div.lmt__target_toolbar__copy > button'

def LaunchDeepL(input_string):
	#chromeを起動
	driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

	#DeepLのページへアクセス
	driver.get(URL)

	#フォームに英文を入力する
	element = driver.find_element_by_css_selector(before_textarea)
	element.send_keys(input_string)

	#訳文が表示されるまで待期
	element = WebDriverWait(driver, 30).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, after_textarea))
	)

	time.sleep(10)

	#クリップボードにコピーする
	element = driver.find_element_by_css_selector(CopyButton)
	driver.execute_script('arguments[0].click();',element)

	#chromeを閉じる
	driver.close()
