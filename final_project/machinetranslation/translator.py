"""
Final Project
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = "2018-05-01"  # set the version for Watson Translator


authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)  # use my translator


def english_to_french(english_text):
    """
    This function converts and returns English text to French
    """
    if english_text is None or \
            (str == type(english_text) and "" == english_text.strip()):
        return ""  # If nothing provided, return a blank string
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """
    This function converts and returns French text to English
    """
    if french_text is None or \
            (str == type(french_text) and "" == french_text.strip()):
        return ""  # If nothing provided, return a blank string
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
