import os			   
import time			
import calendar 	
from PyPDF2 import PdfFileMerger


def pdf_to_ocr():
	os.chdir(".\output")
	dir_files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
	epoch_time = int(calendar.timegm(time.gmtime()))
	print(dir_files)

	for file in dir_files: 
		if file.endswith('.pdf'): 
			print('Working on converting: ' + file)
			
			file = file.replace('.pdf', '') 
			folder = str(int(epoch_time)) + '_' + file 
			combined = folder + '/' + file 
			# create folder
			if not os.path.exists(folder): 
				os.makedirs(folder)
			# convert PDF to PNG(s)
			magick = 'convert -density 150 "' + file + '.pdf" "' + combined + '-%04d.png"'
			print(magick)
			os.system(magick)
			# convert PNG(s) to PDF(s) with OCR data
			pngs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
			for pic in pngs:
				if pic.endswith('.png'):
					combined_pic = folder + '/' + pic
					print(combined_pic)
					tesseract = 'tesseract "' + combined_pic + '" "' + combined_pic + '-ocr" -l kor PDF'
					print(tesseract)
					os.system(tesseract)
			# combine OCR'd PDFs into one
			ocr_pdfs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

			merger = PdfFileMerger()
			for pdf in ocr_pdfs:
				if pdf.endswith('.pdf'):
					merger.append(folder + '/' + pdf)

			merger.write(file + '-ocr-combined.pdf')
			merger.close()
			print("OCR 추출 완료")
			os.chdir(".\..")
			return
