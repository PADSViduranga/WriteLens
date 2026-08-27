class WriteLensException(Exception):
    """Base exception for expected WriteLens application errors."""

    def __init__(
        self,
        message: str,
        code: str = "APPLICATION_ERROR",
    ):
        self.message = message
        self.code = code

        super().__init__(message)