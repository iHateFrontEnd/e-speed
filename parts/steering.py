from gpiozero import RotaryEncoder, Button
import time

value = 0

reset_btn = Button(14)
rotor = RotaryEncoder(16, 15, wrap=True)

def reset_value():
    global value
    value = 0

def increment_value():
    global value
    value += 1

def decrement_value():
    global value
    value -= 1

while True:
    rotor.when_rotated_clockwise = increment_value
    rotor.when_rotated_counter_clockwise = decrement_value

    reset_btn.wait_for_release = reset_value
    print(value)
    time.sleep(1)
    