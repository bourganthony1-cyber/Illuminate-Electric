# Etsy Launch Pipeline

This project contains a python script to automatically generate local folders and files for Etsy listings, allowing you to quickly prepare your products for manual upload.

## How to use

1. Open a terminal or command prompt.
2. Navigate to the folder containing `etsy_pipeline.py`.
3. Run the script using Python:
   ```bash
   python3 etsy_pipeline.py
   ```
4. The script will generate a new folder called `etsy_listings_output`. Inside, you will find separate folders for each product, containing text files with listing details (title, description, tags, price) and image assets (like SVG files).
5. Review the files inside `etsy_listings_output` and manually upload the information and assets to Etsy.

## How to add more products

To add more products, open `etsy_pipeline.py` and add new dictionaries to the `sample_listings` list at the bottom of the script. The script is currently hardcoded to generate a specific SVG for the "caduceus_design" ID, but you can modify the script to generate or copy other assets as needed.
