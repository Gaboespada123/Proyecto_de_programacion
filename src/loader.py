import csv
import os

def load_data(file_path):
    """
    Lê um arquivo CSV e o converte em uma lista de dicionários.
    Argumentos:
        file_path (str): O caminho para o arquivo CSV (ex: 'data/Reviews_small.csv')
    Retorna:
        list: Uma lista onde cada elemento é um dicionário representando uma review.
    """
    data = []
    
    # 1. Verificar se o arquivo existe antes de tentar abri-lo
    if not os.path.exists(file_path):
        
        print(f"ERRO: O arquivo não foi encontrado em: {file_path}")
        return []

    try:
        # 2. Abrir o arquivo com encoding 'utf-8'
        with open(file_path, mode='r', encoding='utf-8') as f:
            
            # 3. Usar DictReader
            reader = csv.DictReader(f)
            
            print("Carregando dados...")
            
            for row in reader:
                # 4. Limpeza e Conversão de Tipos
                try:
                    # Verificamos que os dados chave existam
                    if not row['Score'] or not row['HelpfulnessNumerator']:
                        continue 

                    # Convertimos a inteiros
                    row['Score'] = int(row['Score'])
                    row['HelpfulnessNumerator'] = int(row['HelpfulnessNumerator'])
                    row['HelpfulnessDenominator'] = int(row['HelpfulnessDenominator'])
                    row['Time'] = int(row['Time'])
                    
                    # Adicionamos a linha processada
                    data.append(row)
                    
                except (ValueError, TypeError):
                    # Se houver dados corrompidos, pulamos a linha
                    continue

        print(f"Foram carregadas {len(data)} reviews corretamente.")
        return data

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return []

# Bloco de teste
if __name__ == "__main__":
    mis_datos = load_data("data/Reviews_small.csv")
    if mis_datos:
        print(mis_datos[0])
