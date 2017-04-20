import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import credentials

sswidth=1024
ssheight=768




def JAASstart(driver):
   
   driver.set_window_size(1024, 320)
   driver.get("https://jujucharms.com/")
    # Set cookie to remove annoying notification
   
   driver.add_cookie({'name' : '_cookies_accepted', 'value' : 'true', 'domain' : 'jujucharms.com'})
   driver.get("https://jujucharms.com")
   main=driver.current_window_handle
   sleep(5)
   driver.find_element_by_css_selector('.inactive.menu-link.js-menu-login').click()
   # get the popup window and switch
   sleep(5)
   signin_window_handle = None
   while not signin_window_handle:
     for handle in driver.window_handles:
       if handle != main:
         signin_window_handle = handle
         break
   driver.switch_to.window(signin_window_handle)
   e = driver.find_element_by_id("id_email")
   e.clear()
   e.send_keys(credentials.sso_email)
   e = driver.find_element_by_id("id_password")
   e.send_keys(credentials.sso_password) 
   e.send_keys(Keys.RETURN)
   sleep(5)
   driver.close()
   driver.switch_to.window(main)
   driver.set_window_size(sswidth,ssheight)
   sleep(5)
   driver.save_screenshot('jaas-start.png')
   driver.find_element_by_css_selector('.button--inline-positive').click()
   sleep(5)
   driver.save_screenshot('jaas-canvas.png')

def main():
   driver = webdriver.Firefox('drivers')
   JAASstart(driver)



if __name__ == '__main__':
   main()
   
