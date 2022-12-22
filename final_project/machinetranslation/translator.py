"""
Instance of IBM Watson Language Translation API
Functions using that instance for translating english to french and vice versa
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-12-19',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates english text to french
    """
    if ((not isinstance(english_text, str)) or (len(english_text) < 1)):
        return ''
    result = language_translator.translate(text=english_text, source='en', target='fr').get_result()
    french_text = result['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates french text to english
    """
    if ((not isinstance(french_text, str)) or (len(french_text) < 1)):
        return ''
    result = language_translator.translate(text=french_text, source='fr', target='en').get_result()
    english_text = result['translations'][0]['translation']
    return english_text
