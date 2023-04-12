from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from PMTools import *

# Access to system commands
import sys

#import subprocess
if pkgIsInstalled("neofetch"):
	PM("install", "lolcat")

app = QApplication(sys.argv)

requirmentList = {
	"Session_Type" : [
		(commandOutput("echo $XDG_SESSION_TYPE") == "wayland"),
		commandOutput("echo $XDG_SESSION_TYPE"),
		commandOutput("echo $XDG_SESSION_TYPE")
	],

	"Waydroid_Package": [
		pkgIsInstalled("waydroid"),
		"Installed",
		"Not Installed"
	],

	"Binder_Module": [
		commandOutput("""
			if lsmod | grep -wq "binder"; then
				echo True
				exit 0
			else
				echo False
				exit 0
			fi
		"""),
		"Loaded",
		"Not Loaded"
	],

	"Ashmem_Module": [
		commandOutput("""
			if lsmod | grep -wq "ashmem"; then
				echo True
				exit 0
			else
				echo False
				exit 0
			fi
		"""),
		"Loaded",
		"Not Loaded"
	],

	#"Anbox_Modules_DKMS": [
	#	pkgIsInstalled("")
	#]
}

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Waydroid Manager PySide")

		# Layout of top widget
		rootLayout = QVBoxLayout()

		# Top widget contains everything else in the page
		rootWidget = QWidget()
		rootWidget.setLayout(rootLayout)

		androidOptionsLayout = QVBoxLayout()
		androidOptions = QGroupBox()
		androidOptions.setTitle("Android Options")

		androidOptions.setLayout(androidOptionsLayout)

		GappsOptions = ButtonGroup(["Google apps", "Open Gapps", "FOSS alternatives"], QRadioButton, QHBoxLayout(), "Gapps")
		androidOptionsLayout.addWidget(GappsOptions)

		requirmentsLayout = QVBoxLayout()
		requirments = QGroupBox()
		requirments.setTitle("Requirments")

		requirments.setLayout(requirmentsLayout)
		requirments.setObjectName("requirments")

		rootLayout.addWidget(androidOptions)
		rootLayout.addWidget(requirments)

		rootLayout.addWidget(QPushButton("Install"))

		self.setCentralWidget(rootWidget)

		def checkRequirments():
			for key in requirmentList.keys():
				name = key.replace("_", " ")
				requirment = QLabel()

				if((requirmentList[key][0]) == True):
					requirment.setText(f"{name} : {requirmentList[key][1]}")
					requirment.setStyleSheet("QLabel{color: green;}")
				else :
					requirment.setText(f"{name} : {requirmentList[key][2]}")
					requirment.setStyleSheet("QLabel{color: red;}")

				requirmentsLayout.addWidget(requirment)

		checkRequirments()

# Function to create groups of pushButtons, radioButtons, and other types.
def ButtonGroup(buttons, btnsType, layout, name):

	btnGroupLayout = layout
	btnGroupContainer = QGroupBox()
	btnGroupContainer.setTitle(name)
	btnGroup = QButtonGroup()

	for button in buttons:
		btn = btnsType(button)
		btnGroup.addButton(btn)

	for button in btnGroup.buttons():
		btnGroupLayout.addWidget(button)

	btnGroupContainer.setLayout(btnGroupLayout)
	btnGroup.buttons()[0].toggle()

	return btnGroupContainer

# Set main window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec_()
