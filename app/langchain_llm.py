# app/langchain_llm.py
from langchain_core.language_models.llms import LLM
from typing import Optional, List
from app.executor import run_execution

class JulepLLM(LLM):
    model: str
    task_id: str

    @property
    def _llm_type(self) -> str:
        return "julep"

    input_key: str = "topic"  # Optional: make configurable

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        input_data = {self.input_key: prompt}
        return run_execution(self.task_id, input_data)
