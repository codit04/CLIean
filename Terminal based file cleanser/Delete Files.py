import apt_pkg
import glob
import os
import argparse
import subprocess
import sys
import stat

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


if args.option.lower() == 'dcr' :

	files = crashReports()

	if len(files) == 0 :
		print("\nNo crashreports\n\n")

	else :
		for file in files :
			os.remove(file)
			print(f"{file} has been deleted.")

		print("\n" + str(len(files)) + " has been deleted\n")
			#print('\nCrash reports :\n', crashReports(), '\n')

elif args.option.lower() == 'dal' :
	files = appLogs()

	if len(files) == 0 :
		print("\nNo applogs\n\n")

	else :
		#sudo_password = input("Enter your sudo password : ")
		#sudo_command = f"echo {sudo_password} | sudo -S python3 {__file__}"
		#subprocess.call(sudo_command, shell = True)
		for file in files :
			subprocess.call(['chmod', '0444', file])
			#os.chmod(file, stat.S_IRWXU)
			os.remove(file)
			print(f"{file} has been deleted.")

		print("\n" + str(len(files)) + " has been deleted\n")

		#print('\nApp logs :\n', appLogs(), '\n')

elif args.option.lower() == 'dac' :

	files = appCache()

	if len(files) == 0 :
		print("\nNo appcache\n\n")

	else :
		for file in files :
			os.remove(file)
			print(f"{file} has been deleted.")

		print("\n" + str(len(files)) + " has been deleted\n")

		#print("\nApp cache :\n\n", appCache(), '\n')

elif args.option.lower() == 'dt' :

	files = trash()

	if len(files) == 0 :
		print("\nNo trash\n\n")

	else :
		for file in files :
			os.remove(file)
			print(f"{file} has been deleted.")

		print("\n" + str(len(files)) + " has been deleted\n")

		#print('\nTrash :\n', trash(), '\n')

elif args.option.lower() == 'dpc' :

	files = packageCache()

	if len(files) == 0 :
		print("\nNo packagecache\n\n")

	else :
		for file in files :
			os.remove(file)
			print(f"{file} has been deleted.")

		print("\n" + str(len(files)) + " has been deleted\n")

		#print('\nPackage cache :\n', packageCache(), '\n')



'''# specify the file path
file_path = '/home/dell/.config/libreoffice/4/user/store/.templdir.cache'

# check if file exists before deleting it
if os.path.isfile(file_path):
	os.remove(file_path)
	print(f"{file_path} has been deleted.")
else:
	print(f"{file_path} does not exist.")'''
