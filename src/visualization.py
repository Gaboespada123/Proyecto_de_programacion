
import matplotlib.pyplot as plt

def plot_top_reviewers(top_reviewers):
    """
    Gera um gráfico de barras com os usuários mais ativos.
    Recebe uma lista de tuplas: [('User1', 10), ('User2', 8)...]
    """
    if not top_reviewers:
        print("Nenhum dado para plotar.")
        return

    # Separar nomes e contagens para os eixos X e Y
    
    nomes = [str(user[0]) for user in top_reviewers] 
    contagens = [user[1] for user in top_reviewers]

    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(nomes, contagens, color='skyblue')
    
    # Configurar rótulos e título
    plt.xlabel('Usuários')
    plt.ylabel('Número de Reviews')
    plt.title('Top 10 Reviewers Mais Ativos')
    
    # Rotacionar os nomes no eixo X para melhor leitura
    plt.xticks(rotation=45, ha='right')
    
    # Ajustar layout e mostrar
    plt.tight_layout()
    plt.show()

def plot_score_distribution(data):
    """
    Gera um histograma com a distribuição das notas (Scores).
    """
    scores = []
    for registro in data:
        try:
            
            s = int(registro['Score'])
            scores.append(s)
        except (ValueError, KeyError, TypeError):
            continue

    if not scores:
        print("Nenhum score encontrado para plotar.")
        return

    # Criar histograma
    plt.figure(figsize=(8, 5))
    # bins=[1, 2, 3, 4, 5, 6] para alinhar as barras com as estrelas (1 a 5)
    plt.hist(scores, bins=[1, 2, 3, 4, 5, 6], align='left', rwidth=0.8, color='orange', edgecolor='black')
    
    plt.xlabel('Pontuação (Estrelas)')
    plt.ylabel('Frequência')
    plt.title('Distribuição das Notas (Scores)')
    plt.grid(axis='y', alpha=0.5)
    plt.show()