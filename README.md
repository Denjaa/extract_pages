# extract_pages

People are looking for a script that would be able to read int Portable Document File (PDF) as input and extract specific pages from it.
The extra_pages script was developed to read in document from the user and give it an individual page number or a list of page numbers that need to be extracted.

To run script:
1. Download script into a directory where the input exists
2. Run command python extract_pages.py document.pdf
3. When script will activate it will ask you to provide an input such as 12 (individual page number) or 12, 23, 231 (list of page numbers)

Requirements:
  - Python 3.6.1
  - PyPDF2 1.26.0
  - Argparse
