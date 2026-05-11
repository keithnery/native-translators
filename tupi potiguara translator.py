dictionary = [
    {
        'pt': 'eu',
        'en': 'i',
        'tp': 'ixé'

    },

    {
        'pt': 'você',
        'en': 'you',
        'tp': 'endé'
    },

    {
        'pt': 'guerreiro',
        'en': 'warrior',
        'tp': 'guarinĩ'
},

    {
        'pt': 'falo',
        'en': 'speak',
        'tp': "a-nhe'eng"
    }
]

ignored_words = {
    'pt': ['sou', 'é', 'um', 'uma', 'o', 'a'],
    'en': ['am', 'is', 'are', 'a', 'an', 'the']
}

from_lang = input('Portuguese or english?/Português ou inglês? (pt/en) ').strip().lower()
sentence = input('Type a sentence/Digite uma frase: ').strip().lower()

words = sentence.split()
result = []

for word in words:

    if word in ignored_words[from_lang]:
        continue

    translated = False

    for item in dictionary:
        if item[from_lang] == word:
            result.append(item['tp'])
            translated = True
            break

    if not translated:
        result.append(word)

print('Translation/Tradução: ', ' '.join(result))