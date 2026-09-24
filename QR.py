# live Qrcode contact project

first_name = "Mate"
last_name = "Dorine"
phone_number = "254117512360"
email = "matedorine@gmail.com"

square_color = "black"
background_color = "darkgreen"

!pip install qrcode[pil]
import qrcode
import matplotlib.pyplot as plt

vcard_text = f"""BEGIN:VCARD VAERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
TELL;TYRPE=CELL:{phone_number}
EMAIL:{email}
END:VCARD"""

qr =qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 5
)

qr.add_data(vcard_text)
qr.make(fit=True)

img = qr.make_image(
    fill_color =square_color,
    back_color = background_color
)

plt.imshow(img)
plt.axis("on")
plt.show