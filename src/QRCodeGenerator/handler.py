import json
import qrcode
from PIL import Image
import base64
from io import BytesIO


def generate_qrcode(url):
    logo_file_path = "aws.jpg"
    color = "black"
    logo_base_width = 110

    logo = Image.open(logo_file_path)
    logo_scale_percent = logo_base_width / float(logo.size[0])
    logo_height = int((float(logo.size[1]) * float(logo_scale_percent)))
    logo = logo.resize((logo_base_width, logo_height), Image.Resampling.LANCZOS)
    qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    qr_code.add_data(url)
    qr_code.make()
    img_logo = qr_code.make_image(fill_color=color, back_color="white").convert("RGB")
    pos = (
        (img_logo.size[0] - logo.size[0]) // 2,
        (img_logo.size[1] - logo.size[1]) // 2,
    )
    img_logo.paste(logo, pos)

    return img_logo


def convert_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue())


def handler(event, _):
    print(json.dumps(event))

    url = (event.get("queryStringParameters") or {}).get("url")
    if not url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "url is required"}),
        }

    print(f"Generating QR code for {url}")
    image = generate_qrcode(url)
    encoded_image = convert_image_to_base64(image)

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/jpg",
        },
        "body": encoded_image.decode(),
        "isBase64Encoded": True,
    }

    print(f"response = {json.dumps(response)}")

    return response
