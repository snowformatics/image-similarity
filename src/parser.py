import os

#os.chdir("D:\Stefanie\1run\\")
f = open('D:\\Stefanie\\2run\\outHSR02.txt', 'r')
data = f.readlines()
out = open('D:\\Stefanie\\2run\\outHSR02_80percent.txt', 'w')
out_html = open('D:\\Stefanie\\2run\\outHSR02_80percent.html', 'w')
out_html.write('<html>' + '\n' + '<head>' + '\n ' + '<title> Cell comparator</title>'
+ '\n' + '</head>' + '\n' + '<body>' + '\n\n' + 'Compares identical cells' + '\n\n' +
'</body>' + '\n' + '</html>' + '\n\n' + '<table border="1"  width="800">' + '\n' + 
'<tr><th>Picture1</th><th>R75</th><th>Picture2</th></tr>' + '\n')
le = open('D:\\Stefanie\\2run\\len.txt', 'w')
liste = []
nr = 0

for line in data:
    
    line = line.split('\t')
    if line[1] == line[2]:
        base = line[3]
    percent = float(line[3])*100/float(base)
    if percent > 80: 
        line[3] = line[3].replace('\n', '')
        line[1] = line[1].replace('\n', '')
        line[2] = line[2].replace('\n', '')
        if line[1] == line[2]:
            le.write(line[1] + line[2] + '\n')
        else:
            percent = round(percent, 2)
            out.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3] + '\t' + str(percent) + '\n')
            #out_html.write('<tr><td align="right"><img src="B:\screening\HS01\cutout\\' + line[1] + '" /></td>    <td>' + str(percent) + '</td>    <td align="left"><img src="B:\screening\HS01\cutout\\' + line[2] + '" /></td></tr>' + '\n')
            liste.append((percent, '<tr><td align="right"><img src="http://blumeria.ipk-gatersleben.de/HSR02/cutout/' + 
                          line[1] + '" /></td>    <td>' + str(percent) + 
                          '</td>    <td align="left"><img src="http://blumeria.ipk-gatersleben.de/HSR02/cutout/' +
                           line[2] + '" /></td></tr>' + '\n'))
    if percent > 85: 
        if line[1] != line[2]:
            nr = nr + 1
            print nr
liste.sort(reverse=True)
for i in liste:
    out_html.write(i[1])
#print liste
out.close()
le.close()
        