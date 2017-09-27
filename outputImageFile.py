# references:
#   PIL.Images:  http://effbot.org/imagingbook/image.htm

import PIL.Image as pil
import outputImageToConsole as out
myimage = pil.fromarray(out.np.array(out.readDataFile.train_images[3]))
myimage.show()