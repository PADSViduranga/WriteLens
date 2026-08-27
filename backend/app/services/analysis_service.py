from app.analyzers.feature_extractor import feature_extractor
from app.analyzers.feature_normalizer import feature_normalizer
from app.analyzers.reliability_analyzer import reliability_analyzer
from app.scoring.feature_scorer import feature_scorer


class AnalysisService:
    """Handles writing analysis operations."""

    async def analyze(self, text: str) -> dict:
        extracted_features = feature_extractor.extract(text)

        reliability = reliability_analyzer.analyze(
            word_count=extracted_features["word_count"],
            sentence_count=extracted_features["sentence_count"],
        )

        combined_features = {
            **extracted_features["statistical"],
            **extracted_features["linguistic"],
        }

        normalized_features = feature_normalizer.normalize(
            combined_features
        )

        scoring = feature_scorer.score(
            normalized_features
        )

        return {
            "status": "success",
            "message": "Text analysis completed successfully.",
            "word_count": extracted_features["word_count"],
            "sentence_count": extracted_features["sentence_count"],
            "paragraph_count": extracted_features["paragraph_count"],
            "reliability": reliability,
            "statistical_features": extracted_features["statistical"],
            "linguistic_features": extracted_features["linguistic"],
            "normalized_features": normalized_features,
            "scoring": scoring,
        }


analysis_service = AnalysisService()