import time
from machine import Pin, ADC
from neopixel import NeoPixel

# WS2813 LED 설정 (GP16 핀, LED 10개)
TIMING = (280, 515, 515, 745)
led = NeoPixel(Pin(16), 10, timing=TIMING)

# MQ2 가스 센서 설정 (GP26 / A0 핀)
mq2 = ADC(Pin(26))

# 연기 감지 기준값 (실제 환경에 맞게 숫자 조정 필요)
THRESHOLD = 20000 

def set_color(r, g, b):
    for i in range(10):
        led[i] = (r, g, b)
    led.write()

while True:
    sensor_value = mq2.read_u16()
    print("현재 가스/연기 수치:", sensor_value)
    
    # 연기가 기준치보다 높게 감지된 경우 (경보)
    if sensor_value > THRESHOLD:
        # 빨간색으로 번쩍이기
        set_color(255, 0, 0)
        time.sleep(0.2)
        set_color(0, 0, 0)
        time.sleep(0.2)
    else:
        # 평소 상태 (초록색 유지)
        set_color(0, 50, 0)
        time.sleep(0.5)
