from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
chrome_options.add_argument("test-type");
chrome_options.add_argument("start-maximized");
chrome_options.add_argument("--js-flags=--expose-gc");  
chrome_options.add_argument("--enable-precise-memory-info"); 
chrome_options.add_argument("--disable-popup-blocking");
chrome_options.add_argument("--disable-default-apps"); 
chrome_options.add_argument("disable-infobars"); 
driver = webdriver.Chrome("chrome driver path",chrome_options=chrome_options)

driver.get("https://moodle.dbit.in/login/index.php")

driver.find_element_by_xpath('//*[@id="username"]').send_keys("username")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("password")
driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[2]/ul[1]/li[2]/a').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/div[1]/div[2]/div/div[3]/div[1]/h3/a').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/div[3]/div[2]/div[1]/div[2]/div[1]/h3/a').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/div[3]/div[2]/div/div[2]/div[1]/h3/a').click()
#driver.find_element_by_xpath('').click()