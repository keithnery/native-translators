dictionary = {
    'boa tarde':'Sotxa Kaká',
    'boa noite':"F'thea Kaká",
    'bom dia':"Tx'txaya Kaká",
    'água': 'oya',
    'sol': 'fetxa',
    'lua': 'feya',
    'noite': 'ftheya',
    'dia': 'etxtxa',
    'casa': 'seti',
    'roupa': 'setke',
    'família': 'setitedo',
    'pano': 'setke',
    'vassoura': 'setixtyose',
    'telhado': 'setietxkhe',
    'dente': 'taxi',
    'pedra': 'fowa',
    'gelo': 'fowaxia',
    'serra': 'fowane',
    'geladeira': 'fowaxia-neho',
    'porta': 'khotsa',
    'janela': 'khotstokhe',
    'braço': 'khotxa',
    'coração': 'osla',
    'fogo': 'towe',
    'estudante': 'xtudanti',
    'estudar': 'xtudankya',
    'estudo': 'xtudo',
    'descer': 'etxoka',
    'vermelho': 'etxleya',
    'cair': 'etyaka',
    'cueca': 'xwatkene',
    'bater': 'phaneka',
    'debater': 'phaphneka',
    'peixe': 'piranha',
    'caçador': 'etsfontoa',
    'caçar': 'etsfonkya',
    'vento': 'xmaya',
    'cabelo': 'leya',
    'copo': 'afia',
    'cuia': 'afia',
    'colher': 'foya',
    'noite ': 'ftheyasa',
    'mãe': 'esa'

}

while True:
    word = input('Digite uma palavra em português/Type a word in Portuguese: ').strip().lower()
    if word in dictionary:
        print('Tradução/Translation:', dictionary[word])
    else:
        print('Esta palavra ainda não está no dicionário/This word is not yet in the dictionary.')
