from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarize(content:str, limit:int=2, text_language:str = 'english',bonus_words: list = None, stigma_words: list = None, null_words: list = None)-> tuple[str]:

    parser = PlaintextParser.from_string(content, Tokenizer(text_language))

    summarizer = TextRankSummarizer(Stemmer(text_language))
    summarizer.stop_words = get_stop_words(text_language)

    if bonus_words:
        summarizer.bonus_words = bonus_words
    if stigma_words:
        summarizer.stigma_words = stigma_words
    if null_words:
        summarizer.null_words = null_words


    summary = summarizer(parser.document, limit)
    return summary


        