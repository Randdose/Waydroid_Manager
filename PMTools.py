from SysTools import *
from sys import argv

# Package Managers //ToDo: add zypper, XBPS, and other PMs
PackageManagers = {
	"pacman": {
		"install": lambda pkg : runCommand(f"pacman -S {pkg}", 1),
		"remove": lambda pkg : runCommand(f"sudo pacman -Rns {pkg}", 1),
		"update": lambda : runCommand("sudo pacman -Syu", 1)
	},
	"apt": {
		"install": lambda pkg : runCommand(f"sudo apt install {pkg}", 1),
		"remove": lambda pkg : runCommand(f"sudo apt remove {pkg}", 1),
		"update": lambda : runCommand("sudo apt update; apt upgrade", 1)
	},
	"dnf": {
		"install": lambda pkg : runCommand(f"sudo dnf install {pkg}", 1),
		"remove": lambda pkg : runCommand(f"sudo dnf remove {pkg}", 1),
		"update": lambda : runCommand("sudo dnf update", 1)
	}
}

# Gets the name of the system's package manager
def getPackageManager():
	for i in PackageManagers.keys():
		if (pkgIsInstalled(i)):
			return i

packageManager = getPackageManager()

#def PMInstall(pkg):


def PM(instruction, argv):
	PackageManagers[packageManager][instruction]
