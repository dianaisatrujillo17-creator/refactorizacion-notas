Nombre:Diana Trujillo

# Sistema de Registro de Calificaciones - Refactorización

Este proyecto contiene la refactorización de un sistema básico de registro de calificaciones desarrollado en Python como parte de la asignatura de **Sistemas Ágiles**.

## Mejoras Realizadas (Principios de Clean Code)

Se aplicaron principios de Código Limpio y técnicas de refactorización sobre el código original para mejorar su calidad y mantenibilidad:

* **Nombres Significativos:** Se reemplazaron funciones crípticas (`p`, `l`, `r`) y variables de una sola letra por nombres descriptivos y fáciles de entender (`registrar_calificacion`, `listar_calificaciones`, `calcular_promedio`, etc.).
* **Gestión Segura de Recursos:** Se sustituyó el manejo manual de archivos (`open` y `close`) por el uso de gestores de contexto (`with open(...)`), garantizando el cierre automático y seguro de los archivos.
* **Separación de Responsabilidades:** Se dividieron las operaciones complejas en funciones pequeñas con una única responsabilidad (`calcular_promedio`, `determinar_estado`).
* **Mejora en la Presentación de Datos:** Se implementó una vista tabular formateada en consola para hacer el listado legible y amigable al usuario.
* **Uso de Constantes:** Definición de constantes claras como `ARCHIVO_NOTAS` para evitar "valores mágicos" en el código.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Control de Versiones:** Git & GitHub