from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import student

url = 'https://codeforces.com/group/yskbyyufKw/contests'

Name_stud = student.get_name_student()
print(Name_stud)
#Info_stud = {}
#for name in Name_stud:
#    Info_stud[name].append([])
#print(Info_stud)

#для прописывания прямого пути к бин файлу chrome
options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

#открытие браузера
driver = webdriver.Chrome(chrome_options = options, executable_path=r'chromedriver.exe')
driver.get(url)
print("good")
time.sleep(20)

time_sleep = 10
stop_prog = 100
step = 0
while(step < stop_prog):
    time.sleep(time_sleep)
    driver.refresh()
    print("refresh", step)
    step = step + 1
#driver.quit()