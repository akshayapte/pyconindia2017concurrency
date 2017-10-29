import os
import hashlib
import sys

# ddbd8937e3ea972c806893273f4c667f

def detect(folder, inhash):

    for root,dirs,files in os.walk(folder):
        for f in files:

            fpath = root + '/' + f
            try:
                data = open(fpath, 'rb').read()
            
                fhash = hashlib.md5(data).hexdigest()
                if fhash == inhash:
                    print('Found =>',fpath)
                    return fpath

            except Exception as e:
                print('Error processing filepath=>',fpath,'=>',e)
                

if __name__ == "__main__":
    detect(sys.argv[1], sys.argv[2])
