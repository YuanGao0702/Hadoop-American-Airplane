#!/usr/bin/env python
#How many minutes total did passengers spend waiting for all late departures in 2014?
#Student: Changle Xu, Yuan Gao, Bei Xia

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split('","')
    id = words[1]
    crs = words[6]
    dep = words[7]

    if dep.strip():
        crs = int(crs)/100*60+int(crs)%100
        dep = int(dep)/100*60+int(dep)%100
        delay = dep-crs

        #Outputof mapper: the key is FL_NUM; the value is the delay whose value is larger than 0 minutes.
        if delay>0:
                print '%s\t' % id + '%d\t' % delay
~                                                                                   
