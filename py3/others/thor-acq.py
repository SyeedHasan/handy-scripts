import os
import re
import shutil
import argparse
import tarfile

def tarFiles(dstDir):
    with tarfile.open("ThorResults.tgz", "w:gz" ) as tar:
        for name in os.listdir(dstDir):
            tar.add(dstDir+name)
    
    print("[+] Successfully zipped the files")

def getAlertMatches(logfile):
    potentialMalFiles = []
    with open(logfile, 'r') as fileObj:
        lines = fileObj.readlines()
        for line in lines:
            if re.search('Alert', line) is not None:
                filePath = re.search('(?<=FILE)(.*?)(?=EXT)', line).groups()[0]
                filePath = filePath.lstrip(': ')
                potentialMalFiles.append(filePath)

    if len(potentialMalFiles) >= 1:
        print("[+] Resulting Files: ", len(potentialMalFiles))
        return potentialMalFiles
    else:
        print("[*] No alerts found?! Clean as a whistle.")
        print("[*] Quitting now!")
        os._exit(1)

def copyMalFiles(opDir, fileList):
    successes = 0
    for fileObj in fileList:
        try:
            shutil.copyfile(fileObj, f"{opDir}\\{os.path.split(fileObj)[1]}")
            print(f"[+] Successfully copied the file: {fileObj}")
            successes += 1
        except PermissionError:
            print(f"[-] You don't hold the necessary privileges to copy the file: {fileObj}")
        except FileNotFoundError:
            print(f"[-] Could not locate the file: {fileObj}")

    if successes == 0:
        print("[-] No file could be located. Quitting now.")
        os._exit(1)

def parseArgs():
    ap = argparse.ArgumentParser(description="Acquire files which raise an 'ALERT' in THOR", epilog="Good, wasn't it?!")

    ap.add_argument("--file", metavar="File to scan", required=True, help="File to scan")
    ap.add_argument("--opdir", metavar="Output Directory", required=True, help="Output directory for the files to be copied")

    args = vars(ap.parse_args())
    return args

def main():
    print('''
    THOR File Acquisition
    Written by: Syed Hasan
    ''')
    args = parseArgs()


    if os.path.exists(args['opdir']):
        print("[+] Output directory exists. All good.")
    else:
        print("[-] Incorrect output directory. Mind re-running me with a correct path?!")
        os._exit(0)

    fileList = getAlertMatches(args['file'])
    copyMalFiles(args['opdir'], fileList)
    tarFiles(args['opdir'])

if __name__ == "__main__":
    main()