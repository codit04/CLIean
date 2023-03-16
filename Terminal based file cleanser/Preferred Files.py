import apt_pkg
import glob
import os


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
