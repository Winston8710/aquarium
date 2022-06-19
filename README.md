# aquarium
智慧水族箱

## 1. 事件定義
- 設定情境 : 有養殖魚類需求的個人戶或大型水族館
- 相關設備 : 水族箱、適合養殖魚類的淡(鹹)水
- 主要活動 : 控制水族箱最適合生長環境

## 2. 在此情境下有哪些事件 :
- 事件一、在室內溫度、水溫過高時，可利用溫溼度感測器來發出警示燈，並將感測到的數據回傳至後台。
- 事件二、在水族館、或個人用戶養殖的水族箱的空間中，若有參觀者或不明物體接近時會發出警示燈，藉此提示用戶提高警戒。

## 3. sensor偵測 :
- 溫溼度感測器: 偵測水族館內(養殖之空間)溫度的變化
- 超音波感測器: 偵測距離內是否有參觀者或不明物體靠近


## 4. 應用情境架構圖
![image](https://user-images.githubusercontent.com/101661953/174477868-0a7e4b41-97e6-45ba-8463-58ea850d617e.png)

## 5. 應用情境示意圖
![image](https://user-images.githubusercontent.com/101661953/174477900-26be856b-fab8-4412-a9a1-b1daeae1fccd.png)

## 6. 系統架構
- 資料庫端：MySQL
- 伺服器 : XAMPP、Apache
- 智慧水族箱架構：
  -溫溼度感測器
  -超音波感測器
  -LED (紅*2、黃*1、綠*1 ) : 因為沒藍燈，以第二顆紅燈代替。
