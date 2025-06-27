from setuptools import setup
import os
from shutil import copyfile

setup()

print("Checking if /etc/diskalert.conf exists...")
if os.path.isfile("/etc/diskalert.conf"):
    print("The file /etc/diskalert.conf exists... Not replacing it.")
else:
    if os.path.isdir('/etc'):
        copyfile('etc/diskalert.conf', '/etc/diskalert.conf')
    else:
        print("Either /etc doesn't exist, or isn't a directory. We won't force it.")

print("Installing man pages...")
try:
    copyfile('etc/diskalert.1', '/usr/share/man/man1/diskalert.1')
    os.system('mandb')
except Exception as err:
    print("Error occurred while installing man page: {0}".format(str(err)))

print("""Installation successful!
      Please check the settings in /etc/diskalert.conf so that the script will work accordingly.
      You can always check the man pages for diskalert.""")