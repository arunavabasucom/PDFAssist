# import unittest
# from unittest.mock import Mock, patch
# from src.helpers.getPdf import get_pdf_text  # Import the function from your module
# from PyPDF2 import PageObject

# class TestGetPdfText(unittest.TestCase):

#     @patch('PyPDF2.PdfReader')
#     def test_get_pdf_text(self, mock_pdf_reader):
#         # Set up mock PdfReader instance
#         mock_page1 = Mock(spec=PageObject)
#         mock_page1.extract_text.return_value = "Page 1 content"

#         mock_page2 = Mock(spec=PageObject)
#         mock_page2.extract_text.return_value = "Page 2 content"

#         mock_pdf_reader.return_value.pages = [mock_page1, mock_page2]

#         # Call the function with mock PDFs
#         pdfs = ["fake_pdf_1.pdf", "fake_pdf_2.pdf"]
#         result = get_pdf_text(pdfs)

#         # Assert the result matches the expected combined text
#         expected_result = "Page 1 content" + "Page 2 content"
#         self.assertEqual(result, expected_result)

# if __name__ == '__main__':
#     unittest.main()
