from selenium import webdriver
from selenium import *
import time

#Accessing the file for students credential
file = open('Stud_login.txt', 'r')
dict = {} 

#Making it accessible by storing the values in Key-Value pairs
for line in file:
    a, *b = line.split()
    dict[a] = b
seatNo = list(dict.keys())
mom_name = list(dict.values())

#Initialization
driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
driver.get("http://results.unipune.ac.in/MCOM2013_Credit.aspx?Course_Code=70219&Course_Name=S.E.(2019+CREDIT+PAT.)+APR-MAY+2021")

#Iterating over the seat no. and mother's name.
for j in range(0,len(seatNo)):
    x = seatNo[j]
    y = " ".join(mom_name[j])
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtSeatno").send_keys(x) #Inputs seat no.
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtMother").send_keys(y) #Inputs mother's name
    #time.sleep(5)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSubmit").click() #Clicks the submit button

    #Exceptional Handling: in case the credentials are invalid
    try:

        #Locates and retrieves the sgpa and name of student
        sgpa = driver.find_element_by_xpath('''//*[@id="ctl00_ContentPlaceHolder1_pnlContents"]/span/div/table[2]/tbody/tr[30]/td[3]''').text
        name = driver.find_element_by_xpath('''//*[@id="ctl00_ContentPlaceHolder1_pnlContents"]/span/div/table[1]/tbody/tr[2]/td[1]''').text
        print(name)
        print(sgpa)

        #Writes the above info in the scores.txt file. 
        with open("scores.txt", "a") as text_file:
            text_file.write(name + "\n")
            text_file.write(sgpa + "\n\n")
        text_file.close()
    except:
        pass
    
    time.sleep(2)

    #Clears the text area
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtSeatno").clear()
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtMother").clear()
    

driver.close()
file.close()


