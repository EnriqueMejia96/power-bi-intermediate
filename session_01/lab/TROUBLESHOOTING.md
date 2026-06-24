# Troubleshooting del Laboratorio

## Power BI no abre
Continuar con el plano de solución usando CSV, diccionario y reportes Markdown. La comprensión arquitectónica es el objetivo central del Módulo 1.

## No aparece una relación automática
Crear relación manual en Vista de modelo. Verificar que las columnas llave tengan el mismo tipo. Si hay duda, documentar para Módulo 3.

## El import muestra tipos incorrectos
Entrar a Power Query y revisar el tipo. En Módulo 1 basta con reconocer el problema. La limpieza profunda se hace en Módulo 2.

## El equipo va lento
Usar `data/training/sample`. Evitar importar todas las tablas si la máquina tiene poca memoria.

## El estudiante se queda diseñando visuales
Regresar a la pregunta: qué decisión habilita ese visual, quién lo usará y con qué frecuencia.

## La IA devuelve una respuesta genérica
Mejorar el prompt con:

- Contexto Tech&Eng.
- Audiencia.
- Decisión.
- Tablas disponibles.
- Restricción: no inventar datos.

## Hay confusión entre Power Query, DAX y visuales
Usar esta regla:

- Power Query cambia los datos antes del modelo.
- El modelo define relaciones y significado.
- DAX calcula métricas reutilizables.
- Los visuales comunican una decisión.

## El estudiante quiere usar datos reales
No hacerlo. El curso usa datos sintéticos. Si desea aplicar a su empresa, debe pasar por anonimización, permisos y revisión de privacidad.
