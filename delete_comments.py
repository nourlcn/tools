#Author: nourlcn AT Gtalk
#Protocol/License:creativecommons.org/licenses/by-nc-sa/2.5/cn/

#http://weibo.com/nourl
#http://t.qq.com/nourlcn


import re
import os

def get_input_files():
    base_path = os.getcwd()
    input_path = base_path + "/input"
    #print input_path
    #os.chdir(input_path)
    files = os.listdir(input_path)
    # print files
    
    return input_path,files

def get_output_path():
    base_path = os.getcwd()
    if not os.path.exists(base_path + '/output'):
        os.mkdir(base_path + '/output')
    return base_path + '/output'
    

def delete_comments(in_path, in_file,out_path):
    input_file_name = in_path + '/' + in_file
    #print "current file name is ", input_file_name
    finput = file(input_file_name,'r+')
    foutput = file(out_path + '/' + in_file, 'w+')
              
    
    pattern1 = re.compile('//.*')
    pattern2 = re.compile('/\*.*\*/')
    pattern2_start = re.compile('/\*.*')
    pattern2_end = re.compile('.*\*/')
    
    
    multiline_comment = False
    mc = multiline_comment
  
    
    for line in finput:
        #print "Len of line is ",len(line)
        #len(line) represent length of single line
        m = pattern1.search(line)
        if m:
            start = m.start()
            #print "start is",start
            line = line[:start] + '\n'
            
        m = pattern2.search(line)
        if m:
            start = m.start()
            end = m.end()
            #print "start,end",start,end
            line = line[:start] + line[end:]   
            
        m = pattern2_start.search(line)
        if m:
            start = m.start()
            line = line[:start]
            mc = True
        m = pattern2_end.search(line)
        if m:
            end = m.end()
            line = line[end:]
            mc = False
        else:
            if mc == True:
                line = ""     
                     
        if line:
            foutput.write(line)
        
    finput.close()
    foutput.close()
        

if __name__ == "__main__":
    (in_path, files) = get_input_files() 
    out_path = get_output_path()
  
    for one_file in files:
        delete_comments(in_path, one_file, out_path)

