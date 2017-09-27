# references:
#   PIL.Images(fromarray, convert, save etc.):
#   http://effbot.org/imagingbook/image.htm

import PIL.Image as pil
import outputImageToConsole as out
def outImages(type):
    if(type == 'test'):
        for i in range(len(out.readDataFile.test_images)):
            myimage = pil.fromarray(out.np.array(out.readDataFile.test_images[i]))
            mylabel = out.readDataFile.test_labels[i]
            # convert image
            myimage = myimage.convert('RGB')
            # save image
            imagename = 'test_images/test-'+str(i)+'-'+str(mylabel)+'.png'
            myimage.save(imagename)
    if(type == 'train'):
        for i in range(len(out.readDataFile.train_images)):
            myimage = pil.fromarray(out.np.array(out.readDataFile.train_images[i]))
            mylabel = out.readDataFile.train_labels[i]
            # convert image
            myimage = myimage.convert('RGB')
            # save image
            imagename = 'train_images/train-'+str(i)+'-'+str(mylabel)+'.png'
            myimage.save(imagename)

outImages('test')
outImages('train')