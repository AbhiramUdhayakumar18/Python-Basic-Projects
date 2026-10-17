#create a venv as well for this project then continue to 
#pip install qrcode followed by
#pip install Pillow. Now run the program !
import qrcode

data = input("Enter the text or URL : ").strip()
file_name = input("Enter the file name : ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(
    fill_color='black',
    back_color='white'
)

image.save(file_name)
print(f"QR Code saved as {file_name}")