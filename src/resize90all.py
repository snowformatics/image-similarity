import Image
import os
import re

#pics = os.listdir("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test")
#for x in pics:
#    im = Image.open("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test\\" + x)
#    size = im.size
#    im_resize = i = im.resize(((size[0]/3), (size[1]/3)))
#    im_resize.save("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test_resize\\" + x, "JPEG")
    
project_lst = ["HS01", "HS02", "HS03", "HS04", "HS05", "HS06", "HS07", "HS08", "HS09", "HS10", "HS11", "HS12", "HS13", "HS14", "HS15", "HS16", "HS17", "HS18", "HSR01", "HSR02"]
shots = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
for project in project_lst:
    try:
        pict_lst = os.listdir("B:\\screening\\" + project + '\\cutout\\')
        for pict_id in pict_lst:
            if not re.search(r"_.jpg\Z", str(pict_id)):
                for shot in shots:
                    #os.mkdir(r"D:\Stefanie\HOST\\" + project)
                    #os.mkdir(r"D:\Stefanie\HOST\\" + project + "\\" + shot)
                    #os.mkdir(r"D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" + 'A')
                    #os.mkdir(r"D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" + 'B')
                    if shot == pict_id[0:2]:
                        im = Image.open("B:\\screening\\" + project + '\\cutout\\' + pict_id)
                        size = im.size
                        im_resize = i = im.resize(((size[0]*25/100), (size[1]*25/100)))
                        
                        if pict_id[2] == 'A':
                            im_resize.save("D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" +  "A" + "\\" + pict_id, "JPEG")
                        if pict_id[2] == 'B':
                            im_resize.save("D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" +  "B" + "\\" + pict_id, "JPEG")
                    
                    
    except WindowsError:
        pass
