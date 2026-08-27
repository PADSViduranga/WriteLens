class FeatureScorer:
    """Combines normalized writing features into an interpretable signal score."""

    def score(self, features: dict) -> dict:
        signals = {
            "sentence_regularity": self._sentence_regularity(
                features["sentence_length_std"]
            ),
            "vocabulary_pattern": self._vocabulary_pattern(
                features["vocabulary_diversity"]
            ),
            "repetition_pattern": self._repetition_pattern(
                features["repeated_word_ratio"]
            ),
            "punctuation_pattern": self._punctuation_pattern(
                features["punctuation_density"]
            ),
        }

        overall_score = (
            signals["sentence_regularity"] * 0.35
            + signals["vocabulary_pattern"] * 0.25
            + signals["repetition_pattern"] * 0.20
            + signals["punctuation_pattern"] * 0.20
        )

        return {
            "score": round(overall_score, 3),
            "signals": {
                key: round(value, 3)
                for key, value in signals.items()
            },
        }

    @staticmethod
    def _sentence_regularity(value: float) -> float:
        return max(0.0, min(1.0, 1.0 - value))

    @staticmethod
    def _vocabulary_pattern(value: float) -> float:
        return max(0.0, min(1.0, value))

    @staticmethod
    def _repetition_pattern(value: float) -> float:
        return max(0.0, min(1.0, value))

    @staticmethod
    def _punctuation_pattern(value: float) -> float:
        return max(0.0, min(1.0, value))


feature_scorer = FeatureScorer()