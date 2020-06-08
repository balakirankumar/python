#requirements
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
a=int(input("Enter number to generate a qrcode of your number :\t"))
qr=pyqrcode.create(a)
qr.png("kiran.png", scale=3)
print("Done")