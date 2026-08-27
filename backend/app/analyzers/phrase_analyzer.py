from collections import Counter


class PhraseAnalyzer:
    """Analyzes repeated word sequences in text."""

    def analyze(self, words: list[str]) -> dict:
        normalized_words = [
            word.lower()
            for word in words
            if word.strip()
        ]

        bigrams = self._create_ngrams(normalized_words, 2)
        trigrams = self._create_ngrams(normalized_words, 3)

        repeated_bigrams = self._find_repeated_ngrams(bigrams)
        repeated_trigrams = self._find_repeated_ngrams(trigrams)

        return {
            "bigram_count": len(bigrams),
            "trigram_count": len(trigrams),
            "repeated_bigram_count": len(repeated_bigrams),
            "repeated_trigram_count": len(repeated_trigrams),
            "bigram_repetition_ratio": self._repetition_ratio(
                bigrams,
                repeated_bigrams,
            ),
            "trigram_repetition_ratio": self._repetition_ratio(
                trigrams,
                repeated_trigrams,
            ),
        }

    @staticmethod
    def _create_ngrams(
        words: list[str],
        n: int,
    ) -> list[tuple[str, ...]]:
        if len(words) < n:
            return []

        return [
            tuple(words[index:index + n])
            for index in range(len(words) - n + 1)
        ]

    @staticmethod
    def _find_repeated_ngrams(
        ngrams: list[tuple[str, ...]],
    ) -> dict[tuple[str, ...], int]:
        counts = Counter(ngrams)

        return {
            ngram: count
            for ngram, count in counts.items()
            if count > 1
        }

    @staticmethod
    def _repetition_ratio(
        ngrams: list[tuple[str, ...]],
        repeated_ngrams: dict[tuple[str, ...], int],
    ) -> float:
        if not ngrams:
            return 0.0

        repeated_occurrences = sum(
            count
            for count in repeated_ngrams.values()
        )

        return round(
            repeated_occurrences / len(ngrams),
            3,
        )


phrase_analyzer = PhraseAnalyzer()