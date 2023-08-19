from PyPDF2 import PdfReader


def get_pdf_text(pdfs):
    """ 
    Get the pdf and extract the text content 

    Parameters:
    pdf_docs (pdf) : all the pdfs

    Returns:
    string  : returns text from the pdfs 

    """
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
        