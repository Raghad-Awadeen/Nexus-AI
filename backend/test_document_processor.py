
import fitz

from backend.document_processor import extract_text_from_pdf
from backend.document_pipeline import process_pdf


def test_extract_text_from_pdf():
    pdf = fitz.open()
    page = pdf.new_page()
    page.insert_text((72, 72), "Nexus AI test document")

    pdf_bytes = pdf.tobytes()
    pdf.close()

    result = extract_text_from_pdf(pdf_bytes)

    assert "Nexus AI test document" in result
    assert "[Page 1]" in result



def test_process_pdf():

    pdf = fitz.open()
    page = pdf.new_page()
    page.insert_text(
        (72, 72),
        "Nexus AI processes documents for enterprise knowledge retrieval",
    )
    pdf_bytes = pdf.tobytes()
    pdf.close()

    chunks = process_pdf(
        pdf_bytes,
        chunk_size=5,
        overlap=1,
    )

    assert len(chunks) > 0
    assert any("Nexus AI" in chunk for chunk in chunks)