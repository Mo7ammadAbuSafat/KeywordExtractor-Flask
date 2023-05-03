import asyncio
import spacy
from collections import Counter
from string import punctuation
nlp = spacy.load("en_core_web_sm")


def get_hotwords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN']
    doc = nlp(text.lower())
    for token in doc:
        if token.text in nlp.Defaults.stop_words or token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            result.append(token.text)
    return result


class KeywordExtractor:
    async def setup(self):
        pass

    @staticmethod
    async def extract(text):
        await asyncio.sleep(1)
        output = set(get_hotwords(text))
        most_common_list = Counter(output).most_common(100)
        keywords = list(map(lambda x: x[0], most_common_list))
        return keywords
