
from unittest.mock import patch

from backend.semantic_search import search_chunks


def test_search_chunks_returns_most_similar_first():
    indexed_chunks = [
        {
            "text": "The weather is sunny today",
            "embedding": [0.0, 1.0],
        },
        {
            "text": "Python is a programming language",
            "embedding": [0.8, 0.2],
        },
        {
            "text": "Machine learning uses data to make predictions",
            "embedding": [1.0, 0.0],
        },
    ]

    with patch(
        "backend.semantic_search.generate_embedding",
        return_value=[1.0, 0.0],
    ) as mock_embedding:
        results = search_chunks(
            query="What is machine learning?",
            indexed_chunks=indexed_chunks,
            top_k=2,
        )

    assert len(results) == 2
    assert results[0]["text"] == (
        "Machine learning uses data to make predictions"
    )
    assert results[1]["text"] == "Python is a programming language"
    mock_embedding.assert_called_once_with(
        "What is machine learning?",
        input_type="query",
    )



from backend.semantic_search import build_chunk_index


def test_build_chunk_index():
    chunks = [
        "Python is a programming language",
        "Machine learning uses data",
    ]

    fake_vectors = [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]

    with patch(
        "backend.semantic_search.generate_embeddings",
        return_value=fake_vectors,
    ) as mock_embeddings:
        result = build_chunk_index(chunks)

    assert len(result) == 2
    assert result[0]["text"] == chunks[0]
    assert result[0]["embedding"] == fake_vectors[0]
    assert result[1]["text"] == chunks[1]
    assert result[1]["embedding"] == fake_vectors[1]

    mock_embeddings.assert_called_once_with(
        chunks,
        input_type="document",
    )


def test_build_chunk_index_empty_list():
    with patch(
        "backend.semantic_search.generate_embeddings"
    ) as mock_embeddings:
        result = build_chunk_index([])

    assert result == []
    mock_embeddings.assert_not_called()
