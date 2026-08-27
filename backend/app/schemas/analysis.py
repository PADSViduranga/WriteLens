from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=100_000,
        description="Text to analyze.",
    )


class StatisticalFeatures(BaseModel):
    average_word_length: float
    average_sentence_length: float
    sentence_length_std: float
    vocabulary_diversity: float
    repeated_word_ratio: float


class LinguisticFeatures(BaseModel):
    punctuation_density: float
    question_ratio: float
    exclamation_ratio: float
    capitalization_ratio: float
    long_word_ratio: float
    function_word_ratio: float


class NormalizedFeatures(BaseModel):
    average_word_length: float
    average_sentence_length: float
    sentence_length_std: float
    vocabulary_diversity: float
    repeated_word_ratio: float
    punctuation_density: float
    question_ratio: float
    exclamation_ratio: float
    capitalization_ratio: float
    long_word_ratio: float
    function_word_ratio: float


class ReliabilityResult(BaseModel):
    score: float
    level: str


class ScoringResult(BaseModel):
    score: float
    signals: dict[str, float]


class AnalysisResponse(BaseModel):
    status: str
    message: str
    word_count: int
    sentence_count: int
    paragraph_count: int
    reliability: ReliabilityResult
    statistical_features: StatisticalFeatures
    linguistic_features: LinguisticFeatures
    normalized_features: NormalizedFeatures
    scoring: ScoringResult