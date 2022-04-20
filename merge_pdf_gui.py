import fitz
import pikepdf
import glob
from tkinter import *
from tkinter import filedialog


def unlock_pdfs(files):
    for file in files:
        pdf = pikepdf.open(file, allow_overwriting_input=True)
        pdf.save(file)


def merge_pdfs(infiles, outfile):
    result = fitz.open()

    for infile in infiles:
        with fitz.open(infile) as pdf:
            result.insert_pdf(pdf)

    result.save(outfile)


def choose_directory_callback():
    directory = filedialog.askdirectory(initialdir="", )
    input_path.set(directory)
    update_label(text='', bg=original_label_color)


def save_file_as_callback():
    file = filedialog.asksaveasfilename(initialdir="", defaultextension="*.pdf", filetypes=(("PDF (*.pdf)", "*.pdf"),
                                                                                            ('All Files (*.*)', "*.*")))
    output_path.set(file)


def unlock_callback():
    inputdir = input_path.get()
    infiles = glob.glob(inputdir + "/*.pdf")
    try:
        unlock_pdfs(infiles)
        update_label(bg='green', text='Unlocked PDFs Successfully')
    except:
        update_label(bg='red', text='Unable to unlock PDFs')


def execute_callback():
    save_file_as_callback()

    inputdir = input_path.get()
    outfile = output_path.get()

    infiles = glob.glob(inputdir + "/*.pdf")
    try:
        unlock_pdfs(infiles)
        merge_pdfs(infiles, outfile)
        update_label(bg='green', text='Unlocked & Merged PDFs Successfully')
    except:
        update_label(bg='red', text='Unable to unlock & merge PDFs')


def update_label(text, bg):
    operation_complete_label.config(bg=bg,
                                    text=text)


if __name__ == '__main__':

    window = Tk()
    window.title("Unlock and Merge PDFs")
    window.geometry("415x100")
    window.resizable(False, False)

    input_path = StringVar()
    output_path = StringVar()
    input_frame = Frame(master=window, width=100, height=50)
    input_dir = Entry(master=input_frame, width=45, textvariable=input_path)
    input_dir.place(x=10, y=10)
    select_input_dir = Button(master=input_frame, width=15, height=0, text='Select Input Folder')
    select_input_dir.config(command=choose_directory_callback)
    select_input_dir.place(x=290, y=10)

    operation_complete_label = Label()
    original_label_color = operation_complete_label.cget("background")
    operation_complete_label.place(x=110, y=40)
    unlock_button = Button(text='Unlock PDFs')
    unlock_button.config(command=unlock_callback)
    unlock_button.place(x=110, y=65)

    merge_button = Button(text='Merge PDFs')
    merge_button.config(command=execute_callback)
    merge_button.place(x=210, y=65)

    input_frame.pack(fill=BOTH)
    window.mainloop()
