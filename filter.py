#!/usr/bin/env python
import sys
def help():
    print "Usage: filter.py [src_file] [dest_file] [bounds]"
    print "Bounds: minlat,minlon,maxlat,maxlon. Example bounds: 55.875,57.041,62.042,66.445"
    print "Use - as dest_file for output to stdout"
    print ""
    print "Example: ./filter.py cell_towers.csv RU-SVE.csv 55.875,57.041,62.042,66.445"
    quit()

def die(msg):
    print msg+"\n\n"
    quit()

def in_bounds(lat,lon,minlat,minlon,maxlat,maxlon):
    lat = float(lat)
    lon = float(lon)
    minlat = float(minlat)
    minlon = float(minlon)
    maxlat = float(maxlat)
    maxlon = float(maxlon)
    if (minlat<lat and minlon<lon and maxlat> lat and maxlon>lon):
        return True
    else:
        return False

def main():
    if (len(sys.argv) < 4):
        help()
    try:
       src_fl = open(sys.argv[1])
    except:
       die("cant open src_file")
    if (sys.argv[2] != "-"):
         dest_fl= open(sys.argv[2],'w')
    (minlat,minlon,maxlat,maxlon) = sys.argv[3].split(',')
    print "INPUT:SRC_FILE:%s"%sys.argv[1]
    print "INPUT:DEST_FILE:%s"%sys.argv[2]
    print "INPUT:BOUNDS:%s %s %s %s"%(minlat,minlon,maxlat,maxlon)
    cnt=0
    af_cnt=0
    for line in src_fl:
       cnt+=1
       if (cnt < 2):
           continue
       #%bssid   lat     lon
       (bssid,lat,lon) = line.split("\t")
       print bssid
       if (in_bounds(lat,lon,minlat,minlon,maxlat,maxlon)):
           af_cnt+=1
           if (sys.argv[2] != "-"):
               dest_fl.write(line)
           else:
               print line
    print "STAT: count of lines: %i"%cnt
    print "STAT: count of affected lines: %i"%af_cnt

if  __name__ ==  "__main__" :
    main()
