class FeatureNormalizer:
    """Normalizes analysis features to a 0-1 range."""

    @staticmethod
    def _normalize(value: float, minimum: float, maximum: float) -> float:
        if maximum <= minimum:
            return 0.0

        normalized = (value - minimum) / (maximum - minimum)

        return round(
            max(0.0, min(1.0, normalized)),
            3,
        )

    def normalize(self, features: dict) -> dict:
        return {
            "average_word_length": self._normalize(
                features["average_word_length"],
                1.0,
                15.0,
            ),
            "average_sentence_length": self._normalize(
                features["average_sentence_length"],
                1.0,
                50.0,
            ),
            "sentence_length_std": self._normalize(
                features["sentence_length_std"],
                0.0,
                25.0,
            ),
            "vocabulary_diversity": self._normalize(
                features["vocabulary_diversity"],
                0.0,
                1.0,
            ),
            "repeated_word_ratio": self._normalize(
                features["repeated_word_ratio"],
                0.0,
                1.0,
            ),
            "punctuation_density": self._normalize(
                features["punctuation_density"],
                0.0,
                0.5,
            ),
            "question_ratio": self._normalize(
                features["question_ratio"],
                0.0,
                1.0,
            ),
            "exclamation_ratio": self._normalize(
                features["exclamation_ratio"],
                0.0,
                1.0,
            ),
            "capitalization_ratio": self._normalize(
                features["capitalization_ratio"],
                0.0,
                1.0,
            ),
            "long_word_ratio": self._normalize(
                features["long_word_ratio"],
                0.0,
                1.0,
            ),
            "function_word_ratio": self._normalize(
                features["function_word_ratio"],
                0.0,
                1.0,
            ),
        }


feature_normalizer = FeatureNormalizer()