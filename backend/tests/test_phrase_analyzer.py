from app.analyzers.phrase_analyzer import PhraseAnalyzer


def test_phrase_analyzer_returns_expected_features():
    analyzer = PhraseAnalyzer()

    result = analyzer.analyze(
        [
            "the",
            "system",
            "is",
            "fast",
            "the",
            "system",
            "is",
            "secure",
        ]
    )

    assert "bigram_count" in result
    assert "trigram_count" in result
    assert "repeated_bigram_count" in result
    assert "repeated_trigram_count" in result
    assert "bigram_repetition_ratio" in result
    assert "trigram_repetition_ratio" in result


def test_phrase_analyzer_detects_repeated_bigram():
    analyzer = PhraseAnalyzer()

    result = analyzer.analyze(
        [
            "the",
            "system",
            "is",
            "fast",
            "the",
            "system",
            "is",
            "secure",
        ]
    )

    assert result["repeated_bigram_count"] >= 1
    assert result["bigram_repetition_ratio"] > 0.0


def test_phrase_analyzer_handles_short_text():
    analyzer = PhraseAnalyzer()

    result = analyzer.analyze(
        ["hello"]
    )

    assert result["bigram_count"] == 0
    assert result["trigram_count"] == 0
    assert result["bigram_repetition_ratio"] == 0.0
    assert result["trigram_repetition_ratio"] == 0.0