import pyqrcode

url = input("enter url:")

output_path = ""

try:
    qr = pyqrcode.create(url)
except:
    print("unsucsessful")
finally:
    print("qr code generated")

qr.svg("qqr.svg", scale=8)