from PIL import Image
import numpy as np
from matplotlib import pyplot
orgImage = Image.open('nature.jpg')


# orgImage.show()
# print(orgImage.format)

# numpyImage = np.asarray(orgImage)
# numpyImage = numpyImage + 50


# print("numpyImage:",type(numpyImage))
# print("pillowFormat:",type(orgImage))


# 28/02/2023
sizeOfImage = orgImage.size
print("Size Of Image:",sizeOfImage)

imageFormat = orgImage.format
print("Image Format:",imageFormat)

imageMode = orgImage.mode
print('Image Mode:',imageMode)

resizeImage = orgImage.resize((500,400))
resizeImage.save("natureImageResize.jpg","JPEG")

orgImage.thumbnail((120,200))
sizeOfImage = orgImage.size
print("Size Of Image:",sizeOfImage)
orgImage.save('thumbnaiImage.jpg', "JPEG")

cropImage = orgImage.crop((70, 70, 100, 100))
print(cropImage.size)
cropImage.show()

rotateImageOne = orgImage.rotate(45)
rotateImageTwo = orgImage.rotate(45, expand=True)
pyplot.subplot(1,2,1), pyplot.imshow(rotateImageOne), pyplot.title('first rotate')
pyplot.subplot(1,2,2), pyplot.imshow(rotateImageTwo), pyplot.title('second rotate')
pyplot.show()

orgImageOne = orgImage.copy()
orgImageOne.show()
