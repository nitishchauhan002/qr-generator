import qrcode

def generate_qr_code(input_data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
    )
    qr.add_data(input_data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img_str = qr_img.get_image().convert('1')  # Convert to black and white

    qr_img_str.show()

if __name__ == "__main__":
    data = input("Enter data for QR code: ")
    generate_qr_code(data)
