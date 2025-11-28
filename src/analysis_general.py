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
    
    # Palavras para ignorar (podes adicionar mais)
    stop_words = ['the', 'and', 'a', 'to', 'of', 'is', 'it', 'in', 'i', 'this', 'that', 'was', 'for', 'on', 'with', 'as', 'but', 'are', 'they', 'be', 'at', 'or']
    
    for row in data:
        score = row['Score']
        text = row['Text'].lower()
        # TAREFA: Limpar pontuação, fazer split()
        # Se score == 5, conta as palavras no dic words_5_star
        # Se score == 1, conta as palavras no dic words_1_star
    
    return words_5_star, words_1_star
