from SysTools import *
from sys import argv

# Package Managers //ToDo: add zypper, XBPS, and other PMs
PackageManagers = {
	"pacman": {
		"install": lambda pkg : runCommand(f"sudo pacman -S {pkg}"),
		"remove": lambda pkg : runCommand(f"sudo pacman -Rns {pkg}"),
		"update": lambda : runCommand("sudo pacman -Syu")
	},
	"apt": {
		"install": lambda pkg : runCommand(f"sudo apt install {pkg}"),
		"remove": lambda pkg : runCommand(f"sudo apt remove {pkg}"),
		"update": lambda : runCommand("sudo apt update; apt upgrade")
	},
	"dnf": {
		"install": lambda pkg : runCommand(f"sudo dnf install {pkg}"),
		"remove": lambda pkg : runCommand(f"sudo dnf remove {pkg}"),
		"update": lambda : runCommand("sudo dnf update")
	}
}

# Gets the name of the system's package manager
def getPackageManager():
	for i in PackageManagers.keys():
		if (pkgIsInstalled(i)):
			return i

packageManager = getPackageManager()

def PM(instruction, argv):
	PackageManagers[packageManager][instruction](argv[0])
