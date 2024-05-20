from pdf_scraper import extract_pdf_metadata_from_directory
from web_scraper import scrape_names_and_meanings
import tkinter as tk
from database_interaction import connect_to_mongodb, insert_data_into_collection, download_data_to_excel


def main():
    # PDF scraping
    # Set the path of your PDFs file Folder or Directory
    pdf_path = r'C:\Users\Hp\PycharmProjects\pythonProject\My_Project_ML_Job\PDF fIles'
    title, author, subject = extract_pdf_metadata_from_directory(pdf_path)

    # Web scraping
    # Set the links of your sites into the below list
    web_urls = [r'https://hamariweb.com/names/muslim/boy/', r'https://hamariweb.com/names/muslim/boy/page-2']
    web_names, web_meanings = scrape_names_and_meanings(web_urls)

    # Database interaction
    db = connect_to_mongodb()

    # Insert PDF data into the PDF collection
    # Here is the transformed data about pdf meta_data
    pdf_collection = db['pdf_scrap']
    pdf_data = [{'Title': i, 'Author': j, 'Subject': k} for i, j, k in zip(title, author, subject)]
    insert_data_into_collection(pdf_collection, pdf_data)

    # Insert web data into the web collection
    # Here is the transformed data about web data extraction
    web_collection = db['web_scrap']
    web_data = [{'names': k, 'meanings': l} for k, l in zip(web_names, web_meanings)]
    insert_data_into_collection(web_collection, web_data)

    # ____________________________Set Buttons to download the stored data from MongoDB__________________________

    root = tk.Tk()
    root.title("Data Download")

    # Function to download PDF data
    def download_pdf_data():
        download_data_to_excel(pdf_collection, 'pdf_data.xlsx')

    # Function to download web data
    def download_web_data():
        download_data_to_excel(web_collection, 'web_data.xlsx')

    # Create buttons for downloading PDF and web data
    pdf_button = tk.Button(root, text="Download PDF Data", command=download_pdf_data)
    pdf_button.pack(pady=10)

    web_button = tk.Button(root, text="Download Web Data", command=download_web_data)
    web_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
