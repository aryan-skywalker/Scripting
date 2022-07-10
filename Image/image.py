from PIL import Image, ImageFilter

img = Image.open('Scripting\pokemon\pikachu.jpg')

#1
#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img.save("blur.png", 'png')

#2
#filtered_img = img.convert('L')
#filtered_img.save("grey.png", 'png')

#filtered_img.show()

#3
#crok = filtered_img.rotate(90)
#crok.save("grey.png", 'png')
#crok.show()

#4
#size = filtered_img.resize((900 , 900))
#size.save("grey.png", 'png')
#size.show()

#5
#See how to crop image in docs

#6
#Thumbnail decides the best aspect ratio
#of the file after compressing it (USEFUL)
img.thumbnail((400, 400))
img.save('thumbnail.jpg')

print(img)
print(img.format)
print(img.size)
