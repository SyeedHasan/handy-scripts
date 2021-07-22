# ====================================
# title           : dumpPe.py
# description     : Parse a hex file to extract executables (personally used it on crash memory dumps)
# author          : Syed Hasan
# date            : Jan 01 2020
# usage           : sudo python3 dumpPe.py
# python_version  : 3.X
# version         : 0.1
# notes           : It's riddled with bugs - though at your discretion to be used! :)
# ====================================


fileName = str(input("Enter your filename: "))
i = 1
findCount = 1
with open(fileName, "rb") as f:
    data = f.read(8)
    fileStr = []
    while data:
        # Does this contain MZ?
        matchFound = data.find(b'\x4d\x5a')
        # If yes,
        if matchFound >= 1:

            # Don't need the junk before the MZ header
            data = data[matchFound:]
            fileStr.append(data)

            while i:
                # Found a match? Read and find more of those.
                data = f.read(8)
                secondMatch = data.find(b'\x4d\x5a')

                # If found again, you need to dump the previous found MZ.
                if secondMatch >=1:
                    findCount += 1
                    # Join the data in binary
                    instance = b''.join(fileStr)
                    newFileName = "mem-dump-" + str(findCount)
                    # Open the new file and output to it
                    with open(newFileName, "wb") as newFile:
                        print("Wrote to: ", newFileName)
                        newFile.write(instance)
                        fileStr = []
                        fileStr.append(data[secondMatch:])
                    i = 0
                else:
                    # Usual part which has to be appended with "MZ"
                    fileStr.append(data)

        # Continue reading from the files, there's no match yet.
        data = f.read(8)
        i = 1


