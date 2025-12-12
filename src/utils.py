
import datetime
import os

def registrar_log(mensagem, nivel="INFO"):
    """
    Regista mensagens no terminal e num ficheiro de log.
    Cria a pasta 'logs' se não existir.
    """
    # 1. Preparar a mensagem
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{nivel}] {mensagem}"
    
    # 2. Imprimir no terminal
    print(log_message)
    
    # 3. Guardar no ficheiro
    log_dir = "logs"
    log_file = "app.log"
    
    try:
        # Criar pasta logs se não existir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Escrever no ficheiro (append mode 'a')
        with open(os.path.join(log_dir, log_file), "a", encoding="utf-8") as f:
            f.write(log_message + "\n")
            
    except Exception as e:
        print(f"Erro ao gravar log: {e}")
