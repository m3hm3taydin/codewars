def spin_words(sentence):
    sent_list = sentence.split(' ')
    result = ''
    
    for sent in sent_list:
        if len(sent) < 5:
            result = "{} {}".format(result, sent)
        else:
            result = "{} {}".format(result, sent[::-1])
    
    return result[1:]
