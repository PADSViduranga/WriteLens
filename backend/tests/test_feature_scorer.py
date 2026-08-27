from app.scoring.feature_scorer import FeatureScorer


def test_feature_scorer_returns_valid_score():
    scorer = FeatureScorer()

    features = {
        "sentence_length_std": 0.3,
        "vocabulary_diversity": 0.7,
        "repeated_word_ratio": 0.1,
        "punctuation_density": 0.2,
    }

    result = scorer.score(features)

    assert "score" in result
    assert "signals" in result

    assert 0.0 <= result["score"] <= 1.0


def test_feature_scorer_returns_all_signals():
    scorer = FeatureScorer()

    features = {
        "sentence_length_std": 0.3,
        "vocabulary_diversity": 0.7,
        "repeated_word_ratio": 0.1,
        "punctuation_density": 0.2,
    }

    result = scorer.score(features)

    assert "sentence_regularity" in result["signals"]
    assert "vocabulary_pattern" in result["signals"]
    assert "repetition_pattern" in result["signals"]
    assert "punctuation_pattern" in result["signals"]