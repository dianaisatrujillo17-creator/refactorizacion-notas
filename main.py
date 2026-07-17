# main.py
import os

# Uso de constantes claras en mayúsculas
ARCHIVO_NOTAS = "notas.txt"

def calcular_promedio(nota1: float, nota2: float, nota3: float) -> float:
    """Calcula y retorna el promedio de las tres calificaciones."""
    return (nota1 + nota2 + nota3) / 3

def determinar_estado(promedio: float) -> str:
    """Determina si un estudiante está APROBADO o REPROBADO según su promedio."""
    return "APROBADO" if promedio >= 7 else "REPROBADO"

def registrar_calificacion(nombre: str, nota1: float, nota2: float, nota3: float):
    """Valida los datos de entrada y registra la información del estudiante."""
    # Validación con nombres de variables descriptivos
    datos_validos = nombre != "" and nota1 >= 0 and nota2 >= 0 and nota3 >= 0
    
    if datos_validos:
        promedio = calcular_promedio(nota1, nota2, nota3)
        estado = determinar_estado(promedio)
        
        # Uso de 'with open' para gestionar el archivo de forma automática y segura
        with open(ARCHIVO_NOTAS, "a") as archivo:
            linea = f"{nombre},{nota1},{nota2},{nota3},{promedio:.2f},{estado}\n"
            archivo.write(linea)
            
        print(f"Registro guardado exitosamente para: {nombre}")
    else:
        print("Error: Datos incorrectos. Verifique los campos y calificaciones.")

def listar_calificaciones():
    """Muestra todas las calificaciones almacenadas en un formato tabular limpio."""
    if os.path.exists(ARCHIVO_NOTAS):
        print("-" * 70)
        print(f"{'Estudiante':<15} | {'Nota 1':<8} | {'Nota 2':<8} | {'Nota 3':<8} | {'Promedio':<8} | {'Estado':<10}")
        print("-" * 70)
        
        with open(ARCHIVO_NOTAS, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                # Evita el uso de índices crípticos asignando variables descriptivas
                nombre, nota1, nota2, nota3, promedio, estado = datos
                print(f"{nombre:<15} | {nota1:<8} | {nota2:<8} | {nota3:<8} | {float(promedio):<8.2f} | {estado:<10}")
        print("-" * 70)
    else:
        print("No existen registros actualmente.")

def generar_reporte_rendimiento():
    """Analiza los datos y muestra el total de alumnos aprobados y reprobados."""
    if os.path.exists(ARCHIVO_NOTAS):
        total_aprobados = 0
        total_reprobados = 0
        
        with open(ARCHIVO_NOTAS, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                estado = datos[5]
                if estado == "APROBADO":
                    total_aprobados += 1
                else:
                    total_reprobados += 1
                    
        print("\n=== REPORTE GENERAL DE RENDIMIENTO ===")
        print(f"Estudiantes Aprobados:  {total_aprobados}")
        print(f"Estudiantes Reprobados: {total_reprobados}")
        print("======================================")
    else:
        print("No existen registros de calificaciones para generar el reporte.")


# Pruebas del sistema aplicando las nuevas funciones limpias
if __name__ == "__main__":
    registrar_calificacion("Ana", 8, 9, 10)
    registrar_calificacion("Luis", 5, 6, 4)
    registrar_calificacion("Carlos", 7, 8, 6)
    
    listar_calificaciones()
    generar_reporte_rendimiento()