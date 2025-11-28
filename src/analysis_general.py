import utils # Para usar o convert_date

def reviews_by_year(data):
    """Devolve um dicionário {Ano: Quantidade}"""
    reviews_por_ano = {}
    for row in data:
        timestamp = row['Time']
        data_legivel = utils.convert_date(timestamp) # Devolve "YYYY-MM-DD"
        
        if data_legivel:
            # TAREFA: Extrair apenas o ano (os primeiros 4 caracteres)
            ano = data_legivel[:4]
            # TAREFA: Contar quantas reviews há nesse ano
            ano = data_legivel[:4]
            if ano not in reviews_por_ano:
                reviews_por_ano[ano] = 0
            reviews_por_ano[ano] += 1

    return reviews_por_ano

def analyze_word_frequency(data):
    """PARTE CRIATIVA: Palavras mais comuns em 5 estrelas vs 1 estrela"""
    words_5_star = {}
    words_1_star = {}
    
    # Palavras a ignorar (artigos (in)defenidos, conjunções, pronomes e preposições comuns)

    stop_words = ['the', 'and', 'a', 'to', 'of', 'is', 'it', 'in',
                  'i', 'this', 'that', 'was', 'for', 'on', 'with',
                  'as', 'but', 'are', 'they', 'be', 'at', 'or']

    for row in data:
        score = row['Score']
        text = row['Text'].lower()
        words = text.split()
        for word in words:
            if word not in stop_words:
                continue
            if score == 5:
                if word not in words_5_star:
                    words_5_star[word] = 0
                words_5_star[word] += 1
            elif score == 1:
                if word not in words_1_star:
                    words_1_star[word] = 0
                words_1_star[word] += 1
    return words_5_star, words_1_star


"""stop words alternativa:
stop_words ={
    # Articles
    "the", "a", "an",

    # Conjunções
    "and", "but", "or", "nor", "for", "yet", "so",
    "although", "though", "because", "since",
    "if", "unless", "whereas", "while", "as", "before",
    "after", "until", "once", "whether", "that", "than",
    "both", "either", "neither", "whether", "as",

    # Pronomes
    "i", "you", "he", "she", "it", "we", "they",
    "me", "him", "her", "us", "them","my", "your", "his", "her", "its", "our", "their",
    "mine", "yours", "hers", "ours", "theirs", "myself", "yourself", "himself", 
    "herself", "itself","ourselves", "yourselves", "themselves", "this", "that", 
    "these", "those", "who", "whom","whose", "which", "that", "any", "anyone",
    "anybody", "anything", "some", "someone", "somebody", "something", "each", "either",
    "neither", "few", "many", "several", "all", "most",
    "none", "one", "everyone", "everybody", "everything",
    "no one", "nobody", "nothing",

    # Interrogativa
    "what", "which"
} """