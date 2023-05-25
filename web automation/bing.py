from selenium import webdriver

PATH = "/Applications/chromedriver"
br = webdriver.Edge(PATH)
br.get('https://www.bing.com')

