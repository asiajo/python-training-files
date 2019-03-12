import re

"""It removes multiplied consecutive groups of letters"""


def condensing_sentences(s):
    return re.sub('(\S+)\s+\\1', '\\1', s)
    

text = 'Digital alarm clocks scare area children.'
print(condensing_sentences(text))
