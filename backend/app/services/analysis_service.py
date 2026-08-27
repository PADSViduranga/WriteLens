from app.analyzers.feature_normalizer import feature_normalizer
from app.analyzers.linguistic_analyzer import linguistic_analyzer
from app.analyzers.reliability_analyzer import reliability_analyzer
from app.analyzers.statistical_analyzer import statistical_analyzer
from app.processors.text_processor import text_processor


class AnalysisService:
    """Handles writing analysis operations."""

    async def analyze(self, text: str) -> dict:
        processed_text = text_processor.process(text)

        reliability = reliability_analyzer.analyze(
            word_count=processed_text["word_count"],
            sentence_count=processed_text["sentence_count"],
        )

        statistical_features = statistical_analyzer.analyze(
            words=processed_text["words"],
            sentences=processed_text["sentences"],
        )

        linguistic_features = linguistic_analyzer.analyze(
            text=processed_text["text"],
            words=processed_text["words"],
            sentences=processed_text["sentences"],
        )

        combined_features = {
            **statistical_features,
            **linguistic_features,
        }

        normalized_features = feature_normalizer.normalize(
            combined_features
        )

        return {
            "status": "success",
            "message": "Text analysis completed successfully.",
            "word_count": processed_text["word_count"],
            "sentence_count": processed_text["sentence_count"],
            "paragraph_count": processed_text["paragraph_count"],
            "reliability": reliability,
            "statistical_features": statistical_features,
            "linguistic_features": linguistic_features,
            "normalized_features": normalized_features,
        }


analysis_service = AnalysisService()