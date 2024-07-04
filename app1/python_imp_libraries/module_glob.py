import glob

myfiles = glob.glob("../textfile_b_example/*txt")
print(myfiles)
'''for i in myfiles:
    with open(i, "r") as f:
        print(f.read())'''
