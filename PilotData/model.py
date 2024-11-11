import os
from abc import ABC, abstractmethod
from groq import Groq
from openai import OpenAI
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

# Selects and returns the appropriate model, either OpenAI or Groq based on the model name
def get_model(name: str, temperature: float):
    openai_models = {
        "gpt-4o-2024-05-13",
        "gpt-4o-mini-2024-07-18",
        "gpt-4-turbo-2024-04-09",
        "gpt-3.5-turbo-0125"
    }

    if name in openai_models:
        return OpenAIModel(name, temperature)

    groq_models = {
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    }

    if name in groq_models:
        return GroqModel(name, temperature)

# Abstract Class for interacting with all models.
class Model(ABC):

    # Method to query the models
    def query(self, prompt):
        response = self._query(prompt)
        return response

    @abstractmethod
    def _query(self, prompt):
        pass

# Specific subclass for interacting with OpenAI's models.
class OpenAIModel(Model):

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
    # Method to query the models
    # Includes retry logic to handle potential API failures
    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def _query(self, prompt):
        response = self.client.chat.completions.create(
            model=self.name,
            messages=[{"role": "user", "content": prompt}] if isinstance(prompt, str) else prompt,
            temperature=self.temperature)
        return response.choices[0].message.content

# Specific subclass for interacting with Groq's models.
class GroqModel(Model):

    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
    # query method to query the models
    # Includes retry logic to handle potential API failures
    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def _query(self, prompt):
        response = self.client.chat.completions.create(
            model=self.name,
            messages=[{"role": "user", "content": prompt}] if isinstance(prompt, str) else prompt,
            temperature=self.temperature)
        return response.choices[0].message.content
