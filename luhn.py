from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarize(content:str, limit:int=2, text_language:str = 'english')-> tuple[str]:
    parser = PlaintextParser.from_string(content, Tokenizer(text_language))

    summarizer = LuhnSummarizer(Stemmer(text_language))
    summarizer.stop_words = get_stop_words(text_language)

    summary = summarizer(parser.document, limit)
    return summary