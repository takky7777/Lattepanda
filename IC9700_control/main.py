import serial
import create_command
from serial.tools import list_ports

#MAIN

def main():
    selectPort()

    command_array = create_command.createCommandArray()

    print(command_array)
    send_miss_check=0

    if input("send OK? yes->1 no->0") == "1":
        sendSerialData(command_array,selectPort())
    else:
        print("send error")





#PORT SELECT

def selectPort(baudrate=19200):
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.timeout = None   # タイムアウトはNone

    ports = list_ports.comports()  # ポートを取得
    devices = [info.device for info in ports]

    if len(devices) == 0:   #ポートが見つからない場合
        print('error: cannot find COM PORT')    
    elif len(devices) == 1:
        print("found one COM PORT")
    else:
        print("Choose Number of COM PORT:")
        for i, device in enumerate(devices):
            print(f"input {i:d} open {device}")
        num = int(input("Choose Number of COM PORT:"))
        ser.port = devices[num]

    try:
        ser.open()
        return ser
    
    except serial.SerialException:
        print("error: can't open COM PORT")
        return None


#SEND

def sendSerialData(command_array,ser):
        
    try:
        ser.write(bytes(command_array))  # バイト列に変換して送信2
        print("send command:", command_array)
        ser.close()  
    except serial.SerialException as e:
        print("send error:", str(e))




if __name__ == "__main__":
    main()
