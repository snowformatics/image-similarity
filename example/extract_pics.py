import shutil



f = open('pic.txt', 'r')
pics = f.readlines()

imag = set()
for pic in pics:
    pic = pic.strip()
    imag.add(pic)
    
for im in imag:
    nr = im[0:2]
    letter = im[2]
    print letter
    shutil.copyfile('D:\\Eigene Datein\\Python\\Image Similarity\\example\\HS01\\' + str(nr) + '\\' + str(letter) + '\\' + im, 
                    'D:\\Eigene Datein\\Python\\Image Similarity\\example\\HS01_select\\' + im)
    