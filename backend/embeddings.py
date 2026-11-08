
import os

from dotenv import load_dotenv

load_dotenv()

VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")


def check_api_key() -> bool:
    """Check whether the Voyage AI API key is configured."""
    return bool(VOYAGE_API_KEY and VOYAGE_API_KEY.strip())





import voyageai


def generate_embedding(
    text: str,
    input_type: str = "document",
) -> list[float]:
    """Generate an embedding vector using Voyage AI."""

    if not text.strip():
        raise ValueError("Text cannot be empty")

    if input_type not in {"query", "document"}:
        raise ValueError("input_type must be 'query' or 'document'")

    client = voyageai.Client()

    result = client.embed(
        texts=[text],
        model="voyage-4-lite",
        input_type=input_type,
    )

    return result.embeddings[0]


def generate_embeddings(
    texts: list[str],
    input_type: str = "document",
) -> list[list[float]]:
    """Generate embeddings for multiple texts in one API request."""

    if not texts:
        raise ValueError("Texts list cannot be empty")

    if any(not text.strip() for text in texts):
        raise ValueError("Texts cannot contain empty strings")

    if input_type not in {"query", "document"}:
        raise ValueError("input_type must be 'query' or 'document'")

    client = voyageai.Client()

    result = client.embed(
        texts=texts,
        model="voyage-4-lite",
        input_type=input_type,
    )

    return result.embeddings

