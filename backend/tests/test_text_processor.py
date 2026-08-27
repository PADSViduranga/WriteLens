from app.processors.text_processor import TextProcessor


def test_text_processor_extracts_basic_information():
    processor = TextProcessor()

    result = processor.process(
        "Hello world. This is a test."
    )

    assert result["word_count"] == 6
    assert result["sentence_count"] == 2
    assert result["paragraph_count"] == 1


def test_text_processor_normalizes_whitespace():
    processor = TextProcessor()

    result = processor.process(
        "Hello     world."
    )

    assert result["text"] == "Hello world."