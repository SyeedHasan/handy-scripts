
# ====================================
# title           : importsEnum.py
# description     : Enumerate imports in a PE file
# author          : Syed Hasan
# date            : Jan 03 2020
# usage           : sudo python3 importsEnum.py
# python_version  :3.X
# ====================================

import pefile
import sys
from pprint import pprint

suspectedFile = sys.argv[1]
PE_HEADER = pefile.PE(suspectedFile)
if hasattr(PE_HEADER, "DIRECTORY_ENTRY_IMPORT"):
    for entry in PE_HEADER.DIRECTORY_ENTRY_IMPORT:
        importList = []
        print("Import Entry:", entry.dll.decode('utf-8'))
        for imp in entry.imports:
            if imp.name != None:
                importList.append(imp.name.decode('utf-8'))
            else:
                importList.append(imp.ordinal)
        print(importList)
        print()