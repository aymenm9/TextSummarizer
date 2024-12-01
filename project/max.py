import re
def summarize(sentences:tuple[str], summarize, limit:int=2, text_language:str = 'english')-> list[str]:
    sts = []
    for sentence in sentences:
        sts.append(summarize_sentence(sentence,summarize,limit=limit,text_language=text_language))
    return sts
def summarize_sentence(sentence:str, summarize, limit:int=2, text_language:str = 'english')-> str:
    sentence_str = str(sentence)
    sentence_str = re.sub(',','.',sentence_str)
    new_sentence = summarize(sentence_str,limit=limit,text_language=text_language)
    st = ''
    for s in new_sentence:
        st += re.sub(r'\.',',',str(s))
    return re.sub(r',$','.',st)