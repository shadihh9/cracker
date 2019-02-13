# By ahmad alassaf
import time # Time spent
import zipfile # open and extract files
import os.path # check if file exists
from optparse import OptionParser # user inputs
parser = OptionParser("""


__    __      __   __        __        ___  __  
 / | |__)    /  ` |__)  /\  /  ` |__/ |__  |__) 
/_ | |       \__, |  \ /~~\ \__, |  \ |___ |  \ 
                                                 

[Author => theviperxxsy]

[-h or --help] for more options
""")
#zip file [required]
parser.add_option('-f','--zf',dest='zf',type='string',help='zipfile location')
#password list [required]
parser.add_option('-l','--pl',dest='pl',type='string',help='password list file location')
(options,args) = parser.parse_args()
if options.zf == None or options.pl == None:
    print(parser.usage)
    exit(0)
else:
    zip_file = options.zf # zip file
    pl_file = options.pl # password list file
    start_time = time.time()
    #check is file exists 
    if os.path.isfile(zip_file) == True and os.path.isfile(pl_file) == True:
        print("the time is {0}".format(time.ctime(start_time)))
        open_pl = open(pl_file,'r') # open password list
        for password in open_pl.readlines():
            try:
                password = password.rstrip("\n") # strip newline
                zf = zipfile.ZipFile(zip_file,'r') # open zip file reading mode
                zf.extractall(pwd=password.encode("utf-8")) # extract all files 
            except RuntimeError: # if password not matched
                print("password not matched {0}".format(password))

            else:
                print("the password is {0}".format(password))
                print("finshed time is {0}".format(time.ctime(time.time() - start_time)))
                exit(0)
        print("finshed time is {0}".format(time.ctime(time.time() - start_time)))
    else:
        print("zipfile or wordlist file location not found !")
