import pyqrcode

url = input("Enter Your URL to Generate QR Code : ")
qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale=8)



