import fitz  # PyMuPDF for PDFs
import docx
import requests
import tempfile
import os
from typing import Optional


class ResumeParser:
    def download_file(self, url: str) -> str:
        """Downloads a file from a given URL and saves it as a temporary file."""
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Failed to download file")
        
        # 🔹 Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf" if url.endswith(".pdf") else ".docx") as temp_file:
            temp_file.write(response.content)
            return temp_file.name

    def check_remote_url(self, url: str) -> bool:
        """Checks if a given URL is remote (starts with http or https)."""
        return url.startswith("http")

    def cleanup_file(self, file_path: str) -> None:
        """Removes a file from the filesystem if it exists."""
        if os.path.exists(file_path):
            os.remove(file_path)

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extracts text from a PDF file, downloading it first if it's a URL."""
        temp_file = None
        if self.check_remote_url(pdf_path):
            temp_file = self.download_file(pdf_path)
            pdf_path = temp_file
        
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        
        if temp_file:
            self.cleanup_file(temp_file)  # Clean up downloaded file
        
        return text.strip()

    def extract_text_from_docx(self, docx_path: str) -> str:
        """Extracts text from a DOCX file, downloading it first if it's a URL."""
        temp_file = None
        if self.check_remote_url(docx_path):
            temp_file = self.download_file(docx_path)
            docx_path = temp_file
        
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        
        if temp_file:
            self.cleanup_file(temp_file)  # Clean up downloaded file
        
        return text.strip()

    def extract_text(self, file_path: str) -> str:
        """Extracts text based on the file type (PDF or DOCX), handling remote URLs."""
        if file_path.endswith(".pdf"):
            return self.extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            return self.extract_text_from_docx(file_path)
        else:
            raise ValueError("Unsupported file format! Use PDF or DOCX.")
