import os
import re

def clean_text_corpus(input_path, output_path):
    # Read the input text from a file
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Define the regex pattern for consecutive duplicate lines
    pattern = r'^(.*)(\r?\n\1)+$'

    # Use re.sub() to replace duplicates with a single instance
    cleaned_text = re.sub(pattern, r'\1', text, flags=re.MULTILINE)

    # Write the cleaned text to an output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

if __name__ == "__main__":
    input_folder = "extracted_data"
    output_folder = "cleaned_data"

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(".txt"):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, input_folder)
                output_file = os.path.splitext(os.path.join(output_folder, rel_path))[0] + ".txt"

                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                extracted_text = clean_text_corpus(input_path, output_file)

                if extracted_text:
                    print("Text cleaning complete for:", input_path)
                    print("Text saved to:", output_file)
