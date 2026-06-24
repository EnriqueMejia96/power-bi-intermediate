# Mining domain coverage report

## training
- Dim_Area.AreaName: términos detectados=Mina, Chancado, Correas, Molienda, Flotación, Relaves, HSE, Energía, correa; ejemplos=Mina Rajo Abierto, Despacho Mina, Perforación y Tronadura, Carguío y Transporte, Chancado Primario, Transporte por Correas
- Dim_Equipo.EquipmentType: términos detectados=Chancado, Flotación, Relaves, CAEX, SCADA, Dispatch, Energía, correa, chancador, pulpa, PLC, vibración, bomba; ejemplos=PLC, Camión CAEX, Cargador frontal, Sensor de vibración, Chancador secundario, Servidor SCADA
- Dim_Servicio.ServiceName: términos detectados=Mina, Correas, Relaves, SCADA, Dispatch, HSE, Energía, correa, geotécnico; ejemplos=Mantenimiento Mecánico Mina, Mantenimiento Eléctrico Mina, Mantenimiento Planta, Inspección de Correas, Soporte Dispatch, Automatización y Control
- Dim_Ubicacion.LocationName: términos detectados=Mina, Chancado, Flotación, chancador; ejemplos=Pit Norte, Pit Sur, Frente 4100, Stockpile ROM, Chancador Primario, Faja CV-101
- Dim_TipoTrabajo.WorkTypeName: términos detectados=HSE; ejemplos=Preventivo, Correctivo no planificado, Predictivo, Inspección operacional, Inspección HSE, Overhaul
- Dim_Proyecto.ProjectName: términos detectados=Mina, Chancado, Correas, Molienda, Flotación, Relaves, CAEX, SCADA, Dispatch, correa, pulpa, bomba, geotécnico; ejemplos=Optimización de Chancado Primario 001, Reemplazo de Correa CV-101 002, Mejora de Disponibilidad de Camiones CAEX 003, Modernización Sistema Dispatch 004, Upgrade SCADA Planta 005, Reducción de Consumo Energético en Molienda 006
- Fact_Mantenimiento.FailureMode: términos detectados=Chancado, correa, chancador, pulpa, PLC, vibración, bomba; ejemplos=Falla de pala, Desgaste de neumáticos, Pérdida de comunicación PLC, Falla eléctrica, Corte de correa, Alta vibración
- Fact_Incidentes.IncidentType: términos detectados=Mina, HSE, Energía, correa, geotécnico, control crítico; ejemplos=Condición subestándar, Bloqueo y etiquetado, Incidente operacional, Falla de control crítico, Acto subestándar, Casi accidente
- Fact_Energia.Shift: turnos operacionales cubiertos; ejemplos=Día, Tarde, Noche
- Fact_Productividad.Shift: turnos operacionales cubiertos; ejemplos=Día, Tarde, Noche

## project
- Dim_Area.AreaName: términos detectados=Mina, Chancado, Correas, Molienda, Flotación, Relaves, HSE, Energía, correa; ejemplos=Mina Rajo Abierto, Despacho Mina, Perforación y Tronadura, Carguío y Transporte, Chancado Primario, Transporte por Correas
- Dim_Equipo.EquipmentType: términos detectados=Chancado, Flotación, Relaves, CAEX, SCADA, Dispatch, Energía, correa, chancador, pulpa, PLC, vibración, bomba; ejemplos=Alimentador, Camión CAEX, PLC, Perforadora, Servidor Historiador, Cargador frontal
- Dim_Servicio.ServiceName: términos detectados=Mina, Correas, Relaves, SCADA, Dispatch, HSE, Energía, correa, geotécnico; ejemplos=Mantenimiento Mecánico Mina, Mantenimiento Eléctrico Mina, Mantenimiento Planta, Inspección de Correas, Soporte Dispatch, Automatización y Control
- Dim_Ubicacion.LocationName: términos detectados=Mina, Chancado, Flotación, chancador; ejemplos=Pit Norte, Pit Sur, Frente 4100, Stockpile ROM, Chancador Primario, Faja CV-101
- Dim_TipoTrabajo.WorkTypeName: términos detectados=HSE; ejemplos=Preventivo, Correctivo no planificado, Predictivo, Inspección operacional, Inspección HSE, Overhaul
- Dim_Proyecto.ProjectName: términos detectados=Mina, Chancado, Correas, Molienda, Flotación, Relaves, CAEX, SCADA, Dispatch, correa, pulpa, bomba, geotécnico; ejemplos=Optimización de Chancado Primario 001, Reemplazo de Correa CV-101 002, Mejora de Disponibilidad de Camiones CAEX 003, Modernización Sistema Dispatch 004, Upgrade SCADA Planta 005, Reducción de Consumo Energético en Molienda 006
- Fact_Mantenimiento.FailureMode: términos detectados=Chancado, correa, chancador, pulpa, PLC, vibración, bomba; ejemplos=Falla de bomba de pulpa, Deriva de sensor, Bloqueo de chancador, Obstrucción de chute, Alta vibración, Desalineamiento de correa
- Fact_Incidentes.IncidentType: términos detectados=Mina, HSE, Energía, correa, geotécnico, control crítico; ejemplos=Bloqueo y etiquetado, Riesgo geotécnico, Incidente operacional, Casi accidente, Incidente de tránsito mina, Derrame menor
- Fact_Energia.Shift: turnos operacionales cubiertos; ejemplos=Noche, Tarde, Día
- Fact_Productividad.Shift: turnos operacionales cubiertos; ejemplos=Día, Noche, Tarde

## Lectura esperada
- Dataset A debe sentirse como operación minera de entrenamiento con foco en chancado, correas, taller mina, molienda y energía.
- Dataset B debe conservar el mismo schema, pero mover los problemas hacia dispatch, relaves, molienda, flota mina y OT.
- Ningún nombre corresponde a faenas, empresas o personas reales.