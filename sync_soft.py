#!/usr/bin/env python
#encode:utf-8

import re
import os

def get_soft_list(fobject):
    list = []
    i = 0
    r = re.compile('[a-z0-9+-\.]+')
    

    for line in fobject:
	    if i < 1 and line[:2] == "ii":
		    #line = list(line)
		    #print type(line) #str
		    #print len(line)
		    print line
            i += 1
            m = r.match(line[4:])
            if m:
                #print m.group()
                list.append(m.group())
    #print list,len(list)
    return list
		
def install_soft(local,remote):
    for x in remote:
        if x in local:
            pass
        else:
            print x,"is not installed\n"
            cmd = "aptitude install " + x 
            os.system(cmd)
            
def remove_soft(local,remote):
    for x in local:
        if x in remote:
            pass
        else:
            print x," will be removed\n"
            cmd = "aptitude remove " + x 
            os.system(cmd)
    os.system('aptitude autoremove')
    os.system('aptitude autoclean')
    



if __name__ == "__main__":
    fin = file('/home/nourl/install.soft','r')
    remote_list = get_soft_list(fin)
    fin.close()    
    
    #print local_list
    install = raw_input("install remote machine soft?")
    if install:
        #print len(soft_list)
        os.popen('dpkg -l > tmp_local_soft')
        flocal = file('tmp_local_soft','r')
        local_list = get_soft_list(flocal)
        flocal.close()
        install_soft(local_list, remote_list)
        
#    remove = raw_input("remove local machine soft?")
#    if remove:
#        #print len(soft_list)
#        os.popen('dpkg -l > tmp_local_soft')
#        flocal = file('tmp_local_soft','r')
#        local_list = get_soft_list(flocal)
#        flocal.close()
#        remove_soft(local_list, remote_list)
#        
#    if install or remove:
#        os.system('rm tmp_local_soft')
    if install:
        os.system('rm tmp_local_soft')
        
    print "Done!\n Soft on your system is the same as remote machine~!\n"
    
