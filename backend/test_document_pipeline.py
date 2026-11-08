
import fitz

from backend.document_pipeline import process_pdf


def test_process_empty_pdf():
    pdf = fitz.open()
    pdf.new_page()

    pdf_bytes = pdf.tobytes()
    pdf.close()

    chunks = process_pdf(pdf_bytes)

    assert chunks == []
