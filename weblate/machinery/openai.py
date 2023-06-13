import openai

from django.conf import settings

from weblate.machinery.base import MachineTranslation
from .forms import KeyURLMachineryForm

class OpenAITranslation(MachineTranslation):

    name = "OpenAI"
    max_score = 90

    settings_form = KeyURLMachineryForm
    api_base_url = "https://api.openai.com/v1/chat/completions"

    def __init__(self, settings=None):
        super().__init__(settings)
        openai.api_key = self.settings['key']

    def get_authentication(self):
        return {
            "Authorization": f"Bearer {self.settings['key']}",
            "Content-Type": "application/json",
        }

    def map_code_code(self, code):
        return code.replace("_", "-").split("-")[0].lower()

    def is_supported(self, source, language):
        return True

    def download_translations(
        self,
        source,
        language,
        text: str,
        unit,
        user,
        threshold: int = 75,
    ):    

        messages = [
            {"role": "system", "content": "You are a highly skilled translation assistant, adept at translating text from English to various other languages with precision and nuance."},
            {"role": "user", "content": f"Translate {source} to {language}: {text}"}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the assistant's reply from the response
        assistant_reply = response['choices'][0]['message']['content'].strip()

        yield {
            "text": assistant_reply,
            "quality": self.max_score,
            "service": self.name,
            "source": text,
        }
