

def get_top_reviewers(data, top_n=10):
    """
    Retorna os usuários com maior número de reviews.
    Utiliza try-except para evitar falhas se a chave não existir.
    """
    contagem_usuarios = {}

    for registro in data:
        try:
            # Tenta obter o nome do usuário
            nome_usuario = registro.get('ProfileName', 'Unknown')
            
            if nome_usuario in contagem_usuarios:
                contagem_usuarios[nome_usuario] += 1
            else:
                contagem_usuarios[nome_usuario] = 1

        except Exception:
            continue

    # Ordenar o dicionário
    usuarios_ordenados = sorted(
        contagem_usuarios.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return usuarios_ordenados[:top_n]


def get_most_helpful_users(data, top_n=10):
    """
    Identifica os usuários com maior soma de 'HelpfulnessNumerator'.
    """
    utilidade_usuarios = {}

    for registro in data:
        try:
            nome_usuario = registro.get('ProfileName', 'Unknown')
            utilidade = int(registro['HelpfulnessNumerator'])

            if nome_usuario in utilidade_usuarios: 
                utilidade_usuarios[nome_usuario] += utilidade
            else:
                utilidade_usuarios[nome_usuario] = utilidade

        except (ValueError, KeyError, TypeError):
            continue

    usuarios_ordenados = sorted(  
        utilidade_usuarios.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return usuarios_ordenados[:top_n]

# Agregar en src/analysis_users.py

def get_users_avg_word_count(data, top_n=5):
    """
    Calcula a média de palavras por review para cada utilizador.
    (Requisito: Calcular a média de palavras por avaliação de cada utilizador)
    """
    user_stats = {} 

    for row in data:
        try:
            user = row.get('ProfileName', 'Unknown')
            text = str(row.get('Text', ''))
            
            n_words = len(text.split())

            if user not in user_stats:
                user_stats[user] = {'total_words': 0, 'count': 0}
            
            user_stats[user]['total_words'] += n_words
            user_stats[user]['count'] += 1
        except Exception:
            continue

    # Calcular médias
    user_averages = []
    for user, stats in user_stats.items():
        if stats['count'] > 0:
            avg = stats['total_words'] / stats['count']
            user_averages.append((user, avg))

    
    return sorted(user_averages, key=lambda x: x[1], reverse=True)[:top_n]