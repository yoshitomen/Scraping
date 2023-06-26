import time, sys
from selenium.webdriver.common.by import By
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from mylib.scraping.lib import ScrFunc, param

weekday = '土'

test_mode = param.debug_mode
def main():
    pre_result = [] #空きの変化検出用

    while(True):
            
        #Init処理
        driver = ScrFunc.GetDriver("https://reserve.fumotoppara.net/reserved/reserved-calendar-list")

        #空き曜日を検出してリストに格納
        available_day = Getavailable(driver)
        #LINEで空き日程を通知.
        if ( pre_result != available_day):
            ScrFunc.Notify_LINE_avail(available_day, "humotoppara_token")
            pre_result = available_day

        driver.quit()
        time.sleep(300)#5分に1回スクレイピング

def Getavailable(driver):
    ret = []
    offset = 0
    date_xpath = []
    for i in range(124):
        date_xpath.append(f'//*[@id="__layout"]/section/section/main/form/div[2]/div[2]/table/thead/tr/th[{str(i+2)}]/p[1]')
    #idを入れたらそのまま日付を返すリスト
    for index in range(7):
        chk_xpath = f'//*[@id="__layout"]/section/section/main/form/div[2]/div[2]/table/thead/tr/th[{str(index+2)}]/p[2]'
        #1は例外. 2から曜日が始まるのでindex+2.
        weekday_column = driver.find_element(By.XPATH, chk_xpath)
        if (weekday_column.text == weekday):
            offset = index + 2
            break
    if(test_mode):print(f'最初の{weekday_column.text}曜日は{offset-1}番目のセル')
    
    id = 0 #7の倍数を足して-1して引数に入れれば空き状況を返すインデックス.先頭から何番目か.
    #最初の土曜キャンプ宿泊へのXPATH.これ以降は7ずつ足す.
    for index in range(20):
        id = offset + index*7 - 2
        first_xpath=f'//*[@id="__layout"]/section/section/main/form/div[2]/div[2]/table/tbody/tr[2]/td[{id+1}]'
        val = driver.find_element(By.XPATH,first_xpath).text
        if(val != "ー"):break
    for index in range(20):
        temp_xpath = f'//*[@id="__layout"]/section/section/main/form/div[2]/div[2]/table/tbody/tr[2]/td[{id+1}]/p[1]'
        val = driver.find_element(By.XPATH,temp_xpath).text
        #val2 =(driver.find_element(By.XPATH,temp_xpath2)).text
        if (test_mode):print(val)
        if(val == "ー"):break
        elif (val != '×'):
            ret.append((driver.find_element(By.XPATH, date_xpath[id])).text)
        id += 7
       
    return ret


if __name__ == "__main__":
    main()
