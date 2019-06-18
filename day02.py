import requests
# 请求百度，需要注意：一定要带上http/https
# response = requests.get('http://www.baidu.com')
# print(response)
# print(response.test)
print(response.headers)

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')