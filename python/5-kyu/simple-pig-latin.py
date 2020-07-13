def pig_it(text):
    return ' '.join(['{}{}ay'.format(s[1:], s[0]) if s not in ['!', '?'] else s for s in text.split(' ')])
