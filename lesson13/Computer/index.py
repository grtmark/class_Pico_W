
# 匯入 Python MQTT 第三方模組，需要另外安裝
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-54/#")

def on_message(client, userdata, msg):
    #接受訂閱資訊
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

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
    main()