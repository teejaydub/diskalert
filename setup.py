from setuptools import setup
import os
from shutil import copyfile

try:
    input = raw_input
except NameError:
    pass

result = 0
while result == 0:
    result = input("This will install DiskAlert to your system. Do you wish to continue? (y/N):")

    if result == "" or result in "nN":
        print("Aborting Installation...")
        raise SystemExit

    elif result in "yY":
        break

    else:
        result = 0

setup(
    name="DiskAlert",
    version="0.1",
    packages=["DiskAlert"],
    license="MIT",
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts':[
            'diskalert = DiskAlert.__main__:main'
        ]
    },
)

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