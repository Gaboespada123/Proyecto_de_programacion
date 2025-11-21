import datetime
import os

def registrar_log(mensaje, tipo="INFO"):
    """
    Guarda un mensaje en el log usando solo lectura (r) y escritura (w).
    """
    path_log = 'logs/app.log'
    
    # 1. Asegurar que la carpeta logs existe (esto sí es de la clase 7)
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # 2. Obtener la fecha actual
    # (Si no han visto datetime, avísame, pero el PDF del proyecto lo exige para la conversión)
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_log = f"[{ahora}] - {tipo} - {mensaje}\n"
    
    contenido_anterior = ""

    # 3. TRUCO: Leer lo viejo primero (si el archivo existe)
    if os.path.exists(path_log):
        try:
            with open(path_log, 'r', encoding='utf-8') as f:
                contenido_anterior = f.read()
        except:
            pass # Si falla al leer, asumimos que está vacío

    # 4. Escribir TODO de nuevo (lo viejo + lo nuevo)
    # El modo 'w' borra el archivo, pero como le metemos 'contenido_anterior', no perdemos nada.
    try:
        with open(path_log, 'w', encoding='utf-8') as f:
            f.write(contenido_anterior + linea_log)
    except Exception as e:
        print(f"Error al escribir log: {e}")

def convert_date(timestamp):
    """
    Convierte timestamp Unix a fecha legible (YYYY-MM-DD).
    Requerido por el PDF del proyecto.
    """
    try:
        if not timestamp:
            return None
        date_obj = datetime.datetime.fromtimestamp(int(timestamp))
        return date_obj.strftime('%Y-%m-%d')
    except Exception as e:
        # Usamos nuestra función compatible
        registrar_log(f"Error fecha {timestamp}: {e}", "ERROR")
        return None
