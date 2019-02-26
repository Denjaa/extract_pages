# extract_pages

The following script is designed specifically to extra an individual page or list of pages from a Portable Document File (PDF). This script will help people to have a PDF document that will include only pages they need. For example person needs only page 20 from 200 long document it can be easily achieve using this script.

To run script:
1. Download script into a directory where the input exists
2. Run command python extract_pages.py document.pdf
3. When script will activate it will ask you to provide an input such as 12 (individual page number) or 12, 23, 231 (list of page numbers)

Requirements:
  - Python 3.6.1
  - PyPDF2 1.26.0
  - Argparse
