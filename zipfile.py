import zipfile

z = zipfile.ZipFile('./test.zip','r')

for x in z.namelist():
    print x,
    content = z.read(x)
    print "Content",content
