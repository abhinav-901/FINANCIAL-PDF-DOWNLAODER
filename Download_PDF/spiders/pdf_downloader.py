import scrapy
import os
import json
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from Download_PDF.utils.utils import create_pdf_url
from Download_PDF.items import DownloadPdfItem
import configparser
from pathlib import Path


class PdfDownloader(scrapy.Spider):
    """
    This class is spider used by scrapy to scrape and
    download desired PDFs
    """
    name = 'pdf_downloader'

    # Reading from config file
    # Initialising configparser object
    config = configparser.ConfigParser()

    # creating config path
    config_dir = str(Path(__file__).parent.parent) + '/utils'
    config_name = 'config.ini'
    config_file_path = os.path.join(config_dir, config_name)
    config.read(config_file_path)

    # assigning values to the variables
    OUT_DIR = config["FILE_PATH"]["output_path"]
    COMANY_CODE_PATH = config["FILE_PATH"]["company_code_path"]
    PATTERN = config["PATTERN"]["regex_pattern_string"]

    def start_requests(self):
        """
         must return an iterable of Requests (you can return a list of requests or write a
         generator function) which the Spider will begin to crawl from
        :return: iterable of Requests
        """

        start_url = []  # list containing urls for crawling request
        base_url = "https://www.google.com/search?as_q="
        print(f"Company Code file will be loaded from below path\n{self.COMANY_CODE_PATH}")
        fp = open(self.COMANY_CODE_PATH, 'rb')
        data = json.load(fp)

        for key, value in data.items():
            url = base_url + value + "Annualreportpdf"
            start_url.append(url)
        for url in start_url:
            request = scrapy.Request(url=url)
            yield request

    def parse(self, response):
        """
        method that will be called to handle the response
        downloaded for each of the requests made
        :param response: crawled response for the request url
        :return: pdf url for downloading
        """
        sel = Selector(response)
        for link in sel.xpath("//a[contains(@href,'.pdf')]").extract():
            loader = ItemLoader(item =DownloadPdfItem(), selector=link)
            pdf_url = create_pdf_url(url_string=link,
                                     pattern_string=self.PATTERN)
            print(f"This is url \n{pdf_url}")
            if pdf_url is not None:
                yield Request(pdf_url, callback=self.save_pdf)

    def save_pdf(self, response):
        """
        Method used to save the pdf from the PDF url returned
        by parse method.
        :param response: PDF URL
        :return: Saved PDF
        """

        path = os.path.join(self.OUT_DIR, response.url.split('/')[-1])
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)
