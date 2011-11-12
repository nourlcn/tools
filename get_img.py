import hashlib
import os

def get_img_url(appid):
    int_id = int(appid);
    yu = int_id%5000;
    post_fix = str(yu);
    img_url = "/srv/nfs/img/"+ post_fix + "/" + appid[:-1] + "_m.png";
    return img_url; 

def CalcMD5(filepath):
    f = file(filepath,'rb')
    if f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hashv = md5obj.hexdigest()
        return hashv
    else:
        return "000"
        
if __name__ == "__main__":
    count = 0
    appid=[]
    img=[]
    md5=[]
    fin = file('./pvsz','r')
    for x in fin:
        appid.append(x)
        img.append(get_img_url(x))
    
    for x in img:
        hashfile = x
        if not os.path.exists(hashfile):
            hashfile = os.path.join(os.path.dirname(__file__),hashfile)
            if not os.path.exists(hashfile):
                md5.append("null")
                count += 1                
            else:
                md5.append(CalcMD5(hashfile))
        else:
                md5.append(CalcMD5(hashfile))
    
    fout = file('./id_md5','w')
    
    for x in range(len(appid)-1):
        fout.write(appid[x]+md5[x]+"\n")
    
    fout.close()
    fin.close()
    
    print len(appid) - count
    print len(set(md5))
