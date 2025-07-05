# generate_image.py
from PIL import Image, ImageDraw, ImageFont

# Load template
img = Image.open("template.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 30)

with open("leaderboard.txt") as f:
    lines = [l.strip() for l in f if l.strip()]

for i, line in enumerate(lines):
    draw.text((50, 50 + i*40), line, font=font, fill="white")

img.save("leaderboard.png")
