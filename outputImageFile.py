# references:
#   PIL.Images(fromarray, convert, save etc.):
#   http://effbot.org/imagingbook/image.htm

import PIL.Image as pil
import outputImageToConsole as out
myimage = pil.fromarray(out.np.array(out.readDataFile.train_images[3]))
mylabel = out.readDataFile.train_labels[3]
# convert image
myimage = myimage.convert('RGB')
myimage.show()
myimage.save('images/train-0003-1.png')