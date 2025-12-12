
import sys
from src import loader, utils
from src import analysis_users      # Código do Daniel
from src import analysis_products   # Código do Gabriel
from src import analysis_general    # Codigo do Guilherme
from src import text_analysis       # Codigo do Gabriel
from src import visualization       # Codigo do Gabriel

def main():
    try:
        # 1. Início
        utils.registrar_log("--- Início da execução ---", "INFO")
        
        # 2. Carregar dados
        # NOTA PARA O CARO PROFESSOR RICARDO:
        # Para testar com o dataset completo, altere o nome do ficheiro abaixo para "Reviews.csv"
        # Certifique-se que o ficheiro está na pasta 'data/'
        file_path = 'data/Reviews_small.csv' 
        print(f"A carregar dados de {file_path}...")
        data = loader.load_data(file_path)
        
        if not data:
            print("Erro ao carregar dados.")
            return

        print(f"Dados carregados. Total: {len(data)}")

        # 3. Análises

        #  A. Análise de Usuários 
        # Agora chamamos analysis_users em vez de statistics
        print("\n--- A. Estatísticas de Usuários ---")
        top_users = analysis_users.get_top_reviewers(data, top_n=5)
        print(f"Top Reviewers: {top_users}")

        #  B. Análise de Produtos  
        print("\n--- B. Análise de Produtos ---")
        best_prods = analysis_products.get_best_products(data, min_reviews=2)
        print("Melhores Produtos (Média):")
        for pid, rating, count in best_prods[:3]:
            print(f"  ID: {pid} | Nota: {rating:.1f} | Reviews: {count}")

            
        for pid, rating, count in best_prods[:3]:
            print(f"  ID: {pid} | Nota: {rating:.1f} | Reviews: {count}")
            
        termo = "good"  
        reviews_encontradas = analysis_products.search_reviews_by_keyword(data, termo)
        
        print(f"Reviews contendo a palavra '{termo}': {len(reviews_encontradas)}")
        
        
        if reviews_encontradas:
            print(f"Exemplo: {reviews_encontradas[0].get('Summary', 'Sem resumo')}")

        
        print("Média de palavras por utilizador (Top 3 faladores):")
        top_talkers = analysis_users.get_users_avg_word_count(data, top_n=3)
        for user, avg in top_talkers:
            print(f"  - {user}: {avg:.1f} palavras/review")

        #  C. Análise de Texto  
        print("\n--- C. Análise de Texto ---")
        words = text_analysis.get_most_common_words(data)
        print(f"Palavras comuns: {words}")

        # 4. Visualização
        print("\n--- D. Visualização ---")
        
        visualization.plot_top_reviewers(top_users)
        visualization.plot_score_distribution(data)
        
        print("\nProjeto concluído com sucesso!")
        utils.registrar_log("--- Fim da execução ---", "INFO")

    except Exception as e:
        print(f"Erro crítico no main: {e}")
        utils.registrar_log(f"Erro: {e}", "ERROR")

if __name__ == "__main__":
    main()
