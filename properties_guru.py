from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(executable_path='chromedriver.exe')

url="https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi" 
driver.get(url)

def searchresults():
    apt_type=[]
    location=[]
    price=[]
    ppu=[]
    area=[]
    facing=[]
    status=[]
    floor=[]
    furnish=[]
    free_attorney=[]
    bathroom=[]
    agent=[]
    posted=[]
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    blocks=driver.find_elements_by_class_name("filter-property-list")

    for b in blocks:
        head=b.find_element_by_class_name("filter-pro-heading").get_attribute("innerHTML")
        elem=b.find_element_by_class_name("filter-pro-heading")
        actions = ActionChains(driver)
        actions.move_to_element(elem).perform()
        apt_type.append(head.split('<span>')[0])

        loc=b.find_element_by_css_selector('div.col-8> h1 > span')
        location.append(loc.text)

        p=b.find_element_by_class_name("price")
        price.append(p.text)

        pu=b.find_element_by_class_name("price-per-unit")
        ppu.append(pu.text)

        a=b.find_element_by_class_name("col-4").get_attribute("outerHTML")
        ar=a.split('</span>')[1]
        area.append(ar.replace('<span class="inline">',''))

        f=b.find_elements_by_class_name("col-3")
        facing.append(f[1].get_attribute("innerHTML").split('</span>')[1])

        s=b.find_element_by_class_name("col-5").get_attribute("innerHTML")
        status.append(s.split('</span>')[1])

        li_ele=b.find_element_by_class_name("pro-list")
        items = li_ele.find_elements_by_tag_name("li")
        list_ele=[]
        for item in items:
            list_ele.append(item.text)
        floor.append(list_ele[0])
        furnish.append(list_ele[1])
        free_attorney.append(list_ele[2])
        bathroom.append(list_ele[3])

        ag=b.find_element_by_class_name("owner-name")
        agent.append(ag.text)

        po=b.find_element_by_class_name("owner-post")
        posted.append(po.text)
        print(len(posted))
    return apt_type,location, price,ppu, area,facing,status,floor,furnish,free_attorney,bathroom,agent,posted
    
apt_type,location, price,ppu, area,facing,status,floor,furnish,free_attorney,bathroom,agent,posted=searchresults()
sea_dict={"Title":apt_type,"Location":location, "Cost":price,"Price per unit":ppu, "Area": area, "Facing":facing,"Status":status,"Floor":floor,"Furnished":furnish,"Free/Attorney":free_attorney,"Bathroom":bathroom,"Owner":agent,"Posted":posted}
sea_csv=pd.DataFrame(sea_dict)
sea_csv.to_csv("propertiesgurur.csv")

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

#Reload page before selecting filters
driver.refresh()
driver.refresh()

driver.find_element_by_class_name("bd").click()
driver.implicitly_wait(5)
driver.execute_script('''document.querySelectorAll('.bedroom')[2].click()''')
driver.execute_script('''document.querySelectorAll('.bedroom')[3].click()''')
time.sleep(3)
driver.implicitly_wait(5)
driver.find_element_by_class_name("bd").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
apt_type,location, price,ppu, area,facing,status,floor,furnish,free_attorney,bathroom,agent,posted = searchresults()

sea_dict_34={"Title":apt_type,"Location":location, "Cost":price,"Price per unit":ppu, "Area": area, "Facing":facing,"Status":status,"Floor":floor,"Furnished":furnish,"Free/Attorney":free_attorney,"Bathroom":bathroom,"Owner":agent,"Posted":posted}
sea_csv_34=pd.DataFrame(sea_dict_34)
sea_csv_34.to_csv("propertiesgurur_34.csv")