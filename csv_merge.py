# encoding: utf-8
__author__ = 'nourl'

import sys
import csv

def get_header(onefile):
    result = unicode("时间", 'gbk')
    content = csv.reader(file(onefile), dialect='excel')
    for x in content:
        for i in x:
            result += "," + unicode(i, 'gbk')
        break
    return result

def get_all_files(current_dir):
    import os
    return [current_dir + "/" + x for x in os.listdir(current_dir)]

def merge_file_into_dst(input_file, dst_file, prefix=None):
    index = 0
    for x in open(input_file, 'r').readlines()[1:]:
        dst_file.write(prefix+','+x)

if __name__ == '__main__':
    current_dir = sys.argv[1]
    files = get_all_files(current_dir)
    header = get_header(files[0])

    dst_file_path = "/home/nourl/contest/data" + '/' + files[0].split('_')[1][:8] + '.csv'
    dst_file = file(dst_file_path, 'w')

    for x in files:
        prefix = x.split('_')[1].split('.')[0]
        merge_file_into_dst(x, dst_file, prefix)
    dst_file.close()
#    os.remove(dst_file_path)

