import argparse

def creat_argparse():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-i','--input',help='the input text file name')
    args_parser.add_argument('-o','--output',help='the output text file name')
    args_parser.add_argument('-a','--algorithm',choices = ['TextRank', 'Luhn', 'LSA'],default='TextRank',help='\'TextRank\' for TextRank Algorithm.\n \'Luhn\' for Luhn\'s Algorithm.\n \'LSA\' for Latent Semantic Analysis.')
    args_parser.add_argument('-l','--limit',type=int, help='The max number of sentences to include in the summary.')
    args_parser.add_argument('-sl','--sentence_limit',type=int, help='The max number of sub-sentences or words to include in the summary.')
    args_parser.add_argument('-lang','--language', help='The language of the text.\n Supported languages: english, french, spanish, german, italian, portuguese, russian, dutch, czech, slovak.')
    return args_parser
