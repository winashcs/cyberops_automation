import cx_Freeze
import sys
import os 

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ashwi\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ashwi\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("ca.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name="CyberOps Automation",
    options={"build_exe": {"packages": ["tkinter", "os"], "include_files": [(os.path.join(os.path.dirname(__file__), "record.txt"), "record.txt"),"icon.ico", "images"]}},
    version="1.0",
    description="A software for automating cybersecurity operations.",
    executables=executables
)