import re


def create_pdf_url(url_string, pattern_string):
    pattern = re.compile(pattern_string)
    match = re.findall(pattern, url_string)
    try:
        pdf_url = match[0] + '.pdf'
        return pdf_url
    except Exception as e:
        print(f"Error Message class : {type(e).__name__} at create_pdf_url method")