from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

circle_area = [(0,160),(1280,900)]

lion_img = Image.open("Lion.jpg")

draw = ImageDraw.Draw(lion_img)


draw.ellipse(circle_area,outline = "yellow",width = 10)



lion_img.show()
lion_img.save("c23lion.jpg")
