This project is a web scraper that collects data on electric scooters listed on Cdiscount.
The program automatically extracts:

Product titles

Prices

Customer ratings

Product links

The results are then saved in an Excel file (.xlsx), similar to CSV but more powerful for formatting.

-----

Automated scraping with requests + BeautifulSoup

Excel export with:

Auto-adjusted column widths

Bold headers

Conditional coloring :

🔴 Red prices → above average

🔴 Red ratings → below average

Calculation of average price and average rating (displayed in the header row).

-----

How to run

Install python dependencies:

pip install requests beautifulsoup4 openpyxl

Run the script and open the file xlsx (produits_cdiscount_colo.xlsx, I named)

------

Portefolio Value

This project demonstrates the ability to:

Handle dynamic e-commerce pages

Extract structured data from raw HTML

Format and enrich data for business insights

Build tools that can help dropshippers and e-commerce sellers track competitors.