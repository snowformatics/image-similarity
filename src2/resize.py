import Image
import os

pics = os.listdir("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test")
for x in pics:
    im = Image.open("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test\\" + x)
    size = im.size
    im_resize = i = im.resize(((size[0]/3), (size[1]/3)))
    im_resize.save("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test_resize75\\" + x, "JPEG")