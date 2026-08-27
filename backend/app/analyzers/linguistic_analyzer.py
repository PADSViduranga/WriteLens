import re
from collections import Counter


class LinguisticAnalyzer:
    """Extracts linguistic features from text."""

    def analyze(
        self,
        text: str,
        words: list[str],
        sentences: list[str],
    ) -> dict:
        return {
            "punctuation_density": self._punctuation_density(text),
            "question_ratio": self._question_ratio(sentences),
            "exclamation_ratio": self._exclamation_ratio(sentences),
            "capitalization_ratio": self._capitalization_ratio(words),
            "long_word_ratio": self._long_word_ratio(words),
            "function_word_ratio": self._function_word_ratio(words),
        }

    @staticmethod
    def _punctuation_density(text: str) -> float:
        if not text:
            return 0.0

        punctuation_count = len(
            re.findall(r"[^\w\s]", text)
        )

        return round(
            punctuation_count / len(text),
            3,
        )

    @staticmethod
    def _question_ratio(sentences: list[str]) -> float:
        if not sentences:
            return 0.0

        question_count = sum(
            sentence.endswith("?")
            for sentence in sentences
        )

        return round(
            question_count / len(sentences),
            3,
        )

    @staticmethod
    def _exclamation_ratio(sentences: list[str]) -> float:
        if not sentences:
            return 0.0

        exclamation_count = sum(
            sentence.endswith("!")
            for sentence in sentences
        )

        return round(
            exclamation_count / len(sentences),
            3,
        )

    @staticmethod
    def _capitalization_ratio(words: list[str]) -> float:
        if not words:
            return 0.0

        capitalized_words = sum(
            word[0].isupper()
            for word in words
            if word
        )

        return round(
            capitalized_words / len(words),
            3,
        )

    @staticmethod
    def _long_word_ratio(words: list[str]) -> float:
        if not words:
            return 0.0

        long_words = sum(
            len(word) >= 8
            for word in words
        )

        return round(
            long_words / len(words),
            3,
        )

    @staticmethod
    def _function_word_ratio(words: list[str]) -> float:
        if not words:
            return 0.0

        function_words = {
            "a", "an", "the",
            "and", "or", "but",
            "if", "then",
            "of", "to", "in",
            "on", "at", "for",
            "with", "from",
            "by", "as",
            "is", "are", "was",
            "were", "be", "been",
            "being",
            "have", "has", "had",
            "do", "does", "did",
            "this", "that",
            "these", "those",
            "it", "its",
            "i", "you", "he",
            "she", "we", "they",
        }

        normalized_words = [
            word.lower()
            for word in words
        ]

        counts = Counter(normalized_words)

        function_word_count = sum(
            counts[word]
            for word in function_words
        )

        return round(
            function_word_count / len(normalized_words),
            3,
        )


linguistic_analyzer = LinguisticAnalyzer()