

def get_best_products(data, min_reviews=5, top_n=10):
    """
    Retorna os produtos com melhor média de pontuação (Score).
    Filtra produtos com menos de 'min_reviews' para evitar médias enganosas.
    Protegido com try-except.
    """
    produtos_stats = {}

    for registro in data:
        try:
            prod_id = registro.get('ProductId')
            # Proteção contra dados inválidos no Score
            score = int(registro['Score'])

            if not prod_id:
                continue

            if prod_id not in produtos_stats:
                produtos_stats[prod_id] = {'soma': 0, 'conta': 0}
            
            produtos_stats[prod_id]['soma'] += score
            produtos_stats[prod_id]['conta'] += 1

        except (ValueError, KeyError, TypeError):
            continue

    # Calcular médias
    produtos_medias = []
    for prod_id, stats in produtos_stats.items():
        # Apenas consideramos produtos com um mínimo de reviews
        if stats['conta'] >= min_reviews:
            try:
                media = stats['soma'] / stats['conta']
                produtos_medias.append((prod_id, media, stats['conta']))
            except ZeroDivisionError:
                continue

    # Ordenar pela média (decrescente)
    produtos_ordenados = sorted(
        produtos_medias,
        key=lambda item: item[1], 
        reverse=True
    )

    return produtos_ordenados[:top_n]

def search_reviews_by_keyword(data, keyword):
    """
    Filtra reviews que contenham uma palavra-chave no texto.
    """
    resultados = []
    if not keyword:
        return []
        
    keyword = keyword.lower()

    for registro in data:
        try:
            summary = registro.get('Summary', '').lower()
            text = registro.get('Text', '').lower()

            if keyword in summary or keyword in text:
                resultados.append(registro)
        except AttributeError:
            continue
            
    return resultados