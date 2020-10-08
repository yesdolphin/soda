import os, getpass
os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"')
os.system("rm -rf /Users/%s/.matplotlib"%getpass.getuser())
os.system("rm -rf /Users/%s/.pyenv"%(getpass.getuser()))
try:
  os.system("/usr/local/opt/python/libexec/bin/pip uninstall virtualenv")
except Exception as e:
  print(e)
os.system("rm -rf /Users/%s/tavern"%(getpass.getuser()))
os.system("rm -rf /Users/%s/.ipython"%(getpass.getuser()))
os.system("rm -rf /Users/%s/Library/Application\ Support/Firefox/Profiles/*.sele"%(getpass.getuser()))
os.system("sudo rm -rf /Applications/Firefox\ 67.app")
os.system("sudo rm -rf /Applications/Firefox\ 46.app")
os.system("sudo rm -rf /Applications/Google\ Chrome\ 70.app")
print("Uninstall Complete")