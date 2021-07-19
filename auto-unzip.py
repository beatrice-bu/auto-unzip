import zipfile
from glob import glob as folders

for index, folder in enumerate(folders("./" + "*.zip")):
    with zipfile.ZipFile(folder, "r") as zippedFolder:
        print(f"{index} - Unzipping: {folder}...") 
        folderNameWithoutDotZip = folder[:-4]
        zippedFolder.extractall("./" + folderNameWithoutDotZip)

