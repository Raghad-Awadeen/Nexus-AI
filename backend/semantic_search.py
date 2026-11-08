
import numpy as np

from backend.embeddings import generate_embedding, generate_embeddings


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """Calculate cosine similarity between two vectors."""

    a = np.array(vector_a, dtype=float)
    b = np.array(vector_b, dtype=float)

    if a.shape != b.shape:
        raise ValueError("Vectors must have the same dimensions")

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Vectors must not be zero vectors")

    return float(np.dot(a, b) / (norm_a * norm_b))


def build_chunk_index(chunks: list[str]) -> list[dict]:
    """Generate and store an embedding for each text chunk."""

    if any(not chunk.strip() for chunk in chunks):
        raise ValueError("Chunks cannot contain empty strings")

    if not chunks:
        return []

    vectors = generate_embeddings(chunks, input_type="document")

    return [
        {"text": chunk, "embedding": vector}
        for chunk, vector in zip(chunks, vectors)
    ]


def search_chunks(
    query: str,
    indexed_chunks: list[dict],
    top_k: int = 3,
) -> list[dict]:
    """Search pre-indexed chunks by semantic similarity."""

    if not query.strip():
        raise ValueError("Query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be greater than zero")

    if not indexed_chunks:
        return []

    query_vector = generate_embedding(query, input_type="query")

    results = []

    for chunk in indexed_chunks:
        score = cosine_similarity(query_vector, chunk["embedding"])

        results.append({
            "text": chunk["text"],
            "score": score,
        })

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:top_k]
