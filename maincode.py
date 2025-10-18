import qrcode

# Text or URL to encode
data = input("Enter the text or URL to encode in QR code: ")

# Generate QR Code
qr = qrcode.QRCode(
    version=1,  # controls size (1-40), 1 is 21x21
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each box in pixels
    border=4,  # border in boxes
)
qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")
print("✅ QR Code generated and saved as my_qr_code.png")

data = "https://yourwebsite.com"
img = qrcode.make(data)
img.save("quick_qr.png")
