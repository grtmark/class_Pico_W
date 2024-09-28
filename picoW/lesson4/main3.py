from machine import Timer, Pin

green_led = Pin("LED",Pin.OUT)
red_led = Pin(15,Pin.OUT)

green_led_count=0
red_led_count=0

def green_led_mycallback(t:Timer):
    global green_led_count
    green_led_count+=1
    #print(f"目前 mycallback 被執行：{count}次")
    green_led.toggle() #LED 改變狀態
    if green_led_count >= 100:
        t.deinit()
        
green_led_timer = Timer(period=100,mode=Timer.PERIODIC,callback=green_led_mycallback) #註冊功能，會在背景自動執行

green_led_count=0
def green_led_mycallback(t:Timer):
    global red_led_count
    red_led_count+=1
    #print(f"目前 mycallback 被執行：{count}次")
    red_led.toggle() #LED 改變狀態
    if red_led_count >= 100:
        t.deinit()
        
green_led_timer = Timer(period=500,mode=Timer.PERIODIC,callback=green_led_mycallback) #註冊功能，會在背景自動執行