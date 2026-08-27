import re


class TextProcessor:
    """Prepares raw text for analysis."""

    def process(self, text: str) -> dict:
        normalized_text = self._normalize(text)

        words = self._extract_words(normalized_text)
        sentences = self._extract_sentences(normalized_text)
        paragraphs = self._extract_paragraphs(normalized_text)

        return {
            "text": normalized_text,
            "word_count": len(words),
            "character_count": len(normalized_text),
            "sentence_count": len(sentences),
            "paragraph_count": len(paragraphs),
            "words": words,
            "sentences": sentences,
            "paragraphs": paragraphs,
        }

    @staticmethod
    def _normalize(text: str) -> str:
        text = text.strip()
        text = re.sub(r"[ \t]+", " ", text)

        return text

    @staticmethod
    def _extract_words(text: str) -> list[str]:
        return re.findall(r"\b[\w'-]+\b", text)

    @staticmethod
    def _extract_sentences(text: str) -> list[str]:
        sentences = re.split(r"(?<=[.!?])\s+", text)

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

    @staticmethod
    def _extract_paragraphs(text: str) -> list[str]:
        paragraphs = re.split(r"\n\s*\n", text)

        return [
            paragraph.strip()
            for paragraph in paragraphs
            if paragraph.strip()
        ]


text_processor = TextProcessor()