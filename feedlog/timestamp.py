from StringIO import StringIO
from time import strftime
from PIL import Image, ImageFont, ImageDraw

background_mode = "RGB"
background_size = (400, 150)
background_color = "white"
font_name = "feedlog/fonts/SFMono-Semibold.otf"
font_size = 120
font = ImageFont.truetype(font_name, font_size)
font_color = (50, 50, 50)
y_offset = 15

def drawTimestamp(timestamp):
    text_content = strftime('%H:%M')
    if timestamp:
        text_content = timestamp

    # Create background
    img = Image.new(background_mode, background_size, background_color)
    draw = ImageDraw.Draw(img)

    # Compute center
    textsize = draw.textsize(text_content, font=font)
    midpoint = (background_size[0]/2, background_size[1]/2)
    top_left = (midpoint[0] - textsize[0]/2, midpoint[1] - (textsize[1]/2) - y_offset)

    # Draw text
    draw.text(top_left, text_content, font_color, font=font)
    return img

