fileName = str(input("Enter the filename: "))
newFile = f"{fileName}.bin"

with open(fileName, 'r') as fileHandle:

	print(f"Acquired a handle to: {fileHandle.name}")
	content = fileHandle.readlines()

	hexStrings = content[0]

	asciiStrings = bytes.fromhex(hexStrings)
	print(f"Converted Hex to Bytes")

	with open(newFile, 'wb') as newFile:
		newFile.write(asciiStrings)
		print(f"Successfully wrote the file to disk, {newFile.name}")