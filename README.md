## Data Extractor

This is a simple Python script that extracts data from CSV, JSON, and XML files and saves the extracted data to a CSV file.
Requirements

    Python 3.x
    Pandas library

### Usage

    Save the script (data_extractor.py) in the same directory as your data files.

    Open a terminal or command prompt in the directory where the script and data files are located.

    Run the script using the following command:

    python data_extractor.py

    The script will extract the data from all CSV, JSON, and XML files in the directory and save it to a CSV file named compiled_data.csv.

### Customization

    To change the name of the target CSV file, open the script in a text editor and change the value of the target_file variable at the bottom of the script.
    To extract data from other file formats, add a new function to the script using Pandas' read_* functions, and add a new loop to the extract_data function to process files with that file extension.

License

None
