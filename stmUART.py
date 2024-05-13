import tkinter as tk
import serial

def LED_ON():
    print("LED ON!!!")
    ser = serial.Serial('COM3', 9600)
    data_to_send = b'1'
    ser.write(data_to_send)
    ser.close()


def LED_OFF():
    print("LED OFF!")
    ser = serial.Serial('COM3', 9600)
    data_to_send = b'0'
    ser.write(data_to_send)
    ser.close()


# Ana pencere oluşturma
root = tk.Tk()
root.title("STM LED BLINK")

# Butonları oluşturma
buton1 = tk.Button(root, text="ON", command=LED_ON)
buton1.pack(pady=10)

buton2 = tk.Button(root, text="OFF", command=LED_OFF)
buton2.pack(pady=10)

# Pencereyi çalıştırma
root.mainloop()
