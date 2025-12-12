
import datetime
from src import utils 

def reviews_by_year(data):
    """Devolve um dicionário {Ano: Quantidade}"""
    reviews_por_ano = {}
    for row in data:
        try:
            timestamp = row['Time']
            try:
                data_legivel = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                continue
            
            if data_legivel:
                ano = data_legivel[:4]
                if ano not in reviews_por_ano:
                    reviews_por_ano[ano] = 0
                reviews_por_ano[ano] += 1
        except KeyError:
            continue
    return reviews_por_ano

def reviews_by_month(data):
    """Devolve um dicionário {Mês: Quantidade}"""
    reviews_por_mes = {}
    for row in data:
        try:
            timestamp = row['Time']
            try:
                data_legivel = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                continue
            
            if data_legivel:
                mes = data_legivel[5:7]
                if mes not in reviews_por_mes:
                    reviews_por_mes[mes] = 0
                reviews_por_mes[mes] += 1
        except KeyError:
            continue
    return reviews_por_mes

# Funções de Estatística Geral 

def get_general_statistics(data):
    """
    Calcula estatísticas gerais do dataset:
    - Total de reviews, produtos únicos, utilizadores únicos, média geral.
    """
    stats = {
        'total_reviews': len(data),
        'unique_users': set(),
        'unique_products': set(),
        'total_score': 0,
        'average_score': 0.0
    }

    count_scores = 0

    for registro in data:
        try:
            if 'ProfileName' in registro:
                stats['unique_users'].add(registro['ProfileName'])
            
            if 'ProductId' in registro:
                stats['unique_products'].add(registro['ProductId'])
            
            score = int(registro['Score'])
            stats['total_score'] += score
            count_scores += 1
            
        except (ValueError, KeyError, TypeError):
            continue

    stats['unique_users'] = len(stats['unique_users'])
    stats['unique_products'] = len(stats['unique_products'])
    
    # Aplicamos try-except ZeroDivisionError aquí también por si acaso
    try:
        stats['average_score'] = stats['total_score'] / count_scores
    except ZeroDivisionError:
        stats['average_score'] = 0.0

    return stats

def get_weighted_average_score(data):
    """
    Calcula a avaliação média ponderada pela utilidade (Helpfulness).
    Fórmula: Soma(Score * HelpfulnessNumerator) / Soma(HelpfulnessNumerator)
    """
    soma_ponderada = 0
    total_util = 0

    for registro in data:
        try:
            pontuacao = int(registro['Score'])
            util = int(registro['HelpfulnessNumerator'])

            soma_ponderada += pontuacao * util
            total_util += util
        except (ValueError, KeyError, TypeError):
            continue

    
    try:
        return soma_ponderada / total_util
    except ZeroDivisionError:
        return 0.0