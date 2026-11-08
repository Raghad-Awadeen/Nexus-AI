
from backend.document_pipeline import process_pdf
from backend.semantic_search import build_chunk_index


def index_pdf(
    file_bytes: bytes,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[dict]:
    """Extract, split, and index a PDF for semantic search."""

    chunks = process_pdf(
        file_bytes,
        chunk_size=chunk_size,
        overlap=overlap,
    )

    if not chunks:
        return []

    return build_chunk_index(chunks)
