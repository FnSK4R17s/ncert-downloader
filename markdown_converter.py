import os

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_file=None):
    """
    Extracts text from a PDF file and optionally saves it to a text file.

    :param pdf_path: Path to the PDF file
    :param output_file: Optional path to save the extracted text
    :return: Extracted text as a string
    """
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)

        # Initialize a variable to hold all extracted text
        all_text = ""

        # Iterate over each page in the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Load the page
            all_text += page.get_text()  # Extract text and append

        # Close the document
        doc.close()

        # Save the extracted text to a file if output_file is specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as text_file:
                text_file.write(all_text)

        return all_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    input_folder = "post_processed"
    output_folder = "extracted_data"

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                rel_path = os.path.relpath(pdf_path, input_folder)
                output_file = os.path.splitext(os.path.join(output_folder, rel_path))[0] + ".txt"

                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                extracted_text = extract_text_from_pdf(pdf_path, output_file)

                if extracted_text:
                    print("Text extraction complete for:", pdf_path)
                    print("Text saved to:", output_file)
