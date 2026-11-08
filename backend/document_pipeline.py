
from backend.document_processor import extract_text_from_pdf
from backend.text_chunker import split_text_into_chunks


def process_pdf(
    file_bytes: bytes,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[str]:
    """Extract text from a PDF and split it into chunks."""

    text = extract_text_from_pdf(file_bytes)

    if not text.strip():
        return []

    return split_text_into_chunks(
        text,
        chunk_size=chunk_size,
        overlap=overlap,
    )
