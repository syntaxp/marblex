from LineNotify  import LineAPI
import time

from mbx import NKA , NKT
time.sleep(2)

message = '\n NKT : {} บาท {} \n NKA : {} บาท {}'

time.sleep(5)

while True:
    try:
        LineAPI.SendMessage(message.format(NKT.Price  , NKT.Percent , NKA.Price , NKA.Percent))
    except:
        pass

    time.sleep(60)

    