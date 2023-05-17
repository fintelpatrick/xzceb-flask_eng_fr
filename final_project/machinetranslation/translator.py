"""Translator for french and english using watson"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['api']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Takes english input and outputs french translation"""
    model = 'en-fr'
    return_dict = language_translator.translate(
        text=english_text,
        model_id=model).get_result()
    french_text = return_dict['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Takes french input and outputs french translation"""
    model = 'fr-en'
    return_dict= language_translator.translate(
        text=french_text,
        model_id=model).get_result()
    english_text = return_dict['translations'][0]['translation']
    return english_text
    