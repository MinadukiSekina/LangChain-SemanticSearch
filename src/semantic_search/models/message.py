from pydantic import BaseModel, Field


class Message(BaseModel):
    """メッセージのモデル"""

    prompt: str = Field(title="Request message to LLM.", max_length=1000)


class LLMResponse(BaseModel):
    """LLMのレスポンスのモデル"""

    result: list[str]
