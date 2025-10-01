def sp_eng(sentence: str) -> bool:
    sentence = sentence.lower()
    if 'english' in sentence:
        return True
    return False 
    