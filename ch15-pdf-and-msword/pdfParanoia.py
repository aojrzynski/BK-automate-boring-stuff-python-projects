#! python3
# pdfParanoia.py - Goes through every file in the folder (and subfolders) where this program runs and 
# encrypts or decrypts every PDF file found using the password provided via command line. Saves the encrypted/decrypted 
# PDFs with a specific prefix. When decrypting, if the password doesn't work on the file, that file will be skipped.
#
# NOTES: When run, this program will affect the current folder it is in and all its subfolders, so place the program appropriately. 
#        You need to run the program from the command line, with two arguments order:
#        1. The mode. Put 'encrypt' if you want to encrypt PDFs, or 'decrypt' if you want to decrypt PDFs.
#        2. The password. Will be used to encrypt or decrypt the PDFs.
#        Notes: Each new file will be saved in the same directory as the original file.

import PyPDF2, os, sys

# Assign mode and password from command line.
mode = sys.argv[1]
password = sys.argv[2]

# Checks if mode has a valid value assigned to it.
if mode not in ['encrypt', 'decrypt']:
    print('Please specify mode. Write "encrypt" or "decrypt".')
    sys.exit()

# Walks through the file structure and encrypts/decrypts.
for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.pdf'): # Only focus on files ending with '.pdf'.
            filePath = os.path.join(root, name) # Create the relative path for the current PDF file.
            pdfReader = PyPDF2.PdfFileReader(open(filePath, 'rb'))
            
            # When encrypting/decrypting, if the file is already encrypted/decrypted, skip it.
            if mode == 'encrypt' and  pdfReader.isEncrypted:
                continue
            elif mode == 'decrypt' and not pdfReader.isEncrypted:
                continue
            
            if mode == 'decrypt':
                pdfReader.decrypt(password)

            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

            if mode == 'encrypt':
                pdfWriter.encrypt(password)

            prefix = 'encrypted_' if mode == 'encrypt' else 'decrypted_' # Specify the prefix based on the mode.
            filePath = os.path.join(root, prefix + name) # Create the relative path of the PDF about to be saved.

            resultPdf = open(filePath, 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()