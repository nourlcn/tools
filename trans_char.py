str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

url="http://www.pythonchallenge.com/pc/def/map.html"

newstr=""

for x in url:
    if ord(x) != 32 and ord(x)<= 120 and ord(x) >=97:
        newstr += chr(ord(x)+2)
    elif ord(x) > 120 and ord(x) <=122:
        newstr += chr(97+ord(x)-121)
    else:
        newstr += x

print newstr
        
