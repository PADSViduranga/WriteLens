from app.analyzers.reliability_analyzer import ReliabilityAnalyzer


def test_short_text_has_low_reliability():
    analyzer = ReliabilityAnalyzer()

    result = analyzer.analyze(
        word_count=10,
        sentence_count=2,
    )

    assert result["level"] == "very_low"
    assert result["score"] == 0.2


def test_long_text_has_high_reliability():
    analyzer = ReliabilityAnalyzer()

    result = analyzer.analyze(
        word_count=500,
        sentence_count=25,
    )

    assert result["level"] == "high"
    assert result["score"] == 1.0