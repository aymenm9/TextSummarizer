import text_rank , luhn, lsa

def get_algo(algo_name:str):
    match algo_name:
        case 'TextRank':
            return text_rank.summarize
        case 'Luhn':
            return luhn.summarize
        case 'LSA':
            return lsa.summarize
        case _:
            return text_rank.summarize