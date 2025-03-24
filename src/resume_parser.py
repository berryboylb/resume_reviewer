import fitz  # PyMuPDF for PDFs
import docx

class ResumeParser():
    def extract_text_from_pdf(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        return text.strip()

    def extract_text_from_docx(self, docx_path):
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()

    def extract_text(self, file_path):
        if file_path.endswith(".pdf"):
            return self.extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            return self.extract_text_from_docx(file_path)
        else:
            raise ValueError("Unsupported file format! Use PDF or DOCX.")
