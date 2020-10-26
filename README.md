# NCNU temperature key in
## About
為因應武漢肺炎(COVID-19)，國立暨南國際大學(NCNU)施行了以下措施:
每堂課都必須登記全班學生的體溫，課後再將體溫登記表交由系辦輸入至計網中心所開發之體溫登錄系統。
然而每堂課的學生人數眾多，各系一天的課程也不少，人工將體溫登記表輸入至系統實為曠日廢時之舉，因此利用簡單的爬蟲程式，簡化輸入體溫的工作。

## Installation
#### Step 1 : Clone this repo
`git clone https://github.com/UncleHanWei/NCNU_temperature_key_in.git`

#### Step 2 : 建立相關檔案
需要建立的檔案如下:
1. account.txt
    - 內容僅需要一行由 NCNU 計中配發的帳號
    - 範例見 /example/account.txt
2. 各課程的學生名單.txt
    - 格式請參照範例
    - 範例見 example/student_list.txt

#### Step 3 : 安裝套件
1. `requests`
    - `pip install requests`
2. `beautifulsoup4`
    - `pip install beautifulsoup4`

## 操作教學
先打開電子課程修課名單，把紙本登記單上沒有填的、溫度異常的名字 的 溫度狀態標記為 0
在 CMD 執行 "python temperature_key_in.py" (路徑要對)
輸入 課程名稱(請參考名單檔案的名字)
等待輸入完成，若有失敗的，可再執行一次程式，或改使用網頁手動登記
輸入完成後，請將名單的溫度狀態全部都改為 1 以便下一次使用