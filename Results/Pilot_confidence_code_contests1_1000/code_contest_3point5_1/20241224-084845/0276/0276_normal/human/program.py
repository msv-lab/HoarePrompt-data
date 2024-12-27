#!/usr/bin/env python

def normalize(string):
    return ''.join(filter(lambda x: x.isalpha(), string))

def is_valid_encoding(encoding, word_list):
    encoding_toks = encoding.split('<3')
    message_str = ''.join(word_list)
    encoding_str = ''
    for enc in encoding_toks[1:-1]:
        enc = normalize(enc)
        if not enc:
            return "no"
        encoding_str += enc 
    if encoding_str == message_str:
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    n = int(raw_input())
    word_list = []
    for i in range(n):
        word_list.append(raw_input())
    encoding = raw_input()
