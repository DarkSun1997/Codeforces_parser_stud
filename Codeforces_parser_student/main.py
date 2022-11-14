from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import student
import generate

url = 'https://codeforces.com/group/yskbyyufKw/contests'

def Chrome_bro():
    # для прописывания прямого пути к бин файлу chrome
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    # открытие браузера
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
    driver.get(url)
    print("Ожидание регистрации WhiteSun97...")
    time.sleep(20)
    print("Запуск процесса...")
    time_sleep = 10
    stop_prog = 100
    step = 0
    #element = driver.find_element_by_class_name('contest-table')

    #print(element)
    #driver.quit()
    time.sleep(2000)


generate.generate_folder_stud()
#Name_stud = student.get_name_student()
#print(Name_stud)
#Info_stud = {}
#strin = b'    #include \u003ciostream\u003e\r\n    #include \u003cvector\u003e\r\n    using namespace std;\r\n    long long n,i,j;\r\n    vector \u003clong long\u003e v1,v2,v3;\r\n    int main()\r\n    {cin\u003e\u003en;\r\n    for (i\u003d0;i\u003cn;i++){\r\n        cin\u003e\u003ej;\r\n        v1.push_back(j);\r\n        cin\u003e\u003ej;\r\n        v2.push_back(j);\r\n       \r\n        v3.push_back(0);\r\n    }\r\n    for(i\u003d0;i\u003cn;i++){\r\n        v3[i]\u003dv1[i]+v2[i];\r\n    }\r\n    for (i\u003d0;i\u003cn;i++){\r\n        cout\u003c\u003cv3[i]\u003c\u003cendl;\r\n    }\r\n        \r\n    }'.decode("unicode-escape")
#print(strin)
#for name in Name_stud:
#    Info_stud[name] = {}
#print(Info_stud)
#Chrome_bro()