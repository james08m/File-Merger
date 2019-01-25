import sys
import time



if len(sys.argv) >= 3 and len(sys.argv) <= 4:  # Must have 2 or 3 arguments passed to program
    
    file_ids = open(sys.argv[1], "r")
    file_ips = open(sys.argv[2], "r")

    if len(sys.argv) == 4:
        file_result = open(sys.argv[3], "w+")
    else:
        file_result = open("result.txt", "w+")

    ids    = []
    ips    = []
    temp   = []

    ids = file_ids.readlines()
    ips = file_ips.readlines()

    print "IDs File and IPs file merger"
    print "Loaded ids : %s" % len(ids)
    print "Loaded ips : %s" % len(ips)

    if len(ids) == len(ips):
        for line in ids:
            line = line[:2] + ';' + line[2:] # Separate Province code from site code
            line = line[:8] + ';' + line[8:] # Separate site code from till code
            line = line[:11]                 # Croped unnecessary information from line 
            temp.append(line)
        print "Created temp list : %s" % len(temp)

        i=0
        while i < len(ips):
            line = temp[i] + ';' + ips[i]    # Separate ids from ips
            file_result.write(line)          # Write result to file
            i = i+1

        
    else:
        print "Files lines amount does not match!"

    file_a.close()
    file_b.close()
    file_result.close()
else:
    print "Insufficient or too much arguments passed to program."
    print "Must at least have 2 files path and you can use a third argument to specify the result file name."
