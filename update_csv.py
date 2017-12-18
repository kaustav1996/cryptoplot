from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os
import shutil
def update1():
	outputdir="."
	service_log_path = "{}/chromedriver.log".format(outputdir)
	service_args = ['--verbose']
	os.system('RMDIR "C:/data/" /S /Q')
	prefs = {"download.default_directory" : "C:\data"}
	option = webdriver.ChromeOptions()
	option.add_experimental_option("prefs",prefs)
	browser = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=option, service_args=service_args,service_log_path=service_log_path)

	urls=["https://www.coingecko.com/en/price_charts/litecoin/eur","https://www.coingecko.com/en/price_charts/bitcoin/eur","https://www.coingecko.com/en/price_charts/bitcoin-cash/eur","https://www.coingecko.com/en/price_charts/ethereum/eur","https://www.coingecko.com/en/price_charts/dash/eur"]
	while(len(urls)!=0):
		browser.get(urls[0])
		urls.pop(0)
		browser.execute_script("var elems = document.getElementsByClassName('btn btn-sm dropdown-toggle btn-outline-dark');for(var i= 0;i<elems.length;i++){elems[i].click();}")
		browser.execute_script("var elems = document.getElementsByClassName('dropdown-item');for(var i= 0;i<elems.length;i++){elems[i].click();}")

