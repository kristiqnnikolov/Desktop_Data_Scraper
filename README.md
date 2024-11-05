This project is a web application for scraping data from the website https://desktop.bg/computers-all
and creating API to access the data.

Data includes details as follow : ID, cpu name, processor type, ram tyoe, motherboard type and gpu type.

Used technologies: **Python**, **Flask**, **SQLite**, **Scrapy**
                   
Content
- Installation💻
- Usage🚀
- Database Schema📋
- API Endpoints📡

## Installation 💻

1. Clone the repository:
    ```bash
   git clone https://github.com/kristiqnnikolov/desktop_scraper.git
   cd desktop_scraper

2. Create a virtual environment:
    ```bash
    python -m venv venv

3. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate

    - On macOS and Linux:
      ```bash
      source venv/bin/activate

4. Install the dependencies:
      ```bash
      pip install -r requirements.txt
      pip install flask

## Usage 🚀

1. Run the **Scrapy** spider to scrape data:
      ```bash
      scrapy crawl get_computers_data -O computers_data.json

2. Initialize the database:
      ```bash
      python 2_init_db.py

3. Insert scraped data into the database:
      ```bash
      python 3_insert_data_to_db.py

4. Run the **Flask** application:
      ```bash
      python 4_flask_app.py
   
5. Access the application:

   Go to `http://127.0.0.1:5000/computers`
   
   Apply **Pretty-print** check
   
6. Verify data by running 5_verify_data.py (Optional).
   This file will print the total entries from the database.

   
## Database Schema📋

The database contains a single table `computers` with the following schema:

- `id` (INTEGER): Primary key, autoincrement.
- `cpu_name` (TEXT): Name of the CPU.
- `processor` (TEXT): Processor type.
- `motherboard` (TEXT): Motherboard type.
- `gpu` (TEXT): GPU type.
- `ram` (TEXT): RAM type.

## API Endpoints📡

Retrieve a list of computers with optional filtering.

**Parameters:**

- `processor` (optional): Filter by processor type.
- `gpu` (optional): Filter by GPU type.
- `motherboard` (optional): Filter by motherboard type.
- `ram` (optional): Filter by RAM type.
