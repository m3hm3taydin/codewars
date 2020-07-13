def decodeMorse(morse_code):
    return ' '.join(''.join([MORSE_CODE[s] if s != '' else ' ' for s in morse_code.split(' ')]).split())
