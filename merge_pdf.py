import fitz
import pikepdf
import glob


def unlock_pdfs(files):
    for file in files:
        pdf = pikepdf.open(file, allow_overwriting_input=True)
        pdf.save(file)


def merge_pdfs(files):
    result = fitz.open()

    for file in files:
        with fitz.open(file) as pdf:
            result.insert_pdf(pdf)

    result.save("merged_pdfs.pdf")


if __name__ == '__main__':
    infiles = glob.glob("*.pdf")
    unlock_pdfs(infiles)
    merge_pdfs(infiles)




