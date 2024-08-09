Data Engineering Project - Book Scraping and Data Storage

This project aims to extract information about books from the website https://books.toscrape.com/ using the Selenium and BeautifulSoup libraries in Python, and then store this data in a CSV file and a PostgreSQL table.

Installation
Clone this repository:

git clone https://github.com/your_username/your_repository.git
Install the dependencies:

cd your_repository
pip install -r requirements.txt
Make sure PostgreSQL is installed on your machine.

Usage
Run the Books_all_pages.py script to extract information from all the books on the website and save it in a CSV file:


python Books_all_pages.py
Then, run the csv_to_DB.py script to create a table in PostgreSQL and import the data from the CSV file:


python csv_to_DB.py


Project Structure
Books_all_pages.py: Main script to extract information from all the books on the website.
Books_page_1.py: Script to extract information from the first page of the website.
Books_page_1_category.py: Script to extract information from the first page with categories.
Data_scrap.py: Module containing functions to perform the data scraping.
books_scraped.csv: CSV file where the extracted data is saved.
csv_to_DB.py: Script to create a PostgreSQL table and import the data from the CSV file.
install_requirements.py: Script to install the project dependencies.
requirements.txt: File containing the project's dependencies.
Contact
For more information or questions, please contact via email: leonardovidolin93@gmail.com.
