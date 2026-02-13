import os
import string
import sys
import edit_rw
import edit_w
if __name__== "__main__":
    if len(sys.argv) >1:
        if os.path.exists(sys.argv[0]):
            print("Message: Mode[RW]")
            pat=str(sys.argv[0])
            edit_rw.rw_file.readwrite_file(sys.argv[0])
        else:
            print("File not found.")
            exit(1)
    else:
        print("Message: Mode[W]")
        edit_w.w_file.write_file()
    exit(0)