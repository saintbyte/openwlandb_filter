#!/usr/bin/env python
import sys
import hashlib
from orderedset import OrderedSet
from sets import Set
def help():
    print "Usage: diff.py [file1] [file2]"
    print "Search diff in two bases"
    print ""
    print ""
    print "Example: ./diff.py db1.csv db2.csv"
    quit()

def die(msg):
    print msg+"\n\n"
    quit()

def loadBssid(fh):
    fh.seek(0)
    os = Set()
    cnt=0
    for line in fh:
       cnt+=1
       if (cnt < 2):
           continue
       #%bssid   lat     lon
       try:
          (bssid,lat,lon) = line.split("\t")
          os.add(bssid)
       except:
          pass
    return os

def loadFull(fh):
    fh.seek(0)
    os = Set()
    cnt=0
    for line in fh:
       cnt+=1
       if (cnt < 2):
           continue
       #%bssid   lat     lon
       try:
          line = line.strip()
          os.add(line)
       except:
          pass
    return os

def loadToHash(fh):
    fh.seek(0)
    os=dict()
    cnt=0
    for line in fh: 
       cnt+=1
       if (cnt < 2):
           continue
       #%bssid   lat     lon
       try:
          line = line.strip()
          (bssid,lat,lon) = line.split("\t")
          os[bssid] = hashlib.md5(line).hexdigest()
       except:
          pass
    return os

def showNewAPs(fh,new_os):
    fh.seek(0)
    cnt=0
    for line in fh: 
       cnt+=1
       if (cnt < 2):
           continue
       try:
          line = line.strip()
          (bssid,lat,lon) = line.split("\t")
          if (bssid in new_os):
             print "NEW:{}".format(line)
       except:
          pass


def main():
    if (len(sys.argv) < 3):
        help()
    try:
       file1 = open(sys.argv[1])
    except:
       die("cant open "+sys.argv[1])
    try:
       file2 = open(sys.argv[2])
    except:
       die("cant open "+sys.argv[2])
    new=Set()
    deleted=Set()
    print "INFO:load "+sys.argv[1]
    file1_set = loadBssid(file1)
    print "INFO:load "+sys.argv[2]
    file2_set = loadBssid(file2)
    print "INFO:loading done"
    new = file2_set - file1_set
    deleted = file1_set - file2_set
    showNewAPs(file2,new)
    for item in deleted:
        print "DEL:{}".format(item)
    file1_set.clear()
    file2_set.clear()

    
    print "INFO:Search modify"
    print "INFO:load to Hash:"+sys.argv[1]
    file1_dict = loadToHash(file1)
    cnt=0
    file2.seek(0)
    for line in file2:
       cnt+=1
       if (cnt < 2):
           continue
       try:
          line = line.strip()
          (bssid,lat,lon) = line.split("\t")
          hashline = hashlib.md5(line).hexdigest()
          if (file1_dict[bssid] == hashline ):
              continue
          print "UPD:{}".format(line)
       except:
          pass
    
    print "INFO:Finish"

if  __name__ ==  "__main__" :
    main()
