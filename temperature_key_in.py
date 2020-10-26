import requests
from bs4 import BeautifulSoup
import time

# 全域變數
session_requests = requests.session()

def getToken(url) :
    global session_requests
    r = session_requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    token = soup.find("input", {"name":"token"})
    x_CS_ID = soup.find("input", {"name":"x_CS_ID"})
    if x_CS_ID != None :
        return token['value'], x_CS_ID['value']
    else :
        return token['value']

def login() :
    global session_requests
    url = 'https://ccweb.ncnu.edu.tw/temp_cs/login.php'
    token = getToken(url)
    with open('account.txt', encoding='utf8') as account :
        config = account.readline().strip()
    data = {'token':token, 'modal':0, 'username':config, 'password':config}
    r = session_requests.post(url, data)
    soup = BeautifulSoup(r.text, 'html.parser')

def keyin() :
    global session_requests
    url = 'https://ccweb.ncnu.edu.tw/temp_cs/anti_ncov_ncnu_member_take_temp_recordadd.php'
    courseName = input('請輸入要輸入體溫的課程名稱: ')
    with open(courseName + '.txt', 'r', encoding='utf8') as file :
        stuList = file.readlines()
        stuList = stuList[1:]
        for i in range(len(stuList)) :
            stuList[i] = stuList[i].strip().split('    ')
            stuList[i] = {
                'stuID' : stuList[i][0],
                'name' : stuList[i][1],
                'state' : stuList[i][2]
            }
    count = 0
    for row in stuList :
        if row['state'] == '0' :
            continue
        token, x_CS_ID = getToken(url)
        data = {
            'token' : token,
            't' : 'anti_ncov_ncnu_member_take_temp_record',
            'action' : 'insert',
            'modal' : 0,
            'x_CardUID' : row['stuID'],
            'x_memberType' : 'B',
            'x_memberID' : row['stuID'],
            'x_memberName' : row['name'],
            'x_level1_unit_UID' : '2',
            'x_level2_unit_UID' : '13',
            'x_temperature' : 36,
            'x_body_status[]' : '良好無異樣',
            'x_go_to_the_doctor' : 'N',
            'x_remark' : '',
            'x_CS_ID' : x_CS_ID
        }
        r = session_requests.post(url, data)
        soup = BeautifulSoup(r.text, 'html.parser')
        if '量測資料已儲存' in r.text or '新增資料成功' in r.text:
            print(row['name'] + "'s temperature key in Successfully")
            count += 1
        else :
            print(row['name'] + "'s temperature key in failed")
            with open('ERROR_log.txt', 'a', encoding='utf8') as log :
                log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': ' + row['name'] + "'s temperature key in failed " + str(r) + '\n')
        # 怕被抓爬蟲
        time.sleep(1)
    print('Key in', count, 'data, Total', len(stuList))

def main() :
    # 登入帳號
    login()
    # 輸入資料
    keyin()

if __name__ == '__main__' :
    main()