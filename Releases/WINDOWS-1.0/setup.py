import sys
from cx_Freeze import *

#python setup.py bdist_msi

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files": ["Scripts", "DatFiles", "d20.ico"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "FantasyBoardGamesTools",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]FantasyBoardGamesTools.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}


setup(  name = "FantasyBoardGamesTools",
        version = "1.0",
        description = "Fantasy Board Games Tools for Masters",
        options = {"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
        executables = [Executable("FantasyBoardGamesTools.py", base=base)])