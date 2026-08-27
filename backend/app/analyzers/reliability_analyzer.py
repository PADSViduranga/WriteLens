class ReliabilityAnalyzer:
    """Estimates how reliable an analysis is based on text size."""

    def analyze(
        self,
        word_count: int,
        sentence_count: int,
    ) -> dict:
        word_score = self._word_count_score(word_count)
        sentence_score = self._sentence_count_score(sentence_count)

        reliability_score = round(
            (word_score * 0.7) + (sentence_score * 0.3),
            3,
        )

        return {
            "score": reliability_score,
            "level": self._reliability_level(reliability_score),
        }

    @staticmethod
    def _word_count_score(word_count: int) -> float:
        if word_count >= 500:
            return 1.0

        if word_count >= 250:
            return 0.85

        if word_count >= 100:
            return 0.65

        if word_count >= 50:
            return 0.4

        return 0.2

    @staticmethod
    def _sentence_count_score(sentence_count: int) -> float:
        if sentence_count >= 25:
            return 1.0

        if sentence_count >= 15:
            return 0.85

        if sentence_count >= 8:
            return 0.65

        if sentence_count >= 4:
            return 0.4

        return 0.2

    @staticmethod
    def _reliability_level(score: float) -> str:
        if score >= 0.85:
            return "high"

        if score >= 0.6:
            return "moderate"

        if score >= 0.4:
            return "low"

        return "very_low"


reliability_analyzer = ReliabilityAnalyzer()