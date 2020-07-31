#requirements
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
a=int(input("Enter number to generate a qrcode of your number :\t"))
qr=pyqrcode.create(a)
qr.png("Name.png", scale=3 )# scale=Size of image
print("Done")