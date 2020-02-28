from btctools.HD import check, WORDS


def gen_phrase_patterns(ordered_known_words, mnemonic_length=24):
    list_of_patterns = []
    for i in range(0, mnemonic_length):
        list_template = ['{x}'] * mnemonic_length
        word_position = 0
        for position, known_word in enumerate(ordered_known_words):
            if i <= position:
                list_template[position + 1] = known_word
            else:
                list_template[position] = known_word
            word_position += 1
        list_of_patterns.append(' '.join(list_template))
    return list_of_patterns


def generate_all_valid_phrases(phrase_patterns):
    total_phrases = []
    for pattern in phrase_patterns:
        for word in WORDS:
            mnemonic = pattern.format(x=word)
            if check(mnemonic):
                total_phrases.append(mnemonic)
    return total_phrases


ordered_known_words = [
    'glory',
    'twice',
    'film',
    'near',
    'senior',
    'trust',
    'thunder',
    'endorse',
    'suggest',
    'scheme',
    'habit',
    'limit',
    'slow',
    'yard',
    'clog',
    'attend',
    'axis',
    'enough',
    'only',
    'magic',
    'hair',
    'rule',
    'zone',
]

phrase_patterns = gen_phrase_patterns(ordered_known_words)
for pattern in phrase_patterns:
    print(pattern)

all_possible_phrases = generate_all_valid_phrases(phrase_patterns)
for phrase in all_possible_phrases:
    print(phrase)

print(f'\ntotal number of phrases created: {len(all_possible_phrases)}\n')

