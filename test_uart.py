from machine import UART                       # import module UART (library)
uart = UART(0, 115200)                         # uart port0 baute rate 115200
print(uart)                                    # print the initialisation of uart

strMsg = ''                                    # declare an empty string

while True:                                    # loop
    if uart.any() > 0 :                        # test if serial available
        print('Serial Available')
        strMsg = uart.read()                   # store data to bytearray
        strMsg = strMsg.decode("utf-8")        # bytearray to string
        if type(strMsg) is str:                # check if string
            print(strMsg)
            strId = strMsg[0:2]                # string to substring
            # print(strId)
            if strId == 'id':                  # check if str is "id"
                print('ok')
                strVal = strMsg[2:5]           # string to substring
                if strVal.isdigit():           # check if str is number
                    # print(strVal)
                    intVal = int(strVal)       # string to int
                    if type(intVal) is int:    # check if integer
                        print(intVal)
