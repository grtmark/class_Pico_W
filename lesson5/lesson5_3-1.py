import widget

while True:
    kg=0  #清除變數
    cm=0  #清除變數
    cm,kg=widget.input_data() #呼叫 function
    
    print(f'身高={cm},體重={kg}')
    BMI=widget.calc_bmi(cm=cm,kg=kg)  #引述名稱的呼叫，可以不依照順序輸入引數
    print(f'BMI={BMI}')
    print(widget.get_status(BMI))
    
    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break
print('程式結束')