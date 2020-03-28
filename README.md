# FINANCIAL-PDF-DOWNLAODER
This project will take company code as input and download available "Annual Report" of the company automatically by scraping Google and it's search result.
# Prerequisites
Scrapy==2.0.1 
# Installing
1. Install scrapy equal or greater than version mentioned above.
2. Clone the Repository.
3. rovide the Input path of the file containing "Company Code" in below format
               {index:company code} ex({"0": "ASX"}). In project/Data folder one sample file has been placed.
4. Provide the path for saving Downloaded PDF
5. Please go through the config file and provide all neccessary info.
# Running the tests
Once completed with Installation step, go to the project folder and run below command
scrapy crawl pdf_downloader

# Features of the project
This project is very limited functionality as I have developed it for specific purpose.
Crapy with search with company code in google search engine.
Then scrapy will crawl all search result and select only those links haveing extension as .pdf
Then those links will be taken forward for downloading and saving "Annual reports"  of the company.
Please extend this for specifc requirements.

# Help
For any help regarding the use of this project please open issues.
