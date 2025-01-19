import os
import shutil

def export_text_files(source_folder="cleaned_data", destination_folder="exports"):
    os.makedirs(destination_folder, exist_ok=True)
    for root, _, files in os.walk(source_folder):
        for file_name in files:
            if file_name.lower().endswith(".txt"):
                new_name = root.replace("\\", "_").replace("/", "_").replace(":", "_") + "_" + file_name
                shutil.copy(os.path.join(root, file_name), os.path.join(destination_folder, new_name))

def merge_all_exported_files(destination_folder="exports"):
    with open("all_files.txt", "w") as out_file:
        for root, _, files in os.walk(destination_folder):
            for file_name in files:
                with open(os.path.join(root, file_name), "r") as in_file:
                    out_file.write(in_file.read())
                    out_file.write("\n\n\n")

if __name__ == "__main__":
    merge_all_exported_files()