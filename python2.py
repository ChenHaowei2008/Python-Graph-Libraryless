# -*- coding: utf-8 -*-
from __future__ import with_statement
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import sys
from io import open
def plotGraph(yDataArray, xDataArray, accuracy):
    height = yDataArray
    height = max(height)
    height = round(height, -len(unicode(height)) + 1)
    for i in xrange(accuracy + 1):
        segment = int(height/accuracy*(accuracy - i))
        print unicode(segment) + u" " * (len(unicode(height)) - len(unicode(segment))) + u"|",; sys.stdout.write( u"")
        for y in yDataArray:
            if(y >= segment):
                print u"█",
            else:
                print u" ",
        print

with open(u"data.txt") as f:
    data = f.read().splitlines()

xData = [int(x.split()[0]) for x in data]
yData = [int(y.split()[1]) for y in data]
    
plotGraph(yData, xData, 60)