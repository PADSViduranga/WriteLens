from app.analyzers.statistical_analyzer import StatisticalAnalyzer


def test_statistical_analyzer_returns_expected_features():
    analyzer = StatisticalAnalyzer()

    result = analyzer.analyze(
        words=["this", "is", "a", "simple", "test"],
        sentences=["This is a simple test."],
    )

    assert "average_word_length" in result
    assert "average_sentence_length" in result
    assert "sentence_length_std" in result
    assert "vocabulary_diversity" in result
    assert "repeated_word_ratio" in result


def test_vocabulary_diversity_for_unique_words():
    analyzer = StatisticalAnalyzer()

    result = analyzer.analyze(
        words=["this", "is", "a", "test"],
        sentences=["This is a test."],
    )

    assert result["vocabulary_diversity"] == 1.0