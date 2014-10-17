#!/usr/bin/env python
import sys
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
    for item in new:
        print "NEW:{}".format(item)
    for item in deleted:
        print "DEL:{}".format(item)
    file1_set.clear()
    file2_set.clear()

    print "INFO:Search modify"
    print "INFO:load full"+sys.argv[1]
    file1_set = loadFull(file1)
    print "INFO:load full"+sys.argv[2]
    file2_set = loadFull(file2)
    print "INFO:loading done"
    modi = file2_set - file1_set
    for item in modi:
        print "MOD:{}".format(item)

if  __name__ ==  "__main__" :
    main()
