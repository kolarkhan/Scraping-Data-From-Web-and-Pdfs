import PyPDF2
import os


def extract_pdf_metadata_from_directory(directory_path):
    all_titles = []
    all_authors = []
    all_subjects = []

    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return all_titles, all_authors, all_subjects

    # List all PDF files in the directory
    pdf_files = [file for file in os.listdir(directory_path) if file.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory_path, pdf_file)
        title, author, subject = extract_pdf_metadata(pdf_path)

        all_titles.append(title)
        all_authors.append(author)
        all_subjects.append(subject)

    return all_titles, all_authors, all_subjects


def extract_pdf_metadata(pdf_path):
    # Extract metadata from a single PDF file
    title = author = subject = None

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Extract metadata
        info = pdf_reader.metadata

        # Check if metadata is available
        if hasattr(info, 'title'):
            title = info.title
        if hasattr(info, 'author'):
            author = info.author
        if hasattr(info, 'subject'):
            subject = info.subject

    return title, author, subject


