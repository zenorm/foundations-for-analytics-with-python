import os
import sys
import glob

print("output #145:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
    with open(input_file,'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
