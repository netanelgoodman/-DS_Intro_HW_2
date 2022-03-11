def reverse(sentence, reverse_word):
    try:
        list_words = sentence.split()
        if type (reverse_word) == str:
            if reverse_word in list_words:
                sentence = sentence.replace(reverse_word, reverse_word[::-1],1)
                return(sentence)
            else:
                return ("no match word found")
        else:
            return ("invalid input" )
    except:
        return ("invalid input" )