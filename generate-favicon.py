from PIL import Image, ImageDraw, ImageFont


size = (64, 64)
img = Image.new("RGBA", size, (255, 255, 255, 0))

draw = ImageDraw.Draw(img)

draw.ellipse((4, 4, 60, 60), fill=(0, 100, 255, 255))

try:
    font = ImageFont.truetype("arial.ttf", 36)
except:
    font = ImageFont.load_default()

text = "M"

bbox = draw.textbbox((0, 0), text, font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

position = ((size[0] - w) // 2, (size[1] - h) // 2)

draw.text(position, text, font=font, fill=(255, 255, 255, 255))

img.save("favicon.ico", format="ICO")
print("favicon.ico criado com sucesso!")
