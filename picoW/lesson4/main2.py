from machine import Timer

count=0
def mycallback(t:Timeer):
    global count
    count+=1
    print(f"目前 mycallback 被執行：{count}次")
    if count >= 10:
        t.deinit()

led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=mycallback)

#Timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print(1))
# tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print("看屁"))
   

