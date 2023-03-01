from matplotlib import image
from matplotlib import pyplot 
import numpy as np
orgimage = image.imread('nature.jpg')

# print(orgimage)


def brightness():
    IncreaseBrightness = orgimage + 20
    ReduceBrightness = orgimage - 10
    pyplot.subplot(1,3,1), pyplot.imshow(orgimage), pyplot.title('Orgnial Image')
    pyplot.subplot(1,3,2), pyplot.imshow(IncreaseBrightness), pyplot.title('Increase Brightness')
    pyplot.subplot(1,3,3), pyplot.imshow(ReduceBrightness), pyplot.title('Reduce Brightness')
    pyplot.show()
# brightness()

# saturation

#contrast

def saturation():
    pyplot.subplot(1,2,1), pyplot.imshow(orgimage), pyplot.title('Orgnial Image')
    orgimage_to_ndArray = np.array(orgimage)
    for pexelIndex,pexel in np.ndenumerate(orgimage):
        if pexel < 150:
            orgimage_to_ndArray[pexelIndex] = pexel + 50
        elif pexel > 100:
            orgimage_to_ndArray[pexelIndex] = pexel - 50
    pyplot.subplot(1,2,2), pyplot.imshow(orgimage_to_ndArray), pyplot.title('contrast Image')
    pyplot.show()
# saturation()

def compare(redPexel, greenPexel, bluePexel, tolerance, index, orgimage_to_ndArray):
   


    pexel = {
    1:{ 
     'allEqual':redPexel == greenPexel == bluePexel  
    },
    2:{ 
     'redPexel':((redPexel <= (greenPexel + tolerance)) and (redPexel >= (greenPexel - tolerance))) and ((redPexel <= (bluePexel + tolerance + tolerance)) and (redPexel >= (bluePexel - (tolerance + tolerance))))
    },
    3:{ 
     'greenPexel':((greenPexel <= (redPexel + tolerance)) and (greenPexel >= (redPexel - tolerance))) and ((greenPexel <= (bluePexel + tolerance)) and (greenPexel >= (bluePexel - tolerance)))   
    },
    4:{ 
     'bluePexel':((bluePexel <= (redPexel + tolerance + tolerance)) and (bluePexel >= (redPexel - tolerance))) and ((bluePexel <= (greenPexel + tolerance)) and (bluePexel >= (greenPexel - tolerance)))
    }
}
    
    result = np.all([pexel[2]['redPexel'],  pexel[3]['greenPexel'], pexel[4]['bluePexel']])

    if pexel[1] == True:
        print('equal')

    elif result:
        orgimage_to_ndArray_values =   orgimage_to_ndArray[0][index]
        for iter in range(0, len(orgimage_to_ndArray_values)):
            if orgimage_to_ndArray_values[iter] > 150:
                orgimage_to_ndArray[0][index] = orgimage_to_ndArray[0][index] + 50
            else:
                 orgimage_to_ndArray[0][index] = orgimage_to_ndArray[0][index] - 50

        

def contrast():
    global orgimage_to_ndArray 
    orgimage_to_ndArray = np.array(orgimage)
    for iter in range(0, len(orgimage_to_ndArray[0])):
        RGB_values = orgimage_to_ndArray[0][iter]
        redPexel = RGB_values[0]
        greenPexel = RGB_values[1]
        bluePexel = RGB_values[2]
        compare(redPexel, greenPexel, bluePexel, 3, iter, orgimage_to_ndArray)
contrast()



pyplot.subplot(1,2,1), pyplot.imshow(orgimage), pyplot.title('Orginal Image')
pyplot.subplot(1,2,2), pyplot.imshow(orgimage_to_ndArray), pyplot.title('Contrast Image')
pyplot.show()

# res = np.array_equal(orgimage_to_ndArray, orgimage)

# print(res)





