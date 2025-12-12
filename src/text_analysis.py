
import string

def get_most_common_words(data, top_n=10):
    word_counts = {}
    
    # 1. Stopwords (Palavras a ignorar)
    stopwords = {
        "the", "a", "an", "and", "or", "but", "is", "are", "was", "were", 
        "of", "in", "on", "at", "to", "for", "with", "by", "it", "this", "that",
        "i", "you", "he", "she", "we", "they", "my", "your", "br", "have", "not", "be",
        "as", "from", "so"
    }
    
    # Tabela para eliminar pontuação
    translator = str.maketrans('', '', string.punctuation)

    # 2. DETECTAR NOME DA COLUNA DE TEXTO AUTOMATICAMENTE
    text_key = "Text" 
    if data:
        keys = list(data[0].keys())
        # Procuramos uma chave que se pareça com 'Text' ou 'text' (removendo espaços)
        for k in keys:
            if "text" in k.lower():
                text_key = k
                break
        

    # 3. PROCESSAR
    for registro in data:
        try:
            # Obter texto usando a chave detectada
            texto_bruto = str(registro.get(text_key, ''))
            
            # Se falhar, tentamos com 'Summary' como plano B
            if len(texto_bruto) < 2:
                texto_bruto = str(registro.get('Summary', ''))

            # Limpeza: minúsculas e remover pontuação
            texto_limpo = texto_bruto.lower().translate(translator)
            palavras = texto_limpo.split()
            
            for palavra in palavras:
                # Filtrar stopwords e palavras curtas
                if palavra not in stopwords and len(palavra) > 2:
                    word_counts[palavra] = word_counts.get(palavra, 0) + 1
                    
        except Exception:
            continue

    # 4. ORDENAR E DEVOLVER
    resultado = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    
        
    return resultado