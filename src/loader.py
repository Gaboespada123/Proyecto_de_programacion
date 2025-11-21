import csv
import os

def load_data(file_path):
    """
    Lee un archivo CSV y lo convierte en una lista de diccionarios.
    Argumentos:
        file_path (str): La ruta al archivo CSV (ej: 'data/Reviews_small.csv')
    Retorna:
        list: Una lista donde cada elemento es un diccionario representando una review.
    """
    data = []
    
    # 1. Verificar si el archivo existe antes de intentar abrirlo
    if not os.path.exists(file_path):
        # Aquí más tarde pondremos logs, por ahora print
        print(f"ERROR: El archivo no se encuentra en: {file_path}")
        return []

    try:
        # 2. Abrir el archivo con encoding 'utf-8'
        with open(file_path, mode='r', encoding='utf-8') as f:
            
            # 3. Usar DictReader
            reader = csv.DictReader(f)
            
            print("Cargando datos...")
            
            for row in reader:
                # 4. Limpieza y Conversión de Tipos
                try:
                    # Verificamos que los datos clave existan
                    if not row['Score'] or not row['HelpfulnessNumerator']:
                        continue 

                    # Convertimos a enteros lo que debe ser entero
                    row['Score'] = int(row['Score'])
                    row['HelpfulnessNumerator'] = int(row['HelpfulnessNumerator'])
                    row['HelpfulnessDenominator'] = int(row['HelpfulnessDenominator'])
                    row['Time'] = int(row['Time'])
                    
                    # Añadimos la fila procesada
                    data.append(row)
                    
                except (ValueError, TypeError):
                    # Si hay datos corruptos, saltamos la fila
                    continue

        print(f"Se cargaron {len(data)} reviews correctamente.")
        return data

    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

# Bloque de prueba
if __name__ == "__main__":
    mis_datos = load_data("data/Reviews_small.csv")
    if mis_datos:
        print(mis_datos[0])
