
from unittest.mock import patch

from backend.knowledge_base import index_pdf


def test_index_pdf():
    pdf_bytes = b"fake pdf content"

    chunks = [
        "Nexus AI is a knowledge assistant",
        "It searches documents semantically",
    ]

    indexed_chunks = [
        {"text": chunks[0], "embedding": [0.1, 0.2]},
        {"text": chunks[1], "embedding": [0.3, 0.4]},
    ]

    with (
        patch(
            "backend.knowledge_base.process_pdf",
            return_value=chunks,
        ) as mock_process,
        patch(
            "backend.knowledge_base.build_chunk_index",
            return_value=indexed_chunks,
        ) as mock_index,
    ):
        result = index_pdf(pdf_bytes)

    assert result == indexed_chunks

    mock_process.assert_called_once_with(
        pdf_bytes,
        chunk_size=500,
        overlap=50,
    )
    mock_index.assert_called_once_with(chunks)


def test_index_empty_pdf():
    with (
        patch(
            "backend.knowledge_base.process_pdf",
            return_value=[],
        ) as mock_process,
        patch(
            "backend.knowledge_base.build_chunk_index",
        ) as mock_index,
    ):
        result = index_pdf(b"fake pdf content")

    assert result == []
    mock_process.assert_called_once()
    mock_index.assert_not_called()
