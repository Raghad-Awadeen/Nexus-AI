import pytest

from backend.text_chunker import split_text_into_chunks


def test_split_text_into_chunks():
    text = " ".join(["word"] * 12)

    chunks = split_text_into_chunks(
        text,
        chunk_size=5,
        overlap=2,
    )

    assert len(chunks) == 4
    assert len(chunks[0].split()) == 5
    assert len(chunks[-1].split()) == 3


def test_chunks_overlap():
    text = "one two three four five six seven"

    chunks = split_text_into_chunks(
        text,
        chunk_size=4,
        overlap=2,
    )

    assert chunks[0].split()[-2:] == chunks[1].split()[:2]


def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        split_text_into_chunks("some text", chunk_size=0)


def test_invalid_overlap():
    with pytest.raises(ValueError):
        split_text_into_chunks("some text", chunk_size=5, overlap=5)