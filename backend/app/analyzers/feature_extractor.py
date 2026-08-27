from app.analyzers.linguistic_analyzer import linguistic_analyzer
from app.analyzers.statistical_analyzer import statistical_analyzer
from app.processors.text_processor import text_processor


class FeatureExtractor:
    """Coordinates extraction of writing features."""

    def extract(self, text: str) -> dict:
        processed_text = text_processor.process(text)

        statistical_features = statistical_analyzer.analyze(
            words=processed_text["words"],
            sentences=processed_text["sentences"],
        )

        linguistic_features = linguistic_analyzer.analyze(
            text=processed_text["text"],
            words=processed_text["words"],
            sentences=processed_text["sentences"],
        )

        return {
            "text": processed_text["text"],
            "word_count": processed_text["word_count"],
            "sentence_count": processed_text["sentence_count"],
            "paragraph_count": processed_text["paragraph_count"],
            "statistical": statistical_features,
            "linguistic": linguistic_features,
        }


feature_extractor = FeatureExtractor()