#This code generates a QR code for a given URL and saves it as an image file.
import qrcode

url = input("").strip()
file_path = "/home/shigwedhamatheus/Documents/my_python_project/tekkiewebsite.jpg"  # Specify the file path where you want to save the QR code image

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

#NB: The qrcode library is used to generate QR codes in Python. You can install it using pip if you don't have it already:
#pip install qrcode[pil]
#NB: The add_data method is used to add the URL data to the QR code, and the make_image method generates the QR code image. Finally, the save method saves the image to the specified file path.
#NB: Make sure to replace the file path with the desired location on your system where you want to save the QR code image.
#NB: When you run this code, it will prompt you to enter a URL. After you input the URL, it will generate a QR code for that URL and save it as an image file at the specified location.