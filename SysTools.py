import subprocess

# Returns the output of a given Bash command
def commandOutput(command):
	return ((subprocess.check_output(command, shell=True)).decode())[:-1]

# Runs a Bash command
def runCommand(command, priv=0):
	if (priv==1):
		subprocess.run(f"pkexec {command}", shell=True)
	else:
		subprocess.run(command, shell=True)

# Checks if a package is installed
def pkgIsInstalled(pkgName):
	try:
		return not(commandOutput(f"which {pkgName}") == f"{pkgName} not found")
	except:
		return False
