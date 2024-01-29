import pymongo
import pandas as pd


def connect_to_mongodb():
    # Replace the following with your MongoDB connection details
    # If you have your own string you can put below in MongoClient
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database_name = "My_DataBase"

    # Access or create the specified database
    db = client[database_name]

    return db


def insert_data_into_collection(collection, data):
    try:
        for item in data:
            result = collection.insert_one(item)
            print(f"Successfully inserted document with _id: {result.inserted_id} into MongoDB.")

    except Exception as e:
        print(f"Error inserting data into MongoDB: {str(e)}")


def download_data_to_excel(collection, excel_filename):
    try:
        cursor = collection.find({})
        data_list = list(cursor)

        if data_list:
            # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data_list)

            # Save DataFrame to an Excel file
            df.to_excel(excel_filename, index=False)
            print(f"Data downloaded and saved to {excel_filename} successfully.")
        else:
            print("No data found in the collection.")

    except Exception as e:
        print(f"Error downloading data: {str(e)}")



if __name__ == "__main__":
    db = connect_to_mongodb()
    pdf_collection = db['pdf_scrap']
    web_collection = db['web_scrap']

    download_data_to_excel(pdf_collection, 'pdf_.xlsx')
    download_data_to_excel(web_collection, 'web_.xlsx')
