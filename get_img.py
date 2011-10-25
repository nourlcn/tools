import hashlib
import os,sys



def get_img_url(id):
    int_id = int(id);
    yu = int_id%5000;

    post_fix = str(yu);

    img_url = "/srv/nfs/img/"+ post_fix + "/" + id[:-1] + "_m.png";
    return img_url; 
    

def CalcMD5(filepath):
    f = file(filepath,'rb')
    if f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
    else:
        return "000"
        
if __name__ == "__main__":
    count = 0
    id=[]
    img=[]
    md5=[]
    fin = file('./pvsz','r')
    for x in fin:
        id.append(x)
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
    
    for x in range(len(id)-1):
        fout.write(id[x]+md5[x]+"\n")
    
    fout.close()
    fin.close()
    
    print len(id) - count
    print len(set(md5))





