import Image
import PIL as pil
from scipy import stats as P

im1 = "09B_084_01.jpg"
im2 = "09B_085_01.jpg"
im3 = "2-3.jpg"
im4 = "belichtung1.jpg"
im5 = "belichtung2.jpg"
im6 = 'unterschiedlich1.jpg'
im7 = 'unterschiedlich2.jpg'

f = open('pearson1.txt', 'w')
f2 = open('pearson2.txt', 'w')

im = Image.open(im1)
im = im.resize((50, 200))
data = list(im.getdata())
lst1 = []
for i in data:
    lst1.append(i[0])
    f.write(str(i[0]) + '\n')

im2 = Image.open(im3)
im2 = im2.resize((50, 200))
data2 = list(im2.getdata())
lst2 = []
for i2 in data2:
    lst2.append(i2[0])
    f2.write(str(i2[0]) + '\n')

print P.pearsonr(lst1, lst2)