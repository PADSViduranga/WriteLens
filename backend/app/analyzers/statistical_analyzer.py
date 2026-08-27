import math
import re
from collections import Counter


class StatisticalAnalyzer:
    """Extracts statistical features from processed text."""

    def analyze(
        self,
        words: list[str],
        sentences: list[str],
    ) -> dict:
        word_lengths = [
            len(word)
            for word in words
        ]

        sentence_lengths = [
            len(re.findall(r"\b[\w'-]+\b", sentence))
            for sentence in sentences
        ]

        return {
            "average_word_length": self._average(word_lengths),
            "average_sentence_length": self._average(sentence_lengths),
            "sentence_length_std": self._standard_deviation(
                sentence_lengths
            ),
            "vocabulary_diversity": self._vocabulary_diversity(words),
            "repeated_word_ratio": self._repeated_word_ratio(words),
        }

    @staticmethod
    def _average(values: list[int]) -> float:
        if not values:
            return 0.0

        return round(sum(values) / len(values), 3)

    @staticmethod
    def _standard_deviation(values: list[int]) -> float:
        if len(values) < 2:
            return 0.0

        mean = sum(values) / len(values)

        variance = sum(
            (value - mean) ** 2
            for value in values
        ) / len(values)

        return round(math.sqrt(variance), 3)

    @staticmethod
    def _vocabulary_diversity(words: list[str]) -> float:
        if not words:
            return 0.0

        normalized_words = [
            word.lower()
            for word in words
        ]

        unique_words = len(set(normalized_words))

        return round(
            unique_words / len(normalized_words),
            3,
        )

    @staticmethod
    def _repeated_word_ratio(words: list[str]) -> float:
        if not words:
            return 0.0

        normalized_words = [
            word.lower()
            for word in words
        ]

        counts = Counter(normalized_words)

        repeated_words = sum(
            count - 1
            for count in counts.values()
            if count > 1
        )

        return round(
            repeated_words / len(normalized_words),
            3,
        )


statistical_analyzer = StatisticalAnalyzer()