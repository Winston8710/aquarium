import Adafruit_DHT
import time
import LED
import sql_info
import mysql.connector
from mysql.connector import Error
from datetime import datetime
sensor = Adafruit_DHT.DHT11

timelist = []
templist = []

GPIO = 14

def wet():

    while True:    
        for i in range(0,60,1): #每60秒將資料寫進資料庫
            LED.Setup(2,"OUT")
            LED.Setup(3,"OUT")
            LED.Setup(4,"OUT")

            currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
            humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
            
            if humidity is not None and temperature is not None:
                timelist.append(currentTime)
                templist.append(temperature)
                totallist= list(zip(timelist, templist)) #將時間、溫度寫入list
                print(currentTime,'-> Temp={0}*C %'.format(temperature))
                if((temperature>37)or(temperature<16)):
                    LED.TurnOnLED(4)#紅燈警示
                    time.sleep(2)
                    LED.TurnOffLED(4)
                    time.sleep(1)
                    print("Heatstroke Alert!")#水族箱水溫過高警示
                elif ((temperature>35)or(temperature<20)):
                    LED.TurnOnLED(3)#黃燈警示
                    time.sleep(2)
                    LED.TurnOffLED(3)
                    time.sleep(1)
                    print("Heatstroke Prevention Alert!")#水族箱水溫偏高警示
                else:
                    LED.TurnOnLED(2) #綠燈警示
                    time.sleep(2)
                    LED.TurnOffLED(2)
                    time.sleep(1)
                    print("NO Heatstroke Alert!")#水族箱水溫正常顯示
                time.sleep(2)
                  
            else:
                print('Failed to get reading. Try again!')
                time.sleep(1)
           
           
        try:
        # 連接 MySQL/MariaDB 資料庫，並將資料庫資訊另外建檔
            connection = mysql.connector.connect(
            host=sql_info.host ,          # 呼叫主機名稱
            database=sql_info.database, # 呼叫資料庫名稱
            user=sql_info.user,        # 呼叫帳號
            password=sql_info.password)  # 呼叫密碼

            sql = "INSERT INTO temp (datatime, temp) VALUES(%s, %s);"
        
        
        # 顯示目前使用的資料庫
            cursor = connection.cursor()
            cursor.executemany(sql, totallist)
            connection.commit()
           
        except Error as e:
            print("資料庫insert失敗：", e)

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("資料庫連線已關閉")
