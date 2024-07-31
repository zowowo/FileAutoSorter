import os
import shutil
import pathlib
import datetime

# Directories for your source and destination folders
source_folder = 'C:\\Users\\YourUserName\\Downloads'
destination_folder_root = 'C:\\Users\\YourUserName\\Downloads'

# Feel free to add any other relevant extensions or customize the folders to your liking
extensions_dict = {
    "Images": [".png",'.jpg', '.JPG', '.raw', '.jpeg', '.gif'],
    "Audio and Video Files": ['.mp4', '.MP4', '.mp3', '.mov','.mpg','.wav','.wma','.wmv'],
    "Documents": ['.pdf', '.ppt', '.ppsx', '.pptx', '.doc', '.docx', '.txt'],
    "Spreadsheet Files": ['.csv', '.numbers', '.ods', '.xls', '.xlsx'],
    "Compression and Archive Files": ['.zip', '.7z', '.rar', '.tar'],
    "Executable Program Files": ['.app', '.bat', '.bin', '.cmd', '.com', '.exe', '.vbs', '.x86'],
    "Code": [".py", ".css", ".html", ".htm", ".js", ".php", ".cs", ".json", '.ipynb', '.sql', '.md'],
    "Misc": [".opdownload"]
}

def moveFile(fileDirectory, fileType):
    for key,values in extensions_dict.items():
        for value in values:
            if value == fileType:
                new_destination_folder = destination_folder_root + "\\" + key
                
                if key not in os.listdir(destination_folder_root):
                    os.mkdir(new_destination_folder)
                    
                source_path = os.path.join(source_folder, fileDirectory)
                destination_path = os.path.join(new_destination_folder, fileDirectory)
                shutil.move(source_path, destination_path)
                print(f"Successfully moved {fileDirectory}")

if __name__ == '__main__':
    for file in os.listdir(source_folder):
        file_extension = pathlib.Path(file).suffix

        if any(file_extension in extensions for extensions in extensions_dict.values()):
            moveFile(file, file_extension)
    
    # Optional log text file for keeping track of when this script runs
    file = open(r"C:\\Users\\YourUserName\\Desktop\\YourFolder\\file_movement_log.txt", "a")
    file.write(f'The script ran on {datetime.datetime.now()}\n')

        
            
            
            
            
    
