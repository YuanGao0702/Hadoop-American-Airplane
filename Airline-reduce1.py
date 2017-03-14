#!/usr/bin/env python
#Student: Changle Xu, Yuan Gao, Bei Xia
#What is the percentage departures later than 5 minutes from every airport?

from operator import itemgetter
import sys

current_airport = ""
airport = ""
total = 0
delay = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    count = line.split('""')
    #Input of the reducer: the ORIGIN_CITY_NAME is the key; The value is the delay whose value is 0 or 1.
    airport = count[0]

    count = int(count[1])

    if current_airport == airport:
        if count == 1:
                delay += 1
                total += 1
        else:
                total += 1
    else:
        if not total == 0:
                percentage = float(delay)/float(total)*100
                #Output of the reducer: the ORIGIN_CITY_NAME is the key; the value is the percentage departures later than 5 minutes from every airport.
                print "Airport: "+'%s\t' % (current_airport)+ " The percentage: %.2f" % percentage + "%"
        current_airport = airport
        if count ==1:
                delay +=1
                total +=1
        else:
                total+=1
