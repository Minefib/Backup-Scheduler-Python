import shutil
import sys
import schedule
import time
import os
from datetime import datetime


def filebackup():
    mainfile = input("Enter the path of the file to back up: ")
    backupfolder = input("Enter the folder to save backups in: ")

    if mainfile == "" or backupfolder == "":
        sys.exit("Error: you must enter a path!")
    elif not os.path.isfile(mainfile):
        sys.exit(f"Error: '{mainfile}' is not a file or does not exist!")
    elif not os.path.isdir(backupfolder):
        sys.exit(f"Error: the folder '{backupfolder}' does not exist!")
    else:
        def backupcopy():
            backupfile = os.path.basename(mainfile)
            stamp = f"{datetime.now():%d-%m-%Y_%H-%M-%S}"
            newname = f"{stamp}_{backupfile}"
            fullpath = os.path.join(backupfolder, newname)
            
            try:
                shutil.copy2(mainfile, fullpath)
                print(f"Backed up to {fullpath}")
            except OSError as e:
                print(f"Backup failed: {e}")


        schedule.every(15).seconds.do(backupcopy)

def dirbackup():
    maindir = input("Enter the path of the folder to back up: ")
    askdir = input("Enter the folder to save backups in: ")

    if maindir == "" or askdir == "":
        sys.exit("Error: you must enter a path!")
    elif not os.path.isdir(maindir):
        sys.exit(f"Error: the folder {maindir} does not exist!")
    elif os.path.abspath(askdir).startswith(os.path.abspath(maindir)):
        sys.exit("Error: the backup folder cannot be inside the folder you are backing up!")
    else:
         def backupcopy():
            name = os.path.basename(os.path.normpath(maindir))
            stamp = f"{datetime.now():%d-%m-%Y_%H-%M-%S}"
            newname = f"{stamp}_{name}"
            fullpath = os.path.join(askdir, newname)

            
            try:
                shutil.copytree(maindir, fullpath, dirs_exist_ok=True)
                print(f"Backed up to {fullpath}")
            except OSError as e:
                print(f"Backup failed: {e}")


         schedule.every(15).seconds.do(backupcopy)

userchoose = input("Back up a file (1) or a folder (2)? ")

if userchoose == "1":
        filebackup()
elif userchoose == "2":
        dirbackup()
else:
    sys.exit(f"Error: please enter 1 or 2!")

print("Backup running. Press Ctrl+C to stop.")
try:
    while True:
            schedule.run_pending()
            time.sleep(1)
except KeyboardInterrupt:
    print("Backup stopped.")


        




