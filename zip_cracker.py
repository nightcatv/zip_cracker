import zipfile
import optparse
import time
import os

def extractFile(toPath, zFile, password):
    try:
        zFile.extractall(path = toPath, pwd = password)
        return True
    except Exception:
        return False

def main():
    parser = optparse.OptionParser("[+]Usage: %prog -f <zipFile> -d <dictFile>")
    parser.add_option("-f", dest = "zname", type = "string", help = "specify zip file")
    parser.add_option("-d", dest = "dname", type = "string", help = "specify dict file")
    (options, args) = parser.parse_args()
    if(options.zname == None) or (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        zFile = zipfile.ZipFile(zname)
        passFile = open(dname)
        for password in passFile.readlines():
            start = time.clock()
            password = password.strip("\n")
            guess = extractFile("./", zFile, password)
            if guess:
                end = time.clock()
                print("KEY FOUND!!")
                print("The password is " + password)
                print("Execution time: " + str(end - start) + "s")
                print()
                print("Extracting the file to './' ...")
                print("Complete!!")
                os.popen('M3554C-3.txt')
                exit(0)

if __name__ == "__main__":
    main()