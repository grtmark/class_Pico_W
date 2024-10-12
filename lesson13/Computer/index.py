
# 匯入 Python MQTT 第三方模組，需要另外安裝
import paho.mqtt.client as mqtt
from datetime import datetime
import os,csv

def recoed(r):
    #檢查 data 目錄是否存在，如不存在則新增
    os.getcwd()
    data_dir = os.path.join(root_dir,'data')
    data_dir
    if not os.path.isdir(data_dir):
        os.mkdir('data')
    else:
        print('目錄已存在')
    filename = datetime.now().strftime("%Y-%m-%d")+".log" #用時間來取檔案名稱
    full_pathname = os.path.join(data_dir,filename) #取得檔案的絕對路徑
    if not os.path.exists(full_pathname):
        #如果沒有這個檔案，就建立檔案
        print("沒有這個檔案，建立檔案")
        with open(full_pathname,mode='w', encoding='utf-8',newline='')as file:
            file.write("時間,設備,值\n")
    with open(full_pathname,mode='a',newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(r)

def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-54/#")

def on_message(client, userdata, msg):
    #接受訂閱資訊
    global led_origin_value #把 led_origin_led 強制指定為全域變數，避免程式判斷錯誤
    topic = msg.topic #把 topic 指定為 meg.topic
    value = msg.payload.decode()
    if topic == "SA-54/LED_LEVEL":
        led_value = int(value)
        if led_value != led_origin_value:
            led_origin_value = led_value
            print(f"led_value={led_value}")
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #取得需要的時間格式
            log_data = [time_now,"SA-54\LED_LEVEL",led_value] #產生紀錄內容
            recoed(log_data)
    #print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'") #顯示即時 MQTT 訊息

def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 設定用戶名和密碼
    username = "pi"
    password = "raspberry"
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message 
    client.connect("192.168.0.252", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    led_origin_value = 0 #為避免成為區域變數導致執行功能後內容丟失，要在此宣告成為全域變數
    main()