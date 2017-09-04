#!/usr/bin/python
i=0
j=0
while i <9:
    i += 1
    while j<9:
        j += 1
        print "%s*%s=%s"  %   (j,i,j*i),
        if i==j:
            j=0
            print("-")
            break
