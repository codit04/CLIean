
import apt_pkg
import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--option', help = 'Which type of content is listed')
args = parser.parse_args()

def packageCache():
    apt_pkg.init_system()

    cache = apt_pkg.Cache()
    cacheFiles = []

    for pkg in cache.packages:
        if pkg.current_state == apt_pkg.CURSTATE_INSTALLED:
            cacheFiles.append(pkg.get_fullname())
    return sorted(cacheFiles)


def crashReports():
    crash_reports = glob.glob('/var/crash/*.crash')
    return crash_reports


def appLogs():
    log_files = glob.glob('/var/log/**/*.log', recursive=True)
    logf = []
    for file in log_files:
        logf.append(file)
    return sorted(logf)

def appCache():

    dir_path = "/home"
    ac=[]
    for dirpath, dirs, files in os.walk(dir_path):
        for filename in files:
            if filename.endswith('.cache'):
                file_path = os.path.join(dirpath, filename)
                ac.append(file_path)
    return sorted(ac)

def trash():
    trash_dir = os.path.expanduser("~/.local/share/Trash/files/")
    files = os.listdir(trash_dir)
    junk=[]
    for file in files:
        junk.append(file)

    return sorted(junk)


if args.option.lower() == 'cr' :

    files = crashReports()
    if len(files) == 0  :
        print("\nNo crash reports\n\n")
    else :
       print('\nCrash reports :\n\n')
       for file in files :
           print(file)
       print()
        #print('\nCrash reports :\n', crashReports(), '\n')

elif args.option.lower() == 'al' :
    files = appLogs()
    if len(files) == 0 :
        print("\nNo app logs\n\n")
    else :
       print('\nApp logs :\n\n')
       for file in files :
           print(file)
       print()
        #print('\nApp logs :\n', appLogs(), '\n')

elif args.option.lower() == 'ac' :

    files = appCache()
    if len(files) == 0 :
        print("\nNo app cache\n\n")
    else :
       print('\nApp cache :\n\n')
       for file in files :
           print(file)
       print()
       #print("\nApp cache :\n\n", appCache(), '\n')

elif args.option.lower() == 't' :
    files = trash()
    if len(files) == 0 :
        print("\nNo trash\n\n")
    else :
       print('\nTrash :\n\n')
       for file in files :
           print(file)
       print()
       #print('\nTrash :\n', trash(), '\n')

elif args.option.lower() == 'pc' :
    files = packageCache()
    if len(files) == 0 :
        print("\nNo package cache\n\n")
    else :
       print('\nPackage cache :\n\n')
       for file in files :
           print(file)
       print()
       #print('\nPackage cache :\n', packageCache(), '\n')
