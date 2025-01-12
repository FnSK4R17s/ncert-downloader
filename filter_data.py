'''
script to copy the files from the pdf_list_ceaned.csv file to a post+process folder

the csv contains the following columns:
    "Standard", "Subject", "File Name", "File Path", "language"
'''

import os
import pandas as pd
import shutil

folder_path = "merged_pdfs"

csv_filename = "pdf_list_cleaned.csv"
output_folder = "post_processed"

df = pd.read_csv(csv_filename)

for index, row in df.iterrows():
    file_path = row["File Path"]
    file_name = row["File Name"]
    output_path = file_path.replace(folder_path, output_folder)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    shutil.copy(os.path.join(file_path, file_name), output_path)
    print("Copied: ", file_name, " to ", output_path)
print("Done copying files to post_processed folder")

