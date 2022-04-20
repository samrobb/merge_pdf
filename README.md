# merge_pdf / merge_pdf_gui
Merge all PDF files in a directory to one file. Works for locked pdfs as well.

Both command-line and GUI (Tkinter) options are included.

Two executable files are included that were made from the python source code using PyInstaller. The GUI .exe
file can be run from anywhere and includes the options to either unlock or unlock & merge PDF files. The non-gui
.exe must be placed in a folder with the PDF files that are to be merged and ran. It will automatically unlock and
merge all files in the directory.

To build your own executable file from source, navigate to the directory that contains the .py file(s), open
a command prompt window and run
> pyinstaller --onefile merge_pdf.py

and / or

> pyinstaller --onefile --noconsole merge_pdf_gui.py

I suggest building the executables in a new python environment that contains only the dependencies required
for this source:

- PyMuPdf
- pikepdf

It will drastically reduce the final filesize of the executable.

