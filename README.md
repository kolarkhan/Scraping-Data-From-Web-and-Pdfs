## Overview

This Python tool seamlessly combines PDF metadata extraction and web scraping functionalities. It is designed to efficiently collect information from local PDF files, focusing on extracting Title, Author, and Subject details from research papers. Additionally, the tool scrapes data related to Muslim names and their corresponding meanings from specified web pages.

## Features

## PDF Metadata Extraction:
Utilizes PyPDF2 to extract metadata such as Title, Author, and Subject from local PDF files.
Supports batch processing for handling multiple PDF files.

## Web Scraping for Muslim Names:
Employs BeautifulSoup and requests to scrape Muslim names and their meanings from specified web pages.
Enables data extraction from multiple web pages dedicated to Muslim names.

## MongoDB Database Interaction:
Connects to a MongoDB database to store the extracted PDF metadata and Muslim names data in separate collections.
Provides functions for seamless insertion of data into MongoDB collections and downloading data from collections to Excel files.

## Tkinter GUI for User Interaction:
Features a Tkinter-based graphical user interface (GUI) for an intuitive and user-friendly experience.
Incorporates buttons within the GUI to trigger the download of PDF metadata and Muslim names data stored in MongoDB.

## Prerequisites

To run this tool, you need:

Python (version 3.12).
Required libraries installed using pip install -r requirements.txt.

## Set path 
There is some pdf files in PDF files folder.You can test from it.If you have your own files then change the path in main.py file.
You can also set web pages links in main.py file.

## Usage
Run the main.py file

## Installation
pip install -r requirements.txt
 
