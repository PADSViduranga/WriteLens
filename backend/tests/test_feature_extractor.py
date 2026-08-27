from app.analyzers.feature_extractor import FeatureExtractor


def test_feature_extractor_returns_expected_sections():
    extractor = FeatureExtractor()

    result = extractor.extract(
        "Writing is important. Good writing communicates ideas clearly."
    )

    assert "text" in result
    assert "word_count" in result
    assert "sentence_count" in result
    assert "paragraph_count" in result
    assert "statistical" in result
    assert "linguistic" in result


def test_feature_extractor_counts_sentences():
    extractor = FeatureExtractor()

    result = extractor.extract(
        "This is sentence one. This is sentence two."
    )

    assert result["sentence_count"] == 2