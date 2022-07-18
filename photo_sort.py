import os
import shutil

os.chdir('Photo_and_Video')

for dir in os.listdir():  # Choose a folder
    try:
        os.chdir(dir)  # Entering the folder
        for file in os.listdir():  # Choose a file
            if file.endswith('.jpg'):  # Checking compliance
                collection = file[2:6]  # To sort by month and year in new folder
                collection_dir = '../../Just Photo/' + collection  # Sorted folders
                if not os.path.exists(collection_dir):  # Checking folder exists
                    os.mkdir(collection_dir)  # Create a folder
                shutil.copy2(file, collection_dir)  # Copying file
        os.chdir('..')  # exit the folder
    except NotADirectoryError:
        pass
