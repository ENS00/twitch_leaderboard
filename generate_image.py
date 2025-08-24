# generate_image.py
from PIL import Image, ImageDraw, ImageFont

with open("leaderboard.txt") as f:
    lines = [l.strip() for l in f if l.strip()]
big_font_ratio = 1.525
font_size = 900/len(lines)
# long text may exceed image, so font has a max size
if font_size > 55:
    font_size = 55

# Load template
img = Image.open("template.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Bekstap-Regular.ttf", font_size*big_font_ratio)#56

border = 60
cols = 0
width, height = img.size
scale_Y = height/width
text_len = (width-border)#/3
current_y = 240


for i, line in enumerate(lines):
    position = (border + cols*text_len,
        border + current_y)
    if i == 3:
        # only first 3 have bigger name
        font = ImageFont.truetype("Bekstap-Regular.ttf", font_size)#38
    if i == 0: # GOLD
        draw.text(position, line, font=font, fill="#ffd700")
    elif i == 1: # SILVER
        draw.text(position, line, font=font, fill="#c0c0c0")
    elif i == 2: # BRONZE
        draw.text(position, line, font=font, fill="#cd7f32")
    else:
        draw.text(position, line, font=font, fill="white")
    current_y += font.size*1.5
    if current_y + font.size*1.5 > height - border*2:
        # new column
        current_y = 0
        cols+=1

img.thumbnail((320,scale_Y*320), Image.Resampling.LANCZOS)

img.save("leaderboard.png")
