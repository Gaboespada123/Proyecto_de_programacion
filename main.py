from src import loader, utils
# Importamos los módulos de tus compañeros (vacíos por ahora)
from src import analysis_users, analysis_general, analysis_products

def main():
    # 1. Inicio del programa (Log manual)
    utils.registrar_log("--- Inicio de la ejecución del programa ---", "INFO")
    
    # 2. Cargar datos
    file_path = 'data/Reviews_small.csv' 
    print(f"Cargando datos desde {file_path}...")
    
    data = loader.load_data(file_path)
    
    if not data:
        print("No se pudieron cargar los datos. Revisa la carpeta 'logs'.")
        utils.registrar_log("Fallo en la carga de datos. El programa se detiene.", "ERROR")
        return

    # Log de éxito
    utils.registrar_log(f"Datos cargados correctamente. Total reviews: {len(data)}", "INFO")

    # 3. Ejecutar Análisis
    print("\n--- Inicio del Análisis ---")
    
    # (Aquí irán las llamadas a las funciones de tus amigos)

    # 4. Fin del programa
    utils.registrar_log("--- Fin de la ejecución ---", "INFO")

if __name__ == "__main__":
    main()
