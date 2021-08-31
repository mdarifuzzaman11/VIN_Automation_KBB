from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path = '/Users/mdarifuzzaman/Documents/All Programming/Python Single Projects/drivers/chromedriver')

#the Website to go to for the automation
driver.get('https://www.kbb.com/whats-my-car-worth/?ico=kbbvalue') 

#this Will click on the VIN button
driver.find_element_by_css_selector("main#content > div:nth-of-type(2) > div > div > div > div > div > div > div > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > label:nth-of-type(2) > div > div > div").click() 

#This will enter the VIN# of the car 
driver.find_element_by_css_selector("div#vinNumberInput > label > input").send_keys("1FA6P8AM4F5363926")

#this will click on the GO Button
driver.find_element_by_css_selector("main#content > div:nth-of-type(2) > div > div > div > div > div > div > div > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > button > span").click()

#this will click on the drop down on the site
#driver.find_element_by_css_selector("div#transmission > select").click

driver.find_element_by_class_name("input-label css-1g7gm9q-BaseLabel-StyledInnerLabel e21cbi80").click()

driver.find_element_by_class_name("input-label css-1g7gm9q-BaseLabel-StyledInnerLabel e21cbi80").send_keys("85000")

#Missing Millage and the rest still wokring on it.