from PIL import Image
##
##area = (230,1455,1110,770)
##size = (640,200)
##
#lion_img = Image.open("Lion.jpg")
#fruit_img = Image.open("fruit.png")
##
##print(lion_img.size, lion_img.format,lion_img.mode)
##print(fruit_img.size, fruit_img.format,fruit_img.mode)
##
##fruit_resz = fruit_img.resize(size)
##lion_cropped = lion_img.crop(area)
#lion_img.show()
#fruit_img.show()
##
##lion_cropped.save("lion_cropped.jpg")
##frui_resz.save("fruit_resized.png")
##


size = (120,120)



fruit_img = Image.open("fruit.png")


fruit_rotated = fruit_img.rotate(270)
fruit_converted = fruit_img.convert('L')

fruit_rotated.show()


fruit_rotate.save("돌리기.png")
fruit_converted.save("흑백.png")
