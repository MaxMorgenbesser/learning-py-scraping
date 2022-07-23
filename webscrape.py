from lib2to3.pgen2 import driver
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/maxmorgenbesser/Downloads/chromedriver/ ')
driver.get('https://osxdaily.com/2015/11/05/copy-file-path-name-text-mac-os-x-finder/')