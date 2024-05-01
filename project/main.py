import os
from functions import *

folder_path = "C://Users//ankik//OneDrive//Desktop//project//pdf_folder"

# List all files in the folder
files = os.listdir(folder_path)

priority = {
    "rape" : "1",
    "Murder" : "2",
    "domestic voilence" : "3",
    "civil" : "4",
    "divorce" : "5",
    "Settelment" : "6"
}
# Iterate over each file
# for file_name in files:
#     file_path = os.path.join(folder_path, file_name)
#     summary = summarizer(file_path)
#     category = categorizer(summary)
#     new_name = priority[category]
    
#     # Generate the new full path including the new file name
#     new_file_path = os.path.join(folder_path, new_name + ".pdf")
    
#     # Rename the file
#     os.rename(file_path, new_file_path)

# file_path = os.path.join(folder_path, "5.pdf")
# new_file_path = os.path.join(folder_path, "6" + ".pdf")
# os.rename(file_path, new_file_path)


for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    summary = summarizer(file_path)
    category = categorizer(summary)
    
    new_file_name = priority[category] + ".pdf"
    new_file_path = os.path.join(folder_path, new_file_name)

    os.rename(file_path, new_file_path)
    print(file_name + " -> " + new_file_name + " -> " + category)
