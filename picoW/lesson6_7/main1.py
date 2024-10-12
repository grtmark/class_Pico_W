from machine import ADC,Timer,Pin,PWM,RTC

adc = ADC(4) # 建立實體=內建溫度測試器
converter_factor = 3.3 / 65535 # 將數值換算成電壓
red_led = Pin(15,Pin.OUT) #建立實體=> 外接 LED 開關
pwm = PWM(Pin(15),freq=2000) # 建立實體=>可控 LED 開關
rtc = RTC() #建立實體 =>時鐘

def do_thing(t):
    reading = adc.read_u16()*converter_factor 
    temerture = 27 -(reading - 0.7060)/0.001721
    year,month,day,weekly,hur,min,sec,info=rtc.datetime()
    
    print(temerture)
    print(f"現在時間：{year}/{month}/{day} - {hur}:{min}:{sec}")

def do_thing1(t):
    adc1=ADC(Pin(26))
    duty = adc1.read_u16()
    #red_led.toggle()
    pwm.duty_u16(duty)
    print(f"可變電阻：{round(duty/65535*10)}")

Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)