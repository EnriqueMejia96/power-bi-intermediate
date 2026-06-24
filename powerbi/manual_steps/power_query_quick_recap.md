# Power Query Repaso rápido

## Propósito
Reconocer Power Query como la capa donde se prepara el dato antes de que llegue al modelo. En Módulo 1 solo se hace recap; la limpieza profunda se reserva para Módulo 2.

## Qué revisar en las tablas de muestra
| Revisión | Ejemplo | Por qué importa |
|---|---|---|
| Tipos de datos | `BreachHours` numérico | Permite promedios y sumas |
| Llaves | `AreaID`, `ServiceID` | Permiten relaciones |
| Fechas | `DateKey`, `Date` | Permiten inteligencia de tiempo |
| Booleanos | `SLAMetFlag` | Permiten contar cumplidos/no cumplidos |
| Textos | `AreaName`, `ServiceName` | Permiten segmentar |

## Qué observar en datos crudos (`raw`)
Si abres `data/training/raw`, encontrarás problemas intencionales:

- Prioridades en formatos mixtos.
- Estados en español/inglés.
- Duplicados controlados.
- Fechas nulas.
- Columnas legacy.
- Archivo ancho de energía.

No los resuelvas todavía. Úsalos para explicar por qué Power Query será el foco del Módulo 2.

## Buenas prácticas
- Nombrar pasos con intención si se hacen transformaciones.
- Evitar cambiar lógica de negocio sin documentarla.
- No borrar columnas sin confirmar su uso.
- Separar limpieza estructural de cálculo de KPIs.

## Cierre
Power Query responde: ¿el dato está listo para modelarse?
