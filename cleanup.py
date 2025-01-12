import os
import pandas as pd

folder_path = "merged_pdfs"
csv_filename = "pdf_list.csv"

pdf_files = []
pdf_paths = []
standards = []
subjects = []
for root, _, files in os.walk(folder_path):
    for file in files:
        _, standard, subject = str(root).split("\\")
        pdf_files.append(file)
        pdf_paths.append(root)
        standards.append(int(standard))
        subjects.append(subject)

df = pd.DataFrame({
    "Standard": standards,
    "Subject": subjects,
    "File Name": pdf_files,
    "File Path": pdf_paths,
    "language": "n/a",
})

# sort the dataframe by standard and subject
df = df.sort_values(by=["Standard", "Subject"])

df.to_csv(csv_filename, index=False)