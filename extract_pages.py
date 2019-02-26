from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse

def extracting_pages(input_name):
	pages = input('Enter your pages (seperated by comma): ').split(',')
	pages_to_keep = []
	[pages_to_keep.append(int(page.strip()) - 1) for page in pages] # going though pages that user wants to extract and append it to list

	readDocument = PdfFileReader(input_name, 'rb') # reading in pdf
	writeDocument = PdfFileWriter() # append output to this pdf

	for i in range(readDocument.getNumPages()):
		if i in pages_to_keep:
			page = readDocument.getPage(i) # get specific page
			writeDocument.addPage(page) # append to output

	with open(str(input_name.split('.')[0]) + '_output.pdf', 'wb') as writeOutput:
		writeDocument.write(writeOutput) # write output pages to PDF

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_name', help = 'Enter name of the file that you want to croupout pages from', type = str)
	args = parser.parse_args()

	if args and args.input_name:
		extracting_pages(args.input_name)

if __name__ == '__main__':
	main()