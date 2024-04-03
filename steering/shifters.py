from gpiozero import Button
from time import sleep

#NOTE: if gear = 0 then the gear is in neutral
gear = 0

def upshift():
    global gear

    if gear != 4:
        gear += 1

def downshift():
    global gear

    if gear != 0:
        gear -= 1

def main():
    upshift_btn = Button(20)
    downshift_btn = Button(21)

    while True:
        upshift_btn.when_pressed = upshift
        downshift_btn.when_pressed = downshift

        if gear == 0:
            print('N')
        else:
            print(gear)

if __name__ == '__main__':
    main()