# -*- coding: utf-8 -*-
from scrapy import Spider
import sys
from selenium import webdriver
from time import sleep

class YoutubeSpider(Spider):
    name = 'youtube'
    allowed_domains = ['https://www.youtube.com/']
    start_urls = ['https://www.youtube.com//']

    # take the command line argument video
    
    def __init__(self, video=None):
    	self.video = video

    #check for the window alive condition

    def isAlive(self, driver):
    	try:
    		if driver.current_url:
    			return True
    	except:
    		return False;

    def parse(self, response):
    	
    	driver = webdriver.Chrome('/home/srikanth/Downloads/chromedriver')
    	driver.maximize_window()
    	driver.get('https://www.youtube.com/')
    	
    	search_query = driver.find_element_by_name('search_query')
    	search_query.send_keys(self.video)
    	
    	search_button = driver.find_element_by_id('search-icon-legacy')
    	search_button.click()
    	
    	sleep(1)
    	
    	video_url = driver.find_element_by_class_name("ytd-video-renderer")
    	video_url.click()
    	# call for the window alive function
    	while self.isAlive(driver) == True:
    		sleep(1)