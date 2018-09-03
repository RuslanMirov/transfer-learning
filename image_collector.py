"""
Created on Wed May 17 14:24:02 2018

@author: Ruslan
"""

import time
from selenium import webdriver
import urllib.request

url = "https://www.google.com.ua/search?biw=1827&bih=1014&tbm=isch&sa=1&ei=HFkKW6TBC4PcwAK1-6WoBg&q=%D0%9C%D1%83%D0%BB%D1%8C%D1%82%D1%8F%D1%88%D0%BA%D0%B8&oq=%D0%9C%D1%83%D0%BB%D1%8C%D1%82%D1%8F%D1%88%D0%BA%D0%B8&gs_l=img.3..0l10.3681.5602.0.5897.9.7.0.2.2.0.132.823.0j7.7.0....0...1c.1.64.img..0.9.896...0i67k1.0.ixZxgwmaSF4"

imagelist = []
driver = webdriver.Chrome()


def safe():
    driver.implicitly_wait(10)
    for image in driver.find_elements_by_tag_name('img'):
        imagelist.append(image.get_attribute('src'))
        
    for i in range(200):
        name = "Cartoons." + str(i)
        urllib.request.urlretrieve(imagelist[i], name + ".png")
    

def main():
    driver.get(url)
    safe()
    time.sleep(160)
    driver.quit()

if __name__ == '__main__':
    main()
