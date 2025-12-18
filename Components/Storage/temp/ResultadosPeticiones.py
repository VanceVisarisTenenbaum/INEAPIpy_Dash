# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 14:10:30 2025

@author: mano
"""


Op = [{"Id":4, "Cod_IOE":"30147", "Nombre":"Estadística de Efectos de Comercio Impagados", "Codigo":"EI"}
,{"Id":6, "Cod_IOE":"30211", "Nombre":"Índice de Coste Laboral Armonizado", "Codigo":"ICLA", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736053992&idp=1254735976596"}
,{"Id":7, "Cod_IOE":"30168", "Nombre":"Estadística de Transmisión de Derechos de la Propiedad", "Codigo":"ETDP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736171438&idp=1254735576606"}
,{"Id":10, "Cod_IOE":"30256", "Nombre":"Indicadores Urbanos", "Codigo":"UA", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176957&idp=1254735976608"}
,{"Id":13, "Cod_IOE":"30219", "Nombre":"Estadística del Procedimiento Concursal", "Codigo":"EPC", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177018&idp=1254735576606"}
,{"Id":14, "Cod_IOE":"30182", "Nombre":"Índices de Precios del Sector Servicios", "Codigo":"IPS", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176864&idp=1254735576778"}
,{"Id":15, "Cod_IOE":"30457", "Nombre":"Índice de Precios de la Vivienda (IPV)", "Codigo":"IPV", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736152838&idp=1254735976607"}
,{"Id":16, "Cod_IOE":"", "Nombre":"Distribución de Nombres", "Codigo":"TNOM", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177009&idp=1254735572981"}
,{"Id":18, "Cod_IOE":"30180", "Nombre":"Índice de Precios de Consumo Armonizado (IPCA)", "Codigo":"IPCA", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176803&idp=1254735976607"}
,{"Id":20, "Cod_IOE":"30013", "Nombre":"Contabilidad Nacional Trimestral de España. Base 2000", "Codigo":"CNTR2000"}
,{"Id":21, "Cod_IOE":"30259", "Nombre":"Estimaciones de la Población Actual (ePOBa)", "Codigo":"EPOBA"}
,{"Id":22, "Cod_IOE":"30245", "Nombre":"Cifras Oficiales de Población de los Municipios Españoles: Revisión del Padrón Municipal", "Codigo":"DPOP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177011&idp=1254734710990"}
,{"Id":23, "Cod_IOE":"30417", "Nombre":"Estadística de Defunciones según la Causa de Muerte", "Codigo":"ECM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176780&idp=1254735573175"}
,{"Id":24, "Cod_IOE":"30048", "Nombre":"Estadística Estructural de Empresas: Sector Industrial", "Codigo":"EEE:IND", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736143952&idp=1254735576715"}
,{"Id":25, "Cod_IOE":"30138", "Nombre":"Índice de Precios de Consumo (IPC)", "Codigo":"IPC", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176802&idp=1254735976607"}
,{"Id":26, "Cod_IOE":"30050", "Nombre":"Índices de Producción Industrial", "Codigo":"IPI", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736145519&idp=1254735576715"}
,{"Id":27, "Cod_IOE":"30051", "Nombre":"Índices de Precios Industriales", "Codigo":"IPRI", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736147699&idp=1254735576715"}
,{"Id":30, "Cod_IOE":"", "Nombre":"Encuesta de coyuntura de comercio al por menor. Base 1994", "Codigo":"CCM"}
,{"Id":31, "Cod_IOE":"30183", "Nombre":"Indicadores de Actividad del Sector Servicios", "Codigo":"IAS", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176863&idp=1254735576778"}
,{"Id":32, "Cod_IOE":"30103", "Nombre":"Índices de Comercio al por Menor", "Codigo":"ICM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176900&idp=1254735576799"}
,{"Id":33, "Cod_IOE":"30264", "Nombre":"Indicadores Demográficos Básicos", "Codigo":"IDB", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177003&idp=1254735573002"}
,{"Id":35, "Cod_IOE":"", "Nombre":"Poblaciones de hecho desde 1900 hasta 1991. Cifras oficiales sacadas de los Censos respectivos.", "Codigo":"DPOH"}
,{"Id":36, "Cod_IOE":"", "Nombre":"Poblaciones de derecho desde 1986 hasta 1995. Cifras oficiales sacadas del Padrón.", "Codigo":"DPOD"}
,{"Id":39, "Cod_IOE":"30162", "Nombre":"Encuesta de Ocupación en Alojamientos Turísticos", "Codigo":"EOT"}
,{"Id":40, "Cod_IOE":"30149", "Nombre":"Estadística de Hipotecas", "Codigo":"HPT", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736170236&idp=1254735576606"}
,{"Id":41, "Cod_IOE":"30053", "Nombre":"Índices de Entradas de Pedidos", "Codigo":"IEP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736148149&idp=1254735576715"}
,{"Id":42, "Cod_IOE":"30052", "Nombre":"Índices de Cifras de Negocios en la Industria", "Codigo":"ICN", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736148782&idp=1254735576715"}
,{"Id":43, "Cod_IOE":"30203", "Nombre":"Explotación Estadística del Directorio Central de Empresas", "Codigo":"DIR", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736160707&idp=1254735576550"}
,{"Id":44, "Cod_IOE":"30198", "Nombre":"Encuesta sobre Comercio Internacional de Servicios y otras Operaciones Internacionales", "Codigo":"ICES", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736174702&idp=1254735576778"}
,{"Id":48, "Cod_IOE":"30071", "Nombre":"Índices de Precios de Exportación y de Importación de Productos Industriales", "Codigo":"IPRX-M", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736148943&idp=1254735576715"}
,{"Id":49, "Cod_IOE":"", "Nombre":"Distribución de Apellidos", "Codigo":"APEL", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177009&idp=1254735572981"}
,{"Id":51, "Cod_IOE":"30019", "Nombre":"Contabilidad Nacional Trimestral de España. Base 2008", "Codigo":"CNTR2008"}
,{"Id":52, "Cod_IOE":"30269", "Nombre":"Proyecciones de Población a Corto Plazo", "Codigo":"EPOBC"}
,{"Id":54, "Cod_IOE":"30270", "Nombre":"Proyecciones de Población a Largo Plazo", "Codigo":"EPOBL"}
,{"Id":61, "Cod_IOE":"30222", "Nombre":"Índice de Precios de Apartamentos Turísticos", "Codigo":"IPAP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176962&idp=1254735576863"}
,{"Id":62, "Cod_IOE":"30223", "Nombre":"Índice de Precios de Camping", "Codigo":"IPAC", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176961&idp=1254735576863"}
,{"Id":63, "Cod_IOE":"30229", "Nombre":"Índice de Precios de Alojamientos de Turismo Rural", "Codigo":"IPTR", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176963&idp=1254735576863"}
,{"Id":66, "Cod_IOE":"30463", "Nombre":"Estadística de Nulidades, Separaciones y Divorcios", "Codigo":"ENSD", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176798&idp=1254735573206"}
,{"Id":71, "Cod_IOE":"30277", "Nombre":"Estadística de Migraciones", "Codigo":"EM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177000&idp=1254735573002"}
,{"Id":72, "Cod_IOE":"30321", "Nombre":"Cifras de Población", "Codigo":"CP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176951&idp=1254735572981"}
,{"Id":93, "Cod_IOE":"30049", "Nombre":"Encuesta Industrial Anual de Productos", "Codigo":"EIAP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736149053&idp=1254735576715"}
,{"Id":104, "Cod_IOE":"30062", "Nombre":"Índices de Precios de Materiales y Energía e Índices Nacionales de la Mano de Obra", "Codigo":"IMM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736154972&idp=1254735576757"}
,{"Id":121, "Cod_IOE":"30133", "Nombre":"Encuesta Cuatrienal de Estructura Salarial", "Codigo":"EAES:Q", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177025&idp=1254735976596"}
,{"Id":125, "Cod_IOE":"30151", "Nombre":"Estadística de Sociedades Mercantiles", "Codigo":"SM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177026&idp=1254735576550"}
,{"Id":130, "Cod_IOE":"30177", "Nombre":"Estadística Estructural de Empresas: Sector Servicios", "Codigo":"EEE:SER", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176865&idp=1254735576778"}
,{"Id":132, "Cod_IOE":"30179", "Nombre":"Índice de Precios Hoteleros", "Codigo":"IPH", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177015&idp=1254735576863"}
,{"Id":137, "Cod_IOE":"30185", "Nombre":"Índice de Precios del Trabajo", "Codigo":"IPT", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177027&idp=1254735976596"}
,{"Id":139, "Cod_IOE":"30188", "Nombre":"Encuesta Anual de Coste Laboral", "Codigo":"EACL", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736060920&idp=1254735976596"}
,{"Id":140, "Cod_IOE":"30189", "Nombre":"Encuesta Anual de Estructura Salarial", "Codigo":"EAES", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177025&idp=1254735976596"}
,{"Id":155, "Cod_IOE":"30453", "Nombre":"Encuesta de Condiciones de Vida (ECV)", "Codigo":"ECV", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176807&idp=1254735976608"}
,{"Id":163, "Cod_IOE":"30199", "Nombre":"Indicadores de Confianza Empresarial", "Codigo":"ICE", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736163552&idp=1254735576550"}
,{"Id":171, "Cod_IOE":"30221", "Nombre":"Estadística sobre Transporte Ferroviario", "Codigo":"TF", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177040&idp=1254735576820"}
,{"Id":180, "Cod_IOE":"30230", "Nombre":"Indicadores de Rentabilidad del Sector Hotelero", "Codigo":"IRSH", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177015&idp=1254735576863"}
,{"Id":197, "Cod_IOE":"30271", "Nombre":"Tablas de Mortalidad", "Codigo":"TM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177004&idp=1254735573002"}
,{"Id":205, "Cod_IOE":"30310", "Nombre":"Flujos de la Población Activa", "Codigo":"EFPA", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176907&idp=1254735976595"}
,{"Id":212, "Cod_IOE":"30465", "Nombre":"Estadística de Juzgados de Paz", "Codigo":"EJP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176794&idp=1254735573206"}
,{"Id":213, "Cod_IOE":"30466", "Nombre":"Estadística de Condenados: Adultos", "Codigo":"CONA", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176793&idp=1254735573206"}
,{"Id":214, "Cod_IOE":"30467", "Nombre":"Estadística de Condenados: Menores", "Codigo":"CONM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176795&idp=1254735573206"}
,{"Id":215, "Cod_IOE":"30468", "Nombre":"Estadística de Violencia Doméstica y Violencia de Género", "Codigo":"VGD", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176866&idp=1254735573206"}
,{"Id":234, "Cod_IOE":"30209", "Nombre":"Estadística de Movilidad Laboral y Geográfica", "Codigo":"EMLG", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176909&idp=1254735976597"}
,{"Id":237, "Cod_IOE":"30024", "Nombre":"Contabilidad Nacional Trimestral de España: Principales Agregados", "Codigo":"CNTR2010", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736164439&idp=1254735576581"}
,{"Id":238, "Cod_IOE":"30235", "Nombre":"Encuesta de Ocupación Hotelera", "Codigo":"EOH", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177015&idp=1254735576863"}
,{"Id":239, "Cod_IOE":"30236", "Nombre":"Encuesta de Ocupación en Apartamentos Turísticos", "Codigo":"EOAP", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176962&idp=1254735576863"}
,{"Id":240, "Cod_IOE":"30237", "Nombre":"Encuesta de Ocupación en Campings", "Codigo":"EOAC", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176961&idp=1254735576863"}
,{"Id":241, "Cod_IOE":"30238", "Nombre":"Encuesta de Ocupación en Alojamientos de Turismo Rural", "Codigo":"EOTR", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176963&idp=1254735576863"}
,{"Id":246, "Cod_IOE":"30026", "Nombre":"Cuentas Trimestrales no Financieras de los Sectores Institucionales", "Codigo":"CTNFSI", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736165305&idp=1254735576581"}
,{"Id":247, "Cod_IOE":"30023", "Nombre":"Contabilidad Nacional de España. Base 2010", "Codigo":"CNE", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736165950&idp=1254735576581"}
,{"Id":249, "Cod_IOE":"30063", "Nombre":"Encuesta Coyuntural sobre Stocks y Existencias", "Codigo":"ECSE", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176995&idp=1254735576799"}
,{"Id":250, "Cod_IOE":"30234", "Nombre":"Índice de Producción del Sector Servicios", "Codigo":"IPSS", "Url":"https://ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177099&idp=1254735576778"}
,{"Id":254, "Cod_IOE":"30220", "Nombre":"Índice de ingresos hoteleros", "Codigo":"IIH"}
,{"Id":256, "Cod_IOE":"30232", "Nombre":"Estadística Estructural de Empresas: Sector Comercio", "Codigo":"EEE:COM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176902&idp=1254735576799"}
,{"Id":258, "Cod_IOE":"30083", "Nombre":"Índice de Cifra de Negocios Empresarial", "Codigo":"ICNE", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176958&idp=1254735576550"}
,{"Id":259, "Cod_IOE":"30153", "Nombre":"Estadística sobre Ejecuciones Hipotecarias", "Codigo":"EH", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176993&idp=1254735576606"}
,{"Id":293, "Cod_IOE":"30308", "Nombre":"Encuesta de Población Activa (EPA)", "Codigo":"EPA", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176918&idp=1254735976595"}
,{"Id":297, "Cod_IOE":"30163", "Nombre":"Estadística de Transporte de Viajeros", "Codigo":"TV", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820"}
,{"Id":303, "Cod_IOE":"30187", "Nombre":"Encuesta Trimestral de Coste Laboral (ETCL)", "Codigo":"ETCL", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736045053&idp=1254735976596"}
,{"Id":305, "Cod_IOE":"30302", "Nombre":"MNP Estadística de Matrimonios", "Codigo":"MNPM", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176999&idp=1254735573002"}
,{"Id":307, "Cod_IOE":"30304", "Nombre":"MNP Estadística de Nacimientos", "Codigo":"MNPN", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177007&idp=1254735573002"}
,{"Id":309, "Cod_IOE":"30306", "Nombre":"MNP Estadística de Defunciones", "Codigo":"MNPD", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177008&idp=1254735573002"}
,{"Id":314, "Cod_IOE":"30458", "Nombre":"Encuesta de Presupuestos Familiares (EPF)", "Codigo":"EPF", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176806&idp=1254735976608"}
,{"Id":328, "Cod_IOE":"30239", "Nombre":"Encuesta de Ocupación en Albergues", "Codigo":"EOA", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176964&idp=1254735576863"}
,{"Id":329, "Cod_IOE":"16029", "Nombre":"Encuesta de Gasto Turístico", "Codigo":"EG", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177002&idp=1254735576863"}
,{"Id":330, "Cod_IOE":"16028", "Nombre":"Movimientos Turísticos en Fronteras", "Codigo":"FR", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176996&idp=1254735576863"}
,{"Id":331, "Cod_IOE":"", "Nombre":"Índice de Garantía de la Competitividad", "Codigo":"IGC", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177109&idp=1254735976607"}
,{"Id":333, "Cod_IOE":"30456", "Nombre":"Mujeres y Hombres en España", "Codigo":"MYH", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176984&idp=1254735576508"}
,{"Id":334, "Cod_IOE":"16023", "Nombre":"Encuesta de turismo de residentes", "Codigo":"ETR", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176990&idp=1254735576863"}
,{"Id":336, "Cod_IOE":"30279", "Nombre":"Estadística de Adquisiciones de Nacionalidad Española de Residentes", "Codigo":"ANES", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177001&idp=1254735573002"}
,{"Id":345, "Cod_IOE":"30030", "Nombre":"Contabilidad nacional anual de España: agregados por rama de actividad", "Codigo":"CNEAG", "Url":"/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177056&idp=1254735576581"}
,{"Id":353, "Cod_IOE":"30325", "Nombre":"Atlas de distribución de renta de los hogares", "Codigo":"ADRH", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177088&idp=1254735976608"}
,{"Id":402, "Cod_IOE":"", "Nombre":"Movilidad COVID19", "Codigo":"MMOV", "Url":"https://www.ine.es/experimental/movilidad/experimental_em.htm"}
,{"Id":406, "Cod_IOE":"30324", "Nombre":"Estimacion del numero de defunciones semanales (EDeS)", "Codigo":"EDES", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177074&idp=1254735573002"}
,{"Id":407, "Cod_IOE":"", "Nombre":"Encuesta Cuatrienal de Estructural Salarial", "Codigo":"EAES:Q"}
,{"Id":410, "Cod_IOE":"", "Nombre":"Viviendas turísticas en España", "Codigo":"VTE", "Url":"https://www.ine.es/experimental/viv_turistica/experimental_viv_turistica.htm"}
,{"Id":412, "Cod_IOE":"", "Nombre":"Distribución del gasto en destino realizado por los visitantes extranjeros en sus visitas a España", "Codigo":"GDVE", "Url":"https://www.ine.es/experimental/gasto_tarjetas/trimestral.htm"}
,{"Id":424, "Cod_IOE":"30323", "Nombre":"Estimación Mensual de Nacimientos", "Codigo":"EMN", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177079&idp=1254735573002"}
,{"Id":425, "Cod_IOE":"", "Nombre":"Comercio diario al por menor de grandes empresas", "Codigo":"CDMGE", "Url":"https://www.ine.es/experimental/cdmge/"}
,{"Id":426, "Cod_IOE":"", "Nombre":"Coyuntura demográfica de empresas", "Codigo":"CODEM", "Url":"https://www.ine.es/experimental/codem/experimental_codem.htm"}
,{"Id":429, "Cod_IOE":"", "Nombre":"Ocupación en alojamientos turísticos", "Codigo":"OAT", "Url":"https://www.ine.es/experimental/ocupacion/experimental_ocupacion.htm"}
,{"Id":432, "Cod_IOE":"", "Nombre":"Índice de Precios de Vivienda en Alquiler", "Codigo":"IPVA"}
,{"Id":433, "Cod_IOE":"", "Nombre":"Indicador Multidimensional de Calidad de Vida", "Codigo":"IMCV", "Url":"https://www.ine.es/experimental/imcv/experimental_ind_multi_calidad_vida.htm"}
,{"Id":436, "Cod_IOE":"", "Nombre":"Medición del turismo receptor a partir de la posición de los teléfonos móviles", "Codigo":"TMOV", "Url":"https://www.ine.es/experimental/turismo_moviles/experimental_turismo_moviles.htm#!turismo_receptor"}
,{"Id":437, "Cod_IOE":"", "Nombre":"Medición del turismo emisor a partir de la posición de los teléfonos móviles", "Codigo":"TMOV", "Url":"https://www.ine.es/experimental/turismo_moviles/experimental_turismo_moviles.htm#!turismo_emisor"}
,{"Id":438, "Cod_IOE":"", "Nombre":"Medición del turismo interno interprovincial a partir de la posición de los teléfonos móviles", "Codigo":"TMOV", "Url":"https://www.ine.es/experimental/turismo_moviles/experimental_turismo_moviles_interno.htm"}
,{"Id":450, "Cod_IOE":"30282", "Nombre":"Estadística Continua de Población", "Codigo":"ECP", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177095&idp=1254735572981"}
,{"Id":452, "Cod_IOE":"", "Nombre":"Distribución del gasto realizado por los residentes en sus visitas al Extranjero según país de destino", "Codigo":"GDRE", "Url":"https://www.ine.es/experimental/turismo_gasto/turistas_residentes_gasto_extranjero.htm"}
,{"Id":455, "Cod_IOE":"30283", "Nombre":"Estadística de Migraciones y Cambios de Residencia", "Codigo":"EMCR", "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177098&idp=1254735573002"}
,{"Id":464, "Cod_IOE":"30098", "Nombre":"Comercio Internacional de Servicios por Modos de Suministro (MoS)", "Codigo":"MOS", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177111&idp=1254735576778"}
,{"Id":465, "Cod_IOE":"30240", "Nombre":"Comercio Internacional de Servicios por Características de las Empresas (STEC)", "Codigo":"STEC", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177112&idp=1254735576778"}
,{"Id":474, "Cod_IOE":"30099", "Nombre":"Estadística sobre Cadenas de Valor Globales", "Codigo":"ECVG", "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177116&idp=1254735576550"}
,{"Id":476, "Cod_IOE":"", "Nombre":"Cuentas de Emisiones a la Atmósfera Trimestrales", "Codigo":"CMEA", "Url":"https://www.ine.es/experimental/ceatr/experimental_ceatr.htm"}
]


Pu = [{"Id":1, "Nombre":"Coyuntura Turística Hotelera (EOH/IPH/IRSH)", "FK_Periodicidad":1, "FK_PubFechaAct":11549}
,{"Id":2, "Nombre":"Encuesta de ocupación en alojamientos turísticos extrahoteleros", "FK_Periodicidad":1, "FK_PubFechaAct":12904}
,{"Id":3, "Nombre":"Hipotecas Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":11581}
,{"Id":4, "Nombre":"Indicadores de actividad del sector servicios", "FK_Periodicidad":1, "FK_PubFechaAct":11578}
,{"Id":5, "Nombre":"Índices de Comercio al por menor", "FK_Periodicidad":1, "FK_PubFechaAct":11554}
,{"Id":6, "Nombre":"Índice de Cifras de Negocios en la Industria", "FK_Periodicidad":1, "FK_PubFechaAct":11577}
,{"Id":7, "Nombre":"Índice de Entradas de Pedidos en la Industria", "FK_Periodicidad":1, "FK_PubFechaAct":8079}
,{"Id":8, "Nombre":"Índice de Precios de Consumo", "FK_Periodicidad":1, "FK_PubFechaAct":11569}
,{"Id":9, "Nombre":"Índices de Precios de Consumo Armonizado", "FK_Periodicidad":1, "FK_PubFechaAct":11570}
,{"Id":10, "Nombre":"Índice de Producción Industrial", "FK_Periodicidad":1, "FK_PubFechaAct":11563}
,{"Id":11, "Nombre":"Índice de Precios Industriales", "FK_Periodicidad":1, "FK_PubFechaAct":11551}
,{"Id":12, "Nombre":"Índices de Precios de Exportación (IPRIX) y de Importación (IPRIM) de Productos Industriales", "FK_Periodicidad":1, "FK_PubFechaAct":11555}
,{"Id":13, "Nombre":"Estadística de Transporte de Viajeros", "FK_Periodicidad":1, "FK_PubFechaAct":1691}
,{"Id":14, "Nombre":"Contabilidad Nacional Trimestral de España", "FK_Periodicidad":3, "FK_PubFechaAct":11531}
,{"Id":15, "Nombre":"Encuesta de Población Activa", "FK_Periodicidad":3, "FK_PubFechaAct":1512}
,{"Id":18, "Nombre":"Estimaciones de la población actual de España", "FK_Periodicidad":1, "FK_PubFechaAct":601}
,{"Id":19, "Nombre":"Índices de Comercio Exterior de Servicios", "FK_Periodicidad":3, "FK_PubFechaAct":2204}
,{"Id":20, "Nombre":"Índice de Precios del Sector Servicios", "FK_Periodicidad":3, "FK_PubFechaAct":11571}
,{"Id":21, "Nombre":"Índice de Precios de Vivienda", "FK_Periodicidad":3, "FK_PubFechaAct":11565}
,{"Id":22, "Nombre":"Efectos Impagados", "FK_Periodicidad":1, "FK_PubFechaAct":2764}
,{"Id":24, "Nombre":"Sociedades Mercantiles Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":11568}
,{"Id":25, "Nombre":"Z_Avance del PIB trimestral", "FK_Periodicidad":3, "FK_PubFechaAct":2187}
,{"Id":26, "Nombre":"Cuentas Trimestrales no Financieras de los Sectores Institucionales", "FK_Periodicidad":3, "FK_PubFechaAct":11505}
,{"Id":27, "Nombre":"Índice de Coste Laboral Armonizado", "FK_Periodicidad":3, "FK_PubFechaAct":11566}
,{"Id":28, "Nombre":"Estadística de Transmisiones de Derechos de la Propiedad", "FK_Periodicidad":1, "FK_PubFechaAct":11572}
,{"Id":29, "Nombre":"Cifras oficiales de población de los municipios españoles: revisión del Padrón municipal", "FK_Periodicidad":12, "FK_PubFechaAct":11746}
,{"Id":30, "Nombre":"Explotación Estadística del Directorio Central de Empresas", "FK_Periodicidad":12, "FK_PubFechaAct":11799}
,{"Id":31, "Nombre":"Censos Anuales de Población. Variables demográficas, estado civil, ocupación y actividad.", "FK_Periodicidad":12, "FK_PubFechaAct":11744}
,{"Id":32, "Nombre":"Encuesta de Población Activa. Media anual de los cuatro trimestres", "FK_Periodicidad":12, "FK_PubFechaAct":1787}
,{"Id":33, "Nombre":"Encuesta de Población Activa", "FK_Periodicidad":6, "FK_PubFechaAct":1833}
,{"Id":38, "Nombre":"Indicadores Demográficos Básicos", "FK_Periodicidad":12, "FK_PubFechaAct":12919}
,{"Id":39, "Nombre":"Indicadores Demográficos Básicos", "FK_Periodicidad":1, "FK_PubFechaAct":1185}
,{"Id":40, "Nombre":"Índice de Precios de Consumo. Medias anuales", "FK_Periodicidad":12, "FK_PubFechaAct":11932}
,{"Id":46, "Nombre":"Índice de Precios Industriales Anual", "FK_Periodicidad":12, "FK_PubFechaAct":311}
,{"Id":47, "Nombre":"Índice de Producción Industrial Anual", "FK_Periodicidad":12, "FK_PubFechaAct":316}
,{"Id":48, "Nombre":"Índice de Precios de Vivienda. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":12059}
,{"Id":49, "Nombre":"Índice de Precios de Vivienda. Medias Anuales", "FK_Periodicidad":12, "FK_PubFechaAct":11990}
,{"Id":50, "Nombre":"Índices de Comercio al por menor. Trimestral", "FK_Periodicidad":3, "FK_PubFechaAct":1361}
,{"Id":53, "Nombre":"Índice de Entradas de Pedidos en la Industria. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":4418}
,{"Id":55, "Nombre":"Índice de Cifras de Negocios en la Industria. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":10805}
,{"Id":57, "Nombre":"Estadística Estructural de Empresas: Sector Industrial", "FK_Periodicidad":12, "FK_PubFechaAct":12031}
,{"Id":58, "Nombre":"Encuesta de coyuntura de comercio al por menor. Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":350}
,{"Id":59, "Nombre":"Encuesta de coyuntura de comercio al por menor. Trimestral", "FK_Periodicidad":3, "FK_PubFechaAct":351}
,{"Id":60, "Nombre":"Proyecciones de Población a largo plazo", "FK_Periodicidad":12, "FK_PubFechaAct":4396}
,{"Id":61, "Nombre":"Indicadores de Confianza Empresarial", "FK_Periodicidad":3, "FK_PubFechaAct":11515}
,{"Id":63, "Nombre":"Encuesta sobre métodos de producción en las explotaciones agrícolas", "FK_Periodicidad":12, "FK_PubFechaAct":609}
,{"Id":64, "Nombre":"Nomenclátor: Población por Unidad Poblacional", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177010&idp=1254735572981", "FK_PubFechaAct":11737}
,{"Id":65, "Nombre":"Estadística del padron continuo", "FK_Periodicidad":12, "FK_PubFechaAct":9596}
,{"Id":66, "Nombre":"Tablas de mortalidad", "FK_Periodicidad":12, "FK_PubFechaAct":11743}
,{"Id":67, "Nombre":"Relación de municipios, provincias, comunidades autónomas y sus códigos", "FK_Periodicidad":12, "FK_PubFechaAct":11738}
,{"Id":68, "Nombre":"Estadística estructural de empresas: Sector Comercio", "FK_Periodicidad":12, "FK_PubFechaAct":12029}
,{"Id":71, "Nombre":"Indicadores de Crecimiento y Estructura", "FK_Periodicidad":12, "FK_PubFechaAct":12915}
,{"Id":72, "Nombre":"Publicación de Coeficientes de enlace del IPC", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":74, "Nombre":"Estadística de defunciones según la causa de muerte", "FK_Periodicidad":12, "FK_PubFechaAct":11771}
,{"Id":75, "Nombre":"Estadística de producción editorial de Libros", "FK_Periodicidad":12, "FK_PubFechaAct":8904}
,{"Id":76, "Nombre":"Estadística del padrón de españoles residentes en el extranjero", "FK_Periodicidad":12, "FK_PubFechaAct":11733}
,{"Id":77, "Nombre":"Estadística sobre el uso de biotecnología", "FK_Periodicidad":12, "FK_PubFechaAct":11772}
,{"Id":78, "Nombre":"Indicadores de Alta Tecnología", "FK_Periodicidad":12, "FK_PubFechaAct":12775}
,{"Id":79, "Nombre":"Apellidos y nombres más frecuentes", "FK_Periodicidad":12, "FK_PubFechaAct":11740}
,{"Id":80, "Nombre":"Apellidos más frecuentes", "FK_Periodicidad":12, "FK_PubFechaAct":12042}
,{"Id":81, "Nombre":"Estadística de la Enseñanza Universitaria", "FK_Periodicidad":12, "FK_PubFechaAct":641}
,{"Id":82, "Nombre":"Contabilidad Regional de España. Base 2008", "FK_Periodicidad":12, "FK_PubFechaAct":1797}
,{"Id":84, "Nombre":"Estadística estructural de empresas: Sector Servicios", "FK_Periodicidad":12, "FK_PubFechaAct":12030}
,{"Id":85, "Nombre":"Estadística de Productos en el Sector Servicios", "FK_Periodicidad":12, "FK_PubFechaAct":11776}
,{"Id":87, "Nombre":"Encuesta de Estructura Salarial", "FK_Periodicidad":105, "FK_PubFechaAct":11890}
,{"Id":88, "Nombre":"Encuesta Industrial Anual de Productos", "FK_Periodicidad":12, "FK_PubFechaAct":11774}
,{"Id":90, "Nombre":"Estadística de Profesionales Sanitarios Colegiados", "FK_Periodicidad":12, "FK_PubFechaAct":11761}
,{"Id":91, "Nombre":"Estadística de Juzgados de Paz", "FK_Periodicidad":12, "FK_PubFechaAct":6711}
,{"Id":92, "Nombre":"Indicadores del Sector de Tecnologías de la Información y las Comunicaciones (TIC)", "FK_Periodicidad":12, "FK_PubFechaAct":11781}
,{"Id":93, "Nombre":"Estadística de Variaciones Residenciales", "FK_Periodicidad":12, "FK_PubFechaAct":9429}
,{"Id":94, "Nombre":"Encuesta sobre el Uso de Tecnologías de la Información y las Comunicaciones y del Comercio Electrónico en las Empresas", "FK_Periodicidad":12, "FK_PubFechaAct":12874}
,{"Id":95, "Nombre":"Estadística de Litigios en Arrendamientos Urbanos", "FK_Periodicidad":12, "FK_PubFechaAct":8726}
,{"Id":96, "Nombre":"Módulo de la Encuesta de Población Activa ( Empleo de las personas con discapacidad)", "FK_Periodicidad":12, "FK_PubFechaAct":656}
,{"Id":97, "Nombre":"Encuesta sobre el uso del agua en el sector agrario", "FK_Periodicidad":12, "FK_PubFechaAct":8132}
,{"Id":98, "Nombre":"Proyecciones de Población a corto plazo", "FK_Periodicidad":12, "FK_PubFechaAct":1417}
,{"Id":100, "Nombre":"Estadísticas sobre las actividades de protección medioambiental", "FK_Periodicidad":12, "FK_PubFechaAct":11793}
,{"Id":101, "Nombre":"Encuesta de financiación y gastos de la enseñanza privada", "FK_Periodicidad":12, "FK_PubFechaAct":9557}
,{"Id":103, "Nombre":"Contabilidad Nacional de España. Base 2010", "FK_Periodicidad":12, "FK_PubFechaAct":4563}
,{"Id":104, "Nombre":"Estadísticas sobre generación de residuos", "FK_Periodicidad":12, "FK_PubFechaAct":11792}
,{"Id":105, "Nombre":"Censo Agrario", "FK_Periodicidad":12, "FK_PubFechaAct":9271}
,{"Id":106, "Nombre":"Estadística de nulidades, separaciones y divorcios", "FK_Periodicidad":12, "FK_PubFechaAct":11764}
,{"Id":107, "Nombre":"Estadística de filiales de empresas españolas en el exterior", "FK_Periodicidad":12, "FK_PubFechaAct":11783}
,{"Id":108, "Nombre":"Estadística de Condenados: Adultos", "FK_Periodicidad":12, "FK_PubFechaAct":12903}
,{"Id":109, "Nombre":"Estadística de Condenados: Menores", "FK_Periodicidad":12, "FK_PubFechaAct":11766}
,{"Id":110, "Nombre":"Estadística de Empresas según su pertenencia a grupos", "FK_Periodicidad":12, "FK_PubFechaAct":11782}
,{"Id":112, "Nombre":"Estadística de Productos en el Sector Comercio", "FK_Periodicidad":12, "FK_PubFechaAct":11775}
,{"Id":113, "Nombre":"Encuesta Continua de Hogares", "FK_Periodicidad":12, "FK_PubFechaAct":8645}
,{"Id":114, "Nombre":"Base de Datos de Información Demográfica (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":115, "Nombre":"Proyección de Hogares", "FK_Periodicidad":12, "FK_PubFechaAct":10664}
,{"Id":116, "Nombre":"Estadística de Migraciones", "FK_Periodicidad":12, "FK_PubFechaAct":10065}
,{"Id":117, "Nombre":"Cifras de Población", "FK_Periodicidad":6, "FK_PubFechaAct":9547}
,{"Id":118, "Nombre":"Organización (normalización definiciones estándares)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":119, "Nombre":"Cuenta Satélite del Turismo (CST)", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":120, "Nombre":"Contabilidad Nacional de España. Base 2000", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":121, "Nombre":"Contabilidad Regional de España. Base 2000", "FK_Periodicidad":12, "FK_PubFechaAct":1247}
,{"Id":123, "Nombre":"Cuentas Satélite de las Cooperativas y Mutualidades", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":124, "Nombre":"Contabilidad Nacional de España. Base 2008. Tablas de Origen y Destino. ", "FK_Periodicidad":12, "FK_PubFechaAct":1347}
,{"Id":127, "Nombre":"Cuenta Satélite del Turismo de España. Base 2008", "FK_Periodicidad":12, "FK_PubFechaAct":1784}
,{"Id":129, "Nombre":"Registro Estadístico de Explotaciones Agrarias", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":131, "Nombre":"Encuesta sobre la Estructura de las Explotaciones Agrícolas", "FK_Periodicidad":12, "FK_PubFechaAct":12024}
,{"Id":133, "Nombre":"Directorio de Empresas y Organismos Públicos Posibles Investigadores", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":135, "Nombre":"Estadística sobre Actividades en I+D en el Sector Administración Pública", "FK_Periodicidad":12, "FK_PubFechaAct":12891}
,{"Id":136, "Nombre":"Estadística sobre Actividades en I+D en el Sector Instituciones Privadas", "FK_Periodicidad":12, "FK_PubFechaAct":12893}
,{"Id":137, "Nombre":"Estadística sobre Actividades en I+D en el Sector Enseñanza Superior", "FK_Periodicidad":12, "FK_PubFechaAct":12892}
,{"Id":138, "Nombre":"Encuesta sobre Innovación en las Empresas", "FK_Periodicidad":12, "FK_PubFechaAct":11795}
,{"Id":140, "Nombre":"Consumos Intermedios e Inversión", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":141, "Nombre":"Indicadores de Globalización (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":142, "Nombre":"Sistema de Recogida de Información Económica sobre el Medio Ambiente", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":143, "Nombre":"Estadísticas Medioambientales sobre el Agua", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":145, "Nombre":"Encuesta de Consumos Energéticos", "FK_Periodicidad":12, "FK_PubFechaAct":11773}
,{"Id":146, "Nombre":"Cuentas Ambientales", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":147, "Nombre":"Indicadores de Desarrollo Sostenible", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":148, "Nombre":"Indicadores Agroambientales (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":151, "Nombre":"Estadística del taxi ", "FK_Periodicidad":12, "FK_PubFechaAct":6826}
,{"Id":152, "Nombre":"Financiación y Gastos de la Enseñanza Privada", "FK_Periodicidad":12, "FK_PubFechaAct":661}
,{"Id":153, "Nombre":"Encuesta de Coste Laboral", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":158, "Nombre":"Investigación del Alojamiento Privado de Uso Turístico (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":160, "Nombre":"Encuesta de Paridades del Poder Adquisitivo (PPA)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":161, "Nombre":"Índice de precios del trabajo", "FK_Periodicidad":12, "FK_PubFechaAct":11750}
,{"Id":162, "Nombre":"Encuesta Anual de Coste Laboral", "FK_Periodicidad":12, "FK_PubFechaAct":12789}
,{"Id":163, "Nombre":"Encuesta Anual de Estructura Salarial", "FK_Periodicidad":12, "FK_PubFechaAct":11749}
,{"Id":165, "Nombre":"Estadística de Discapacidad y Mercado Laboral: Empleo", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736055502&idp=1254735976621", "FK_PubFechaAct":11756}
,{"Id":169, "Nombre":"Pruebas de Acceso a la Universidad", "FK_Periodicidad":12, "FK_PubFechaAct":948}
,{"Id":170, "Nombre":"Encuesta de Morbilidad Hospitalaria", "FK_Periodicidad":12, "FK_PubFechaAct":11757}
,{"Id":172, "Nombre":"Encuesta de Discapacidad Autonomía Personal y Situaciones de Dependencia", "FK_Periodicidad":100, "FK_PubFechaAct":10585}
,{"Id":173, "Nombre":"Indicadores Sociales", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":174, "Nombre":"Encuesta de Empleo del Tiempo", "FK_Periodicidad":12, "FK_PubFechaAct":6647}
,{"Id":175, "Nombre":"Encuesta sobre Equipamiento y Uso de Tecnologías de Información y Comunicación de los Hogares (TIC-H)", "FK_Periodicidad":12, "FK_PubFechaAct":11770}
,{"Id":176, "Nombre":"Encuesta de Transición Educativa - Formativa e Inserción Laboral", "FK_Periodicidad":12, "FK_PubFechaAct":8222}
,{"Id":178, "Nombre":"Encuesta a las Personas sin Hogar EPSH ", "FK_Periodicidad":12, "FK_PubFechaAct":9519}
,{"Id":179, "Nombre":"Mujeres y Hombres en España", "FK_Periodicidad":12, "FK_PubFechaAct":8102}
,{"Id":181, "Nombre":"Encuesta de Gasto de los Hogares en Educación", "FK_Periodicidad":12, "FK_PubFechaAct":11802}
,{"Id":185, "Nombre":"Desarrollo de Estimadores basados en Modelos", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":186, "Nombre":"Proyecciones de Tasas de Actividad", "FK_Periodicidad":12, "FK_PubFechaAct":3226}
,{"Id":187, "Nombre":"Estadística sobre Transporte Ferroviario", "FK_Periodicidad":3, "FK_PubFechaAct":12909}
,{"Id":189, "Nombre":"Encuesta sobre Recursos Humanos en Ciencia y Tecnología", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":190, "Nombre":"Inventario de Establecimientos Hoteleros (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":194, "Nombre":"Encuesta sobre Acceso a Financiación de las Empresas", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":195, "Nombre":"Censos de Edificios", "FK_Periodicidad":12, "FK_PubFechaAct":1335}
,{"Id":199, "Nombre":"Relación de Unidades Poblacionales con Especificación de su Población", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":200, "Nombre":"Estimaciones intercensales de población", "FK_Periodicidad":12, "FK_PubFechaAct":1326}
,{"Id":201, "Nombre":"Estudio Demográfico Longitudinal (EDL)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":202, "Nombre":"Estimaciones Mensuales de Coyuntura Demográfica", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":203, "Nombre":"Flujos de Permisos de Residencia a Extranjeros (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":205, "Nombre":"Encuesta de Población Residente y Migraciones Exteriores (EPRYME)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":206, "Nombre":"Encuesta Sociodemográfica y de Generaciones (ESOGE) (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":208, "Nombre":"Encuesta Comunitaria de Fuerza de Trabajo (ECFT)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":210, "Nombre":"Encuesta de Migraciones", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":211, "Nombre":"Encuesta Nacional de Inmigrantes", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":212, "Nombre":"Encuesta Europea de Seguridad (en proyecto)", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":218, "Nombre":"Encuesta sobre las Personas sin Hogar (Centros)", "FK_Periodicidad":12, "FK_PubFechaAct":946}
,{"Id":219, "Nombre":"Encuesta de Hogares y Medioambiente", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":220, "Nombre":"Sistema de Información Geográfica Estadística", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":221, "Nombre":"Sistema Datawarehouse para el Sistema de Información Demográfica", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":222, "Nombre":"Anuario Estadístico de España", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":223, "Nombre":"España en Cifras", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":224, "Nombre":"Boletín Mensual de Estadística", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":225, "Nombre":"Banco de Datos TEMPUS 2", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":226, "Nombre":"Banco de Datos INEbase", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":227, "Nombre":"Censos Históricos", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":228, "Nombre":"Codificación Asistida y Automática y Elaboración de las Aplicaciones Inf", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":229, "Nombre":"Adaptación de Clasificaciones Internacionales a la Realidad Nacional", "FK_Periodicidad":100, "FK_PubFechaAct":None}
,{"Id":230, "Nombre":"Encuesta Europea de Salud", "FK_Periodicidad":12, "FK_PubFechaAct":8647}
,{"Id":232, "Nombre":"Encuesta de Inserción Laboral de Graduados Universitarios", "FK_Periodicidad":12, "FK_PubFechaAct":8185}
,{"Id":233, "Nombre":"Encuesta de Integración Social y Salud (EISS)", "FK_Periodicidad":12, "FK_PubFechaAct":1436}
,{"Id":234, "Nombre":"Encuesta Nacional de Salud ", "FK_Periodicidad":12, "FK_PubFechaAct":4464}
,{"Id":235, "Nombre":"Estadística de Movilidad Laboral y Geográfica", "FK_Periodicidad":12, "FK_PubFechaAct":10159}
,{"Id":236, "Nombre":"Publicación para los ambitos geográficos de Territoriales", "FK_Periodicidad":12, "FK_PubFechaAct":8077}
,{"Id":237, "Nombre":"Indicadores de Calidad de Vida. Anual", "FK_Periodicidad":12, "Url":"https://www.ine.es/dynt3/ICV/index.html", "FK_PubFechaAct":11769}
,{"Id":239, "Nombre":"Cuentas de flujos de materiales", "FK_Periodicidad":12, "FK_PubFechaAct":681}
,{"Id":265, "Nombre":"Encuesta sobre la participación de la población adulta en las actividades de aprendizaje", "FK_Periodicidad":12, "FK_PubFechaAct":10201}
,{"Id":266, "Nombre":"Encuesta de población activa (Decil de salarios del empleo)", "FK_Periodicidad":12, "FK_PubFechaAct":1416}
,{"Id":267, "Nombre":"Estadística sobre actividades en I+D", "FK_Periodicidad":12, "FK_PubFechaAct":11790}
,{"Id":268, "Nombre":"Demografía Armonizada de Empresas", "FK_Periodicidad":12, "FK_PubFechaAct":11789}
,{"Id":272, "Nombre":"Estadística del Procedimiento Concursal. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":8796}
,{"Id":273, "Nombre":"Índice de Precios de Consumo a Impuestos Constantes", "FK_Periodicidad":1, "FK_PubFechaAct":3836}
,{"Id":274, "Nombre":"Poblaciones de hecho desde 1900 hasta 1991", "FK_Periodicidad":12, "FK_PubFechaAct":933}
,{"Id":275, "Nombre":"Publicación división DPOD", "FK_Periodicidad":12, "FK_PubFechaAct":934}
,{"Id":280, "Nombre":"Cuenta Satélite de emisiones a la atmósfera. Base 2010", "FK_Periodicidad":12, "FK_PubFechaAct":957}
,{"Id":281, "Nombre":"Impuestos ambientales", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":283, "Nombre":"Encuesta de condiciones de vida. Transmision intergeneracional de la pobreza y el bienestar.", "FK_Periodicidad":12, "FK_PubFechaAct":951}
,{"Id":284, "Nombre":"Contabilidad Nacional Trimestral de España. Base 1995", "FK_Periodicidad":3, "FK_PubFechaAct":953}
,{"Id":287, "Nombre":"Estadística del Procedimiento Concursal", "FK_Periodicidad":3, "FK_PubFechaAct":8769}
,{"Id":288, "Nombre":"Contabilidad Nacional de España. Base 2008. Cuadros contables", "FK_Periodicidad":12, "FK_PubFechaAct":1447}
,{"Id":289, "Nombre":"Hipotecas", "FK_Periodicidad":12, "FK_PubFechaAct":12838}
,{"Id":292, "Nombre":"Transporte de Viajeros. Antigua", "FK_Periodicidad":1, "FK_PubFechaAct":1237}
,{"Id":293, "Nombre":"Encuesta de Población Activa (Variables de submuestra) ", "FK_Periodicidad":12, "FK_PubFechaAct":1328}
,{"Id":297, "Nombre":"Sociedades Mercantiles Anual", "FK_Periodicidad":12, "FK_PubFechaAct":12798}
,{"Id":298, "Nombre":"Estadística de Transmisiones de Derechos de la Propiedad. Resultados anuales", "FK_Periodicidad":12, "FK_PubFechaAct":12839}
,{"Id":299, "Nombre":"Estadística de Efectos de Comercio Impagados. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":3114}
,{"Id":300, "Nombre":"Índice de Precios Industriales. Medias Anuales", "FK_Periodicidad":12, "FK_PubFechaAct":11950}
,{"Id":301, "Nombre":"Índices de Precios de Exportación (IPRIX) y de Importación (IPRIM) de Productos Industriales. Medias anuales", "FK_Periodicidad":12, "FK_PubFechaAct":11955}
,{"Id":306, "Nombre":"Índice de Precios Industriales. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":11947}
,{"Id":307, "Nombre":"Índices de Precios de Exportación (IPRIX) y de Importación (IPRIM) de Productos Industriales. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":11951}
,{"Id":308, "Nombre":"Ponderaciones IPC", "FK_Periodicidad":12, "FK_PubFechaAct":3110}
,{"Id":309, "Nombre":"Estadística de Transporte de Viajeros (Urbano e interurbano)", "FK_Periodicidad":12, "FK_PubFechaAct":1306}
,{"Id":310, "Nombre":"Indicadores de actividad del sector servicios. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":12038}
,{"Id":311, "Nombre":"Censos de Población y Viviendas 2011. Población residente en establecimientos colectivos", "FK_Periodicidad":12, "FK_PubFechaAct":1327}
,{"Id":312, "Nombre":"Estadística de Violencia Doméstica y Violencia de Género", "FK_Periodicidad":12, "FK_PubFechaAct":11762}
,{"Id":313, "Nombre":"Índices de Comercio al por menor. Ponderaciones ", "FK_Periodicidad":12, "FK_PubFechaAct":11971}
,{"Id":315, "Nombre":"Estadística de Discapacidad y Mercado Laboral: Salarios", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176911&idp=1254735976621", "FK_PubFechaAct":11754}
,{"Id":316, "Nombre":"Módulo de la Encuesta de Población Activa. (Transición del mercado laboral a la  jubilación)  ", "FK_Periodicidad":12, "FK_PubFechaAct":1357}
,{"Id":317, "Nombre":"Índice de Producción Industrial. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":10806}
,{"Id":318, "Nombre":"Encuesta sobre centros de atención a personas sin hogar", "FK_Periodicidad":14, "FK_PubFechaAct":12873}
,{"Id":319, "Nombre":"Índice de Precios del Sector Servicios. Medias anuales", "FK_Periodicidad":12, "FK_PubFechaAct":12846}
,{"Id":324, "Nombre":"Contabilidad Nacional de España. Base 2008. Serie 2000-2012. Principales resultados", "FK_Periodicidad":12, "FK_PubFechaAct":1389}
,{"Id":325, "Nombre":"Contabilidad regional de España. Gasto en consumo final de los hogares", "FK_Periodicidad":12, "FK_PubFechaAct":11720}
,{"Id":326, "Nombre":"Índices de Reparto Regional del IVA y los Impuestos Especiales sobre la Cerveza, sobre el Alcohol y Bebidas derivadas y sobre productos Intermedios", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736167628&idp=1254735576581", "FK_PubFechaAct":11721}
,{"Id":327, "Nombre":"Datos anuales (BdE)", "FK_Periodicidad":12, "FK_PubFechaAct":1400}
,{"Id":328, "Nombre":"Datos trimestrales (BdE)", "FK_Periodicidad":3, "FK_PubFechaAct":2545}
,{"Id":329, "Nombre":"Datos mensuales (BdE)", "FK_Periodicidad":1, "FK_PubFechaAct":1402}
,{"Id":330, "Nombre":"Encuesta de Población Activa", "FK_Periodicidad":3, "FK_PubFechaAct":11528}
,{"Id":336, "Nombre":"Encuesta de Población Activa. Semestral", "FK_Periodicidad":6, "FK_PubFechaAct":4513}
,{"Id":337, "Nombre":"Cuentas Medioambientales: Cuenta de Emisiones a la Atmósfera", "FK_Periodicidad":12, "FK_PubFechaAct":11786}
,{"Id":338, "Nombre":"Cuentas Medioambientales: Cuenta de Impuestos Ambientales", "FK_Periodicidad":12, "FK_PubFechaAct":11788}
,{"Id":339, "Nombre":"Cuentas Medioambientales. Cuentas de flujos de materiales", "FK_Periodicidad":12, "FK_PubFechaAct":11797}
,{"Id":340, "Nombre":"Estadísticas sobre Recogida y Tratamiento de Residuos", "FK_Periodicidad":12, "FK_PubFechaAct":11791}
,{"Id":341, "Nombre":"Encuesta de Población Activa. Media de los cuatro trimestres del año", "FK_Periodicidad":12, "FK_PubFechaAct":11829}
,{"Id":342, "Nombre":"Estadísticas sobre el Suministro y Saneamiento del Agua", "FK_Periodicidad":12, "FK_PubFechaAct":10596}
,{"Id":343, "Nombre":"Estadística de Bibliotecas", "FK_Periodicidad":12, "FK_PubFechaAct":6873}
,{"Id":344, "Nombre":"Encuesta de Condiciones de Vida", "FK_Periodicidad":12, "FK_PubFechaAct":12076}
,{"Id":345, "Nombre":"Estadística sobre Ejecuciones Hipotecarias", "FK_Periodicidad":3, "FK_PubFechaAct":11564}
,{"Id":346, "Nombre":"Índice de Cifra de Negocios Empresarial", "FK_Periodicidad":1, "FK_PubFechaAct":11550}
,{"Id":347, "Nombre":"Encuesta de Población Activa. Variables de submuestra.", "FK_Periodicidad":12, "FK_PubFechaAct":11830}
,{"Id":348, "Nombre":"Encuesta de población activa. Decil de salarios del empleo principal", "FK_Periodicidad":12, "Url":"https://ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176918&menu=resultados&idp=1254735976595#!tabs-1254736195128", "FK_PubFechaAct":11755}
,{"Id":349, "Nombre":"Indicadores de Migraciones", "FK_Periodicidad":12, "FK_PubFechaAct":12914}
,{"Id":350, "Nombre":"Encuesta de Condiciones de Vida. Módulo sobre condiciones de la vivienda", "FK_Periodicidad":12, "FK_PubFechaAct":1768}
,{"Id":351, "Nombre":"Cuentas medioambientales. Otras Cuentas Medioamientales", "FK_Periodicidad":12, "FK_PubFechaAct":6645}
,{"Id":352, "Nombre":"Encuesta sobre el uso del agua en el sector industrial manufacturero", "FK_Periodicidad":12, "FK_PubFechaAct":1793}
,{"Id":353, "Nombre":"Ponderaciones IPCA", "FK_Periodicidad":12, "FK_PubFechaAct":11933}
,{"Id":354, "Nombre":"Indicadores de Confianza Empresarial: Módulo de Opinión sobre el entorno empresarial.", "FK_Periodicidad":12, "FK_PubFechaAct":8031}
,{"Id":355, "Nombre":"Estadística de Transporte de Viajeros", "FK_Periodicidad":1, "FK_PubFechaAct":11567}
,{"Id":356, "Nombre":"Estadística de Transporte de Viajeros (Urbano e interurbano)", "FK_Periodicidad":12, "FK_PubFechaAct":1972}
,{"Id":357, "Nombre":"Encuesta sobre el tiempo de trabajo", "FK_Periodicidad":12, "FK_PubFechaAct":1844}
,{"Id":358, "Nombre":"Encuesta de salarios en la industria y los servicios", "FK_Periodicidad":3, "FK_PubFechaAct":1845}
,{"Id":359, "Nombre":"Índice de Cifra de Negocios Empresarial. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":10808}
,{"Id":360, "Nombre":"Encuesta Trimestral de Coste Laboral", "FK_Periodicidad":3, "FK_PubFechaAct":11573}
,{"Id":363, "Nombre":"Censos de población y viviendas. Población vinculada", "FK_Periodicidad":12, "FK_PubFechaAct":1920}
,{"Id":364, "Nombre":"Movimiento Natural de la Población", "FK_Periodicidad":1, "FK_PubFechaAct":12866}
,{"Id":365, "Nombre":"Movimiento Natural de Población (Matrimonios, Nacimientos y Defunciones)", "FK_Periodicidad":12, "FK_PubFechaAct":12910}
,{"Id":370, "Nombre":"Cambio de base poblacional en la EPA. Series revisadas 2002-", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":372, "Nombre":"Cambio de base poblacional en la EPA. Series revisadas 2002-", "FK_Periodicidad":12, "FK_PubFechaAct":1993}
,{"Id":373, "Nombre":"Índice de Coste Laboral Armonizado. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":12063}
,{"Id":374, "Nombre":"Encuesta de Población Activa. Módulos. Base poblacional 2011", "FK_Periodicidad":12, "FK_PubFechaAct":11751}
,{"Id":377, "Nombre":"Estadística de defunciones según la causa de muerte. Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":12902}
,{"Id":381, "Nombre":"Encuesta de Presupuestos Familiares", "FK_Periodicidad":12, "FK_PubFechaAct":12913}
,{"Id":382, "Nombre":"Datos semestrales (BdE)", "FK_Periodicidad":6, "FK_PubFechaAct":2053}
,{"Id":383, "Nombre":"Contabilidad Nacional de España. Base 2010. Principales resultados", "FK_Periodicidad":12, "FK_PubFechaAct":4495}
,{"Id":386, "Nombre":"Encuesta de  turismo de residentes", "FK_Periodicidad":1, "FK_PubFechaAct":None}
,{"Id":388, "Nombre":"Índices de precios de materiales y nacional de la mano de obra", "FK_Periodicidad":1, "FK_PubFechaAct":12782}
,{"Id":398, "Nombre":"El Salario de las Personas con Discapacidad", "FK_Periodicidad":105, "FK_PubFechaAct":2078}
,{"Id":399, "Nombre":"Estadística de Flujos de la Población Activa", "FK_Periodicidad":3, "FK_PubFechaAct":11527}
,{"Id":400, "Nombre":"Proyecciones de Población", "FK_Periodicidad":12, "FK_PubFechaAct":10899}
,{"Id":401, "Nombre":"Notas de prensa Demografia", "FK_Periodicidad":100, "FK_PubFechaAct":2147}
,{"Id":402, "Nombre":"Contabilidad Nacional de España. Base 2010.  Cuadros contables", "FK_Periodicidad":12, "FK_PubFechaAct":2146}
,{"Id":403, "Nombre":"Contabilidad Regional de España", "FK_Periodicidad":12, "FK_PubFechaAct":11730}
,{"Id":404, "Nombre":"Avance de la Estadística sobre Actividades en I+D", "FK_Periodicidad":12, "FK_PubFechaAct":2148}
,{"Id":405, "Nombre":"Indicadores Urbanos", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176957&idp=1254735976608", "FK_PubFechaAct":11760}
,{"Id":406, "Nombre":"Encuesta de Comercio Internacional de Servicios", "FK_Periodicidad":3, "FK_PubFechaAct":10135}
,{"Id":407, "Nombre":"Movimientos Turísticos en Fronteras", "FK_Periodicidad":1, "FK_PubFechaAct":11561}
,{"Id":408, "Nombre":"Encuesta de Gasto Turístico Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":11560}
,{"Id":409, "Nombre":"Encuesta de turismo de residentes", "FK_Periodicidad":3, "FK_PubFechaAct":None}
,{"Id":410, "Nombre":"Efectos Impagados. Trimestral", "FK_Periodicidad":3, "FK_PubFechaAct":2762}
,{"Id":411, "Nombre":"Datos anuales (IGAE)", "FK_Periodicidad":12, "FK_PubFechaAct":2485}
,{"Id":412, "Nombre":"Datos mensuales (IGAE)", "FK_Periodicidad":1, "FK_PubFechaAct":2486}
,{"Id":413, "Nombre":"Datos mensuales (AEAT)", "FK_Periodicidad":1, "FK_PubFechaAct":2487}
,{"Id":414, "Nombre":"Encuesta sobre Movilidad Internacional de los Estudiantes", "FK_Periodicidad":12, "FK_PubFechaAct":2502}
,{"Id":415, "Nombre":"Estadística sobre Ejecuciones Hipotecarias. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":12833}
,{"Id":416, "Nombre":"Datos trimestrales (IGAE)", "FK_Periodicidad":3, "FK_PubFechaAct":2543}
,{"Id":417, "Nombre":"Índice de Garantía de la Competitividad", "FK_Periodicidad":1, "FK_PubFechaAct":11576}
,{"Id":418, "Nombre":"IMM Coeficientes de enlace", "FK_Periodicidad":1, "FK_PubFechaAct":2560}
,{"Id":420, "Nombre":"Encuesta de condiciones de Vida. Módulos.", "FK_Periodicidad":12, "FK_PubFechaAct":11759}
,{"Id":424, "Nombre":"Contabilidad Nacional de España. Base 2010. Tablas de Origen y Destino", "FK_Periodicidad":12, "FK_PubFechaAct":4527}
,{"Id":427, "Nombre":"Mujeres y Hombres en España. Empleo", "FK_Periodicidad":12, "FK_PubFechaAct":12046}
,{"Id":429, "Nombre":"Encuesta de Población Activa. Módulos. Base poblacional 2001", "FK_Periodicidad":12, "FK_PubFechaAct":2603}
,{"Id":443, "Nombre":"Encuesta de  turismo de residentes. Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":12831}
,{"Id":444, "Nombre":"Encuesta de Comercio Internacional de Servicios", "FK_Periodicidad":12, "FK_PubFechaAct":10167}
,{"Id":445, "Nombre":"Encuesta de turismo de residentes", "FK_Periodicidad":3, "FK_PubFechaAct":11498}
,{"Id":447, "Nombre":"Cuentas anuales no Financieras de los Sectores Institucionales.", "FK_Periodicidad":12, "FK_PubFechaAct":11725}
,{"Id":448, "Nombre":"Movimientos turísticos de los españoles", "FK_Periodicidad":1, "FK_PubFechaAct":2691}
,{"Id":449, "Nombre":"Movimientos turísticos de los españoles", "FK_Periodicidad":12, "FK_PubFechaAct":2692}
,{"Id":450, "Nombre":"Encuesta Coyuntural sobre Stocks y Existencias", "FK_Periodicidad":1, "FK_PubFechaAct":11880}
,{"Id":451, "Nombre":"Encuesta Coyuntural sobre Stocks y Existencias. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":12056}
,{"Id":452, "Nombre":"Mujeres y Hombres en España. Salarios", "FK_Periodicidad":12, "FK_PubFechaAct":11987}
,{"Id":453, "Nombre":"Mujeres y Hombres en España. Educación", "FK_Periodicidad":12, "FK_PubFechaAct":12864}
,{"Id":454, "Nombre":"Mujeres y Hombres en España. Ciencia", "FK_Periodicidad":12, "FK_PubFechaAct":11936}
,{"Id":455, "Nombre":"Mujeres y Hombres en España. Violencia", "FK_Periodicidad":12, "FK_PubFechaAct":2701}
,{"Id":456, "Nombre":"Mujeres y Hombres en España. Poder", "FK_Periodicidad":12, "FK_PubFechaAct":11913}
,{"Id":457, "Nombre":"Mujeres y Hombres en España. Empleo del tiempo", "FK_Periodicidad":12, "FK_PubFechaAct":2712}
,{"Id":458, "Nombre":"Mujeres y Hombres en España. Salud", "FK_Periodicidad":12, "FK_PubFechaAct":2713}
,{"Id":459, "Nombre":"Estadística de Adquisiciones de Nacionalidad Española de Residentes", "FK_Periodicidad":12, "FK_PubFechaAct":11741}
,{"Id":460, "Nombre":"Contabilidad Nacional de España. Base 2010. Resultados detallados", "FK_Periodicidad":12, "FK_PubFechaAct":6799}
,{"Id":461, "Nombre":"Cuenta Satélite del Turismo de España", "FK_Periodicidad":12, "FK_PubFechaAct":10687}
,{"Id":462, "Nombre":"Encuesta de turismo de residentes anual", "FK_Periodicidad":12, "FK_PubFechaAct":12054}
,{"Id":468, "Nombre":"Nombres más frecuentes de los recién nacidos", "FK_Periodicidad":12, "FK_PubFechaAct":3239}
,{"Id":469, "Nombre":"Encuesta Coyuntural sobre Stocks y Existencias-Trimestral", "FK_Periodicidad":3, "FK_PubFechaAct":11562}
,{"Id":470, "Nombre":"Ponderaciones IPC", "FK_Periodicidad":12, "FK_PubFechaAct":11931}
,{"Id":471, "Nombre":"Movimientos turísticos en fronteras", "FK_Periodicidad":12, "FK_PubFechaAct":11979}
,{"Id":472, "Nombre":"Encuesta de Gasto Turístico", "FK_Periodicidad":12, "FK_PubFechaAct":11980}
,{"Id":479, "Nombre":"Estadística de Migraciones", "FK_Periodicidad":6, "FK_PubFechaAct":9551}
,{"Id":480, "Nombre":"Estadística sobre Transporte Ferroviario. Anuales", "FK_Periodicidad":12, "FK_PubFechaAct":11734}
,{"Id":481, "Nombre":"SID", "FK_Periodicidad":12, "FK_PubFechaAct":8226}
,{"Id":483, "Nombre":"Cifras de población", "FK_Periodicidad":12, "FK_PubFechaAct":3993}
,{"Id":484, "Nombre":"Cuentas medioambientales: Cuenta de gasto en protección medioambiental ", "FK_Periodicidad":12, "FK_PubFechaAct":11798}
,{"Id":485, "Nombre":"Cuentas medioambientales: Cuenta de flujos físicos de la energía", "FK_Periodicidad":12, "FK_PubFechaAct":11787}
,{"Id":486, "Nombre":"Indices de Precios de Consumo Armonizado. Medias anuales", "FK_Periodicidad":12, "FK_PubFechaAct":11934}
,{"Id":489, "Nombre":"Encuesta de Fecundidad", "FK_Periodicidad":12, "FK_PubFechaAct":6709}
,{"Id":490, "Nombre":"Cuentas medioambientales: bienes y servicios ambientales", "FK_Periodicidad":12, "FK_PubFechaAct":11796}
,{"Id":492, "Nombre":"Indicadores de la Agenda 2030 para el Desarrollo Sostenible (INE)", "FK_Periodicidad":12, "FK_PubFechaAct":12916}
,{"Id":493, "Nombre":"Contabilidad nacional anual de España: principales agregados", "FK_Periodicidad":12, "Url":"https://ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177057&idp=1254735576581", "FK_PubFechaAct":11724}
,{"Id":494, "Nombre":"Contabilidad nacional anual de España: agregados por rama de actividad", "FK_Periodicidad":12, "FK_PubFechaAct":12860}
,{"Id":496, "Nombre":"Contabilidad nacional anual de España: tablas de Origen y Destino", "FK_Periodicidad":12, "FK_PubFechaAct":11729}
,{"Id":497, "Nombre":"Contabilidad nacional anual de España: tablas Input-Output", "FK_Periodicidad":12, "FK_PubFechaAct":10602}
,{"Id":498, "Nombre":"ODS: Publicacion MNMT ", "FK_Periodicidad":12, "FK_PubFechaAct":6736}
,{"Id":506, "Nombre":"ODS: Publicación MAPA", "FK_Periodicidad":12, "FK_PubFechaAct":6763}
,{"Id":507, "Nombre":"Atlas de distribución de renta de los hogares", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177088&idp=1254735976608", "FK_PubFechaAct":11768}
,{"Id":508, "Nombre":"ODS: Publicacion MTFP", "FK_Periodicidad":12, "FK_PubFechaAct":6798}
,{"Id":510, "Nombre":"ODS: Banco de España", "FK_Periodicidad":12, "FK_PubFechaAct":6810}
,{"Id":511, "Nombre":"ODS: Publicación MSCB", "FK_Periodicidad":12, "FK_PubFechaAct":6818}
,{"Id":512, "Nombre":"Cuentas Medioambientales: Cuenta de los Residuos", "FK_Periodicidad":12, "FK_PubFechaAct":11785}
,{"Id":513, "Nombre":"ODS: Publicación MITECO", "FK_Periodicidad":12, "FK_PubFechaAct":6840}
,{"Id":514, "Nombre":"ODS: Publicación MINT", "FK_Periodicidad":12, "FK_PubFechaAct":6841}
,{"Id":515, "Nombre":"(68008) Anuario Estadístico del Ministerio del Interior", "FK_Periodicidad":12, "FK_PubFechaAct":6842}
,{"Id":516, "Nombre":"(70048) Estadística de Accidentes de Tráfico con Víctimas", "FK_Periodicidad":12, "FK_PubFechaAct":6843}
,{"Id":517, "Nombre":"(68025) Estadística del Sistema de Seguimiento Integral en los casos de Violencia de Género (Sistema VdG o VIOGÉN)", "FK_Periodicidad":12, "FK_PubFechaAct":6844}
,{"Id":518, "Nombre":"(68020) Estadística General de la Población Reclusa. Periodicidad Mensual", "FK_Periodicidad":12, "FK_PubFechaAct":6845}
,{"Id":519, "Nombre":"(31127) Cuentas de las Administraciones Públicas", "FK_Periodicidad":12, "FK_PubFechaAct":6846}
,{"Id":520, "Nombre":"(31125) Estadística de Liquidación de los Presupuestos del Estado y de sus Organismos Públicos, Empresas y Fundaciones", "FK_Periodicidad":12, "FK_PubFechaAct":6847}
,{"Id":521, "Nombre":"(65007) Macroencuesta de Violencia contra la Mujer", "FK_Periodicidad":12, "FK_PubFechaAct":6848}
,{"Id":522, "Nombre":"(68001) Estadística de Seguridad: Actuaciones Policiales", "FK_Periodicidad":12, "FK_PubFechaAct":6876}
,{"Id":523, "Nombre":"(23033) Estadística de Diversidad de Especies Silvestres", "FK_Periodicidad":12, "FK_PubFechaAct":6878}
,{"Id":524, "Nombre":"(01142) Estadísticas de Capturas y Desembarcos de Pesca Marítima", "FK_Periodicidad":12, "FK_PubFechaAct":7994}
,{"Id":525, "Nombre":"(01049) Red Contable Agraria Nacional (RECAN)", "FK_Periodicidad":12, "FK_PubFechaAct":7995}
,{"Id":526, "Nombre":"(04001) Inventario Forestal Nacional", "FK_Periodicidad":12, "FK_PubFechaAct":7996}
,{"Id":527, "Nombre":"(23030) Estadística sobre Gestión Forestal Sostenible", "FK_Periodicidad":12, "FK_PubFechaAct":7997}
,{"Id":528, "Nombre":"(32063) Estadística de los Declarantes del IRPF", "FK_Periodicidad":12, "FK_PubFechaAct":7998}
,{"Id":529, "Nombre":"(32068) Estadística del Rendimiento de Actividades Económicas", "FK_Periodicidad":12, "FK_PubFechaAct":7999}
,{"Id":530, "Nombre":"(41001) Estadística de Enseñanzas no Universitarias (Centros, Matrícula, Graduados y Personal)", "FK_Periodicidad":12, "FK_PubFechaAct":8005}
,{"Id":531, "Nombre":"(42184) Programa de Evaluación Internacional de Competencias de Adultos (PIAAC Programme for the International Assessment of Adult Competences de la OCDE)", "FK_Periodicidad":107, "FK_PubFechaAct":8006}
,{"Id":532, "Nombre":"(41022) Estadística sobre la Sociedad de la Información y la Comunicación en los Centros Educativos no Universitarios", "FK_Periodicidad":12, "FK_PubFechaAct":8007}
,{"Id":533, "Nombre":"(37142) Balanza de Pagos y Posición de Inversión Internacional", "FK_Periodicidad":12, "FK_PubFechaAct":8008}
,{"Id":534, "Nombre":"(37145) Encuesta de Competencias Financieras (ECF)", "FK_Periodicidad":12, "FK_PubFechaAct":8009}
,{"Id":535, "Nombre":"ODS - Cuentas Medioambientales: Cuenta de Emisiones a la Atmósfera (30084)", "FK_Periodicidad":12, "FK_PubFechaAct":8010}
,{"Id":536, "Nombre":"(85004) Estadística de Ayuda Oficial al Desarrollo (AOD) de España", "FK_Periodicidad":12, "FK_PubFechaAct":8023}
,{"Id":538, "Nombre":"(01165) Estadística de la Producción Ecológica", "FK_Periodicidad":12, "FK_PubFechaAct":8034}
,{"Id":539, "Nombre":"Cubo Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":9387}
,{"Id":542, "Nombre":"Experimental: movilidad COVID19", "FK_Periodicidad":30, "FK_PubFechaAct":9374}
,{"Id":543, "Nombre":"Publicación para operaciones no pertenecientes al PEN. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":8126}
,{"Id":544, "Nombre":"Estimación del número de defunciones semanales", "FK_Periodicidad":7, "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177074&idp=1254735573002", "FK_PubFechaAct":11574}
,{"Id":545, "Nombre":"Encuesta cuatrienal de Estructura Salarial", "FK_Periodicidad":105, "FK_PubFechaAct":None}
,{"Id":547, "Nombre":"ODS: Publicación MTMA", "FK_Periodicidad":12, "FK_PubFechaAct":8152}
,{"Id":548, "Nombre":"Experimental: Índice Diario de Comercio al por Menor", "FK_Periodicidad":30, "FK_PubFechaAct":11858}
,{"Id":551, "Nombre":"(21021) Seguimiento del Estado de las Aguas Superficiales", "FK_Periodicidad":12, "FK_PubFechaAct":8234}
,{"Id":552, "Nombre":"Estadística de Discapacidad y Mercado Laboral: Vida Laboral", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177069&idp=1254735976621", "FK_PubFechaAct":11753}
,{"Id":553, "Nombre":"(23042) Inventario de Emisiones Contaminantes a la Atmósfera", "FK_Periodicidad":12, "FK_PubFechaAct":8237}
,{"Id":554, "Nombre":"(23031) Espacios Naturales o de Interés. Anual.", "FK_Periodicidad":12, "FK_PubFechaAct":8239}
,{"Id":555, "Nombre":"Tabla de Pensiones", "FK_Periodicidad":12, "FK_PubFechaAct":10222}
,{"Id":556, "Nombre":"Experimental: Viviendas turísticas en España", "FK_Periodicidad":1, "FK_PubFechaAct":12390}
,{"Id":557, "Nombre":"(79001) Barómetros de Opinión", "FK_Periodicidad":12, "FK_PubFechaAct":8270}
,{"Id":558, "Nombre":"Experimental: Distribución del gasto en destino realizado por los visitantes extranjeros en sus visitas a España", "FK_Periodicidad":12, "FK_PubFechaAct":12006}
,{"Id":559, "Nombre":"Experimental: Distribución del gasto en destino realizado por los visitantes extranjeros en sus visitas a España", "FK_Periodicidad":3, "FK_PubFechaAct":12856}
,{"Id":560, "Nombre":"(54063) Estadística de Enfermedades de Declaración Obligatoria", "FK_Periodicidad":12, "FK_PubFechaAct":8585}
,{"Id":561, "Nombre":"ODS: Publicación MCUD", "FK_Periodicidad":12, "FK_PubFechaAct":8619}
,{"Id":562, "Nombre":"Estimación Mensual de Nacimientos", "FK_Periodicidad":1, "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177079&idp=1254735573002", "FK_PubFechaAct":11575}
,{"Id":563, "Nombre":"Experimental: Coyuntura demográfica de empresas", "FK_Periodicidad":3, "FK_PubFechaAct":10033}
,{"Id":564, "Nombre":"(32078) Clasificación Funcional del Gasto de las Administraciones Públicas (COFOG)", "FK_Periodicidad":12, "FK_PubFechaAct":8670}
,{"Id":565, "Nombre":"Clasificación Funcional del Gasto de las Administraciones Públicas (COFOG)", "FK_Periodicidad":12, "FK_PubFechaAct":8669}
,{"Id":566, "Nombre":"Publicación trimestral para operaciones no pertenecientes al PEN", "FK_Periodicidad":3, "FK_PubFechaAct":8679}
,{"Id":568, "Nombre":"Publicación de Explotación de las Variables Educativas en la Encuesta de Población Activa: Nivel de Formación y Formación Permanente", "FK_Periodicidad":12, "FK_PubFechaAct":8713}
,{"Id":570, "Nombre":"GruposPeriodo - Estadística del padron continuo", "FK_Periodicidad":12, "FK_PubFechaAct":9950}
,{"Id":571, "Nombre":"Experimental: Ocupación en alojamientos turísticos. Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":12859}
,{"Id":572, "Nombre":"Experimental: Ocupación en alojamientos turísticos. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":12786}
,{"Id":574, "Nombre":"ODS- Deuda Pública según el Protocolo de Déficit Excesivo (ANUAL)", "FK_Periodicidad":12, "FK_PubFechaAct":8795}
,{"Id":575, "Nombre":"(32075) Operaciones No Financieras del Sector Administraciones Públicas y sus Subsectores", "FK_Periodicidad":12, "FK_PubFechaAct":8820}
,{"Id":576, "Nombre":"Encuesta de Ocupación Hotelera. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":8854}
,{"Id":577, "Nombre":"Encuesta de ocupación en alojamientos turísticos extrahoteleros. Anual", "FK_Periodicidad":12, "FK_PubFechaAct":9413}
,{"Id":578, "Nombre":"GruposPeriodo - Contabilidad nacional anual de España: agregados por rama de actividad", "FK_Periodicidad":12, "FK_PubFechaAct":10177}
,{"Id":579, "Nombre":"(68052) Estadística sobre la Trata y la Explotación de Seres Humanos", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":580, "Nombre":"Índice de Precios de Vivienda en Alquiler", "FK_Periodicidad":12, "Url":"https://www.ine.es/experimental/ipva/experimental_precios_vivienda_alquiler.htm", "FK_PubFechaAct":12025}
,{"Id":581, "Nombre":"Experimental: Indicador Multidimensional de Calidad de Vida", "FK_Periodicidad":12, "FK_PubFechaAct":12875}
,{"Id":582, "Nombre":"Grupos periodo -  Explotación Estadística del Directorio Central de Empresas", "FK_Periodicidad":12, "FK_PubFechaAct":12888}
,{"Id":583, "Nombre":"Publicación para operaciones no pertenecientes al PEN. Quinquenal", "FK_Periodicidad":108, "FK_PubFechaAct":9284}
,{"Id":584, "Nombre":"CALENDARIO", "FK_Periodicidad":100, "FK_PubFechaAct":12906}
,{"Id":585, "Nombre":"Publicación para operaciones no pertenecientes al PEN. Cuatrienal Base 2003", "FK_Periodicidad":111, "FK_PubFechaAct":9288}
,{"Id":586, "Nombre":"Publicación para operaciones no pertenecientes al PEN. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":9289}
,{"Id":587, "Nombre":"(23031) Espacios Naturales o de Interés. Trienal.", "FK_Periodicidad":112, "FK_PubFechaAct":9290}
,{"Id":588, "Nombre":"(41022) Estadística sobre la Sociedad de la Información y la Comunicación en los Centros Educativos no Universitarios. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":9300}
,{"Id":589, "Nombre":"(65007) Macroencuesta de Violencia contra la Mujer. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":9301}
,{"Id":590, "Nombre":"Encuesta Nacional de Salud. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":10835}
,{"Id":591, "Nombre":"Encuesta sobre la participación de la población adulta en las actividades de aprendizaje. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":11822}
,{"Id":592, "Nombre":"(23031) Espacios Naturales o de Interés. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":9304}
,{"Id":593, "Nombre":"(23033) Estadística de Diversidad de Especies Silvestres. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":9305}
,{"Id":594, "Nombre":"(41022) Estadística sobre la Sociedad de la Información y la Comunicación en los Centros Educativos no Universitarios. Bienal impar", "FK_Periodicidad":13, "FK_PubFechaAct":9310}
,{"Id":595, "Nombre":"Medición del turismo receptor a partir de la posición de los teléfonos móviles", "FK_Periodicidad":1, "FK_PubFechaAct":12899}
,{"Id":596, "Nombre":"Medición del turismo emisor a partir de la posición de los teléfonos móviles", "FK_Periodicidad":1, "FK_PubFechaAct":12900}
,{"Id":597, "Nombre":"Medición del turismo interno interprovincial a partir de la posición de los teléfonos móviles", "FK_Periodicidad":1, "FK_PubFechaAct":12901}
,{"Id":598, "Nombre":"(50052) Cuenta Satélite de Cultura", "FK_Periodicidad":12, "FK_PubFechaAct":9384}
,{"Id":599, "Nombre":"(50057) Explotación de la Encuesta de Población Activa en el Ámbito Cultural, en lugar de la Cuenta Satélite", "FK_Periodicidad":12, "FK_PubFechaAct":9389}
,{"Id":602, "Nombre":"(80024) Registro Central de Personal. Boletín Estadístico del Personal al Servicio de las Administraciones Públicas", "FK_Periodicidad":12, "FK_PubFechaAct":9473}
,{"Id":603, "Nombre":"(32077) Impuestos y Cotizaciones Sociales", "FK_Periodicidad":12, "FK_PubFechaAct":9474}
,{"Id":604, "Nombre":"Cuentas Trimestrales no Financieras de los Sectores Institucionales (solo para ODS)", "FK_Periodicidad":12, "FK_PubFechaAct":9494}
,{"Id":605, "Nombre":"Contabilidad Nacional Trimestral (solo para ODS)", "FK_Periodicidad":12, "FK_PubFechaAct":9495}
,{"Id":607, "Nombre":"(01160) Encuesta de Comercialización de Productos Fitosanitarios", "FK_Periodicidad":12, "FK_PubFechaAct":9573}
,{"Id":608, "Nombre":"Encuesta de características esenciales de la población y viviendas (ECEPOV)", "FK_Periodicidad":12, "FK_PubFechaAct":9943}
,{"Id":609, "Nombre":"(43041) Actividad del Consejo Superior de Investigaciones Científicas (MCIN)", "FK_Periodicidad":12, "FK_PubFechaAct":9587}
,{"Id":610, "Nombre":"Estadística Continua de Población", "FK_Periodicidad":3, "FK_PubFechaAct":12898}
,{"Id":612, "Nombre":"Distribución del gasto realizado por los residentes en sus visitas al Extranjero según país de destino", "FK_Periodicidad":12, "FK_PubFechaAct":12016}
,{"Id":613, "Nombre":"Distribución del gasto realizado por los residentes en sus visitas al Extranjero según país de destino", "FK_Periodicidad":1, "FK_PubFechaAct":12855}
,{"Id":616, "Nombre":"Indicadores de Confianza Empresarial. Módulo de Opinión sobre la Energía", "FK_Periodicidad":3, "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736163552&menu=resultados&idp=1254735576550#!tabs-1254736195794", "FK_PubFechaAct":10042}
,{"Id":617, "Nombre":"Encuesta de Población Activa. Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":10063}
,{"Id":619, "Nombre":"(01048) Salarios e Índices Agrarios Medios Nacionales Mensuales y Anuales", "FK_Periodicidad":12, "FK_PubFechaAct":10150}
,{"Id":620, "Nombre":"(01053) Cuentas Económicas de la Agricultura", "FK_Periodicidad":12, "FK_PubFechaAct":10151}
,{"Id":622, "Nombre":"Estadística de Migraciones y Cambios de Residencia", "FK_Periodicidad":12, "FK_PubFechaAct":12853}
,{"Id":626, "Nombre":"Índice de Producción del Sector Servicios", "FK_Periodicidad":1, "Url":"https://ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177099&idp=1254735576778", "FK_PubFechaAct":11552}
,{"Id":627, "Nombre":"Índice de Producción del Sector Servicios. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":12000}
,{"Id":629, "Nombre":"Comercio Internacional de Servicios por Modos de Suministro (MoS)", "FK_Periodicidad":12, "FK_PubFechaAct":11993}
,{"Id":630, "Nombre":"Comercio Internacional de Servicios por Características de las Empresas (STEC)", "FK_Periodicidad":12, "FK_PubFechaAct":10685}
,{"Id":631, "Nombre":"Grupos periodo -  ECM", "FK_Periodicidad":12, "FK_PubFechaAct":12905}
,{"Id":632, "Nombre":"Estimación del número de defunciones mensuales", "FK_Periodicidad":1, "FK_PubFechaAct":11930}
,{"Id":633, "Nombre":"Censo de población. Al detalle", "T3_Periodicidad":"Al Detalle", "FK_PubFechaAct":282}
,{"Id":634, "Nombre":"Grupos periodo -  Censo anual", "FK_Periodicidad":12, "FK_PubFechaAct":12012}
,{"Id":635, "Nombre":"Grupos periodo. Modulo de viajeros", "FK_Periodicidad":12, "FK_PubFechaAct":12053}
,{"Id":636, "Nombre":"Panel de Indicadores Ambientales", "FK_Periodicidad":12, "Url":"https://ine.es/infografias/medioambiente/panel_ind_medioambiente.htm", "FK_PubFechaAct":12879}
,{"Id":637, "Nombre":"Índice de Precios del Sector Servicios. Ponderaciones", "FK_Periodicidad":12, "FK_PubFechaAct":11999}
,{"Id":638, "Nombre":"Grpos Periodo. MNP", "FK_Periodicidad":12, "FK_PubFechaAct":12911}
,{"Id":640, "Nombre":"Encuesta de Turismo de Residentes. HVD. Periodicidad Trienal", "FK_Periodicidad":106, "FK_PubFechaAct":11945}
,{"Id":641, "Nombre":"Publicación para operaciones no pertenecientes al PEN. Bienal", "FK_Periodicidad":14, "FK_PubFechaAct":10891}
,{"Id":643, "Nombre":"Censo anual de poblacion.Indicadores HVD", "FK_Periodicidad":12, "FK_PubFechaAct":11915}
,{"Id":644, "Nombre":"Encuesta de Salud de España", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736177114&idp=1254735573175", "FK_PubFechaAct":11800}
,{"Id":645, "Nombre":"Tabla Origen-Destino de la economía digital", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":646, "Nombre":"Cuenta satélite de la economía social", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":647, "Nombre":"Estadística estructural de empresas: Sector Construcción", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":648, "Nombre":"Estadística sobre Cadenas de Valor Globales", "FK_Periodicidad":12, "FK_PubFechaAct":11820}
,{"Id":649, "Nombre":"Cuentas Trimestrales de Emisiones a la Atmósfera", "FK_Periodicidad":3, "FK_PubFechaAct":12887}
,{"Id":650, "Nombre":"Encuesta de Turismo de Residentes. HVD. Periodicidad Anual", "FK_Periodicidad":12, "FK_PubFechaAct":12920}
,{"Id":651, "Nombre":"Censos Anuales de Población. Migración, educación y relación con la actividad.", "FK_Periodicidad":12, "FK_PubFechaAct":12862}
,{"Id":652, "Nombre":"Censos Anuales de Población. Ocupación y actividad.", "FK_Periodicidad":12, "FK_PubFechaAct":12889}
,{"Id":653, "Nombre":"Censos Anuales de Población. Años de llegada y residencia anterior.", "FK_Periodicidad":12, "FK_PubFechaAct":12861}
,{"Id":654, "Nombre":"Índice de Referencia de Arrendamientos de Vivienda", "FK_Periodicidad":1, "FK_PubFechaAct":11912}
,{"Id":655, "Nombre":"Encuesta sobre la Estructura de las Explotaciones Agrícolas: Módulos", "FK_Periodicidad":12, "FK_PubFechaAct":11985}
,{"Id":656, "Nombre":"Encuesta de Ocupación en Alojamientos Turísticos. HVD", "FK_Periodicidad":12, "FK_PubFechaAct":None}
,{"Id":657, "Nombre":"Experimental: Panel de indicadores TiVA", "FK_Periodicidad":12, "FK_PubFechaAct":12772}
,{"Id":658, "Nombre":"Censo anual de poblacion. ODS", "FK_Periodicidad":12, "FK_PubFechaAct":12022}
,{"Id":660, "Nombre":"Estadística sobre Relación con la Actividad a partir de Datos Administrativos.Mensual", "FK_Periodicidad":1, "FK_PubFechaAct":None}
,{"Id":661, "Nombre":"Estadística sobre Relación con la Actividad a partir de Datos Administrativos.Semanal", "FK_Periodicidad":7, "FK_PubFechaAct":None}
,{"Id":662, "Nombre":"Experimental: Visualizador de multilocalización empresarial (VIME)", "FK_Periodicidad":12, "Url":"https://www.ine.es/experimental/VIME/experimental_visualizador_empresarial.htm", "FK_PubFechaAct":12069}
,{"Id":663, "Nombre":"Cuentas Medioambientales: Cuenta de Subvenciones Medioambientales y Otras Transferencias Similares", "FK_Periodicidad":12, "Url":"https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177118&idp=1254735976603", "FK_PubFechaAct":12878}
,{"Id":664, "Nombre":"Índice de Producción de la Construcción", "FK_Periodicidad":1, "FK_PubFechaAct":None}
,{"Id":665, "Nombre":"Índice de producción de la construcción", "FK_Periodicidad":1, "FK_PubFechaAct":None}
,{"Id":666, "Nombre":"Encuesta sobre centros de atención a personas sin hogar. Anual sin determinar", "FK_Periodicidad":107, "FK_PubFechaAct":12857}
,{"Id":667, "Nombre":"Censo anual de población. Estado civil", "FK_Periodicidad":12, "FK_PubFechaAct":12890}
,{"Id":668, "Nombre":"Estadística sobre Cadenas de Valor Globales", "FK_Periodicidad":106, "FK_PubFechaAct":12876}
,{"Id":669, "Nombre":"(20061)  Encuesta Permanente de Transporte de Mercancías por Carretera", "FK_Periodicidad":12, "FK_PubFechaAct":12880}
]

Un = [{"Id":3, "Nombre":"Personas", "Codigo":None, "Abrev":None}
,
{"Id":7, "Nombre":"Euros", "Codigo":None, "Abrev":"€"}
,
{"Id":9, "Nombre":"Pares", "Codigo":None, "Abrev":"Pares"}
,
{"Id":10, "Nombre":"Minutos", "Codigo":None, "Abrev":None}
,
{"Id":11, "Nombre":"Horas", "Codigo":None, "Abrev":"Horas"}
,
{"Id":12, "Nombre":"Días", "Codigo":None, "Abrev":None}
,
{"Id":33, "Nombre":"Metros cuadrados", "Codigo":None, "Abrev":"m2"}
,
{"Id":34, "Nombre":"Kilómetros cuadrados", "Codigo":None, "Abrev":"Km2"}
,
{"Id":37, "Nombre":"Hectáreas", "Codigo":None, "Abrev":None}
,
{"Id":42, "Nombre":"Toneladas", "Codigo":None, "Abrev":"t."}
,
{"Id":45, "Nombre":"Litros", "Codigo":None, "Abrev":"Litros"}
,
{"Id":48, "Nombre":"Horas/trabajador(mes)", "Codigo":None, "Abrev":None}
,
{"Id":50, "Nombre":"Tanto por cien", "Codigo":None, "Abrev":"Tanto por cien"}
,
{"Id":51, "Nombre":"Tanto por mil", "Codigo":None, "Abrev":"%1000"}
,
{"Id":93, "Nombre":"Miles de euros", "Codigo":None, "Abrev":"Miles de euros"}
,
{"Id":97, "Nombre":"Empresas", "Codigo":None, "Abrev":None}
,
{"Id":101, "Nombre":"Porcentaje", "Codigo":None, "Abrev":"%"}
,
{"Id":108, "Nombre":"Años", "Codigo":None, "Abrev":None}
,
{"Id":110, "Nombre":"Hijos por mujer", "Codigo":None, "Abrev":None}
,
{"Id":113, "Nombre":"Nacimientos por 1.000 mujeres", "Codigo":None, "Abrev":None}
,
{"Id":114, "Nombre":"Matrimonios por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":115, "Nombre":"Nacimientos menos defunciones (por mil habitantes)", "Codigo":None, "Abrev":None}
,
{"Id":116, "Nombre":"Defunciones por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":117, "Nombre":"Defunciones de menores de 1 año por 1.000 nacidos", "Codigo":None, "Abrev":None}
,
{"Id":118, "Nombre":"Defunciones durante las 24 primeras horas de vida", "Codigo":None, "Abrev":None}
,
{"Id":120, "Nombre":"Nacimientos", "Codigo":None, "Abrev":None}
,
{"Id":121, "Nombre":"Matrimonios", "Codigo":None, "Abrev":None}
,
{"Id":122, "Nombre":"Defunciones", "Codigo":None, "Abrev":None}
,
{"Id":123, "Nombre":"Número", "Codigo":None, "Abrev":None}
,
{"Id":124, "Nombre":"Gasto total: miles de euros. Gastos medios: euros ", "Codigo":None, "Abrev":"Gasto total: miles de euros. Gastos medios: euros "}
,
{"Id":125, "Nombre":"Gasto total: miles de euros. Valor unitario: euros/unidad", "Codigo":None, "Abrev":"Gasto total: miles de euros. Valor unitario: euros/unidad"}
,
{"Id":128, "Nombre":"Locales", "Codigo":None, "Abrev":None}
,
{"Id":129, "Nombre":"Cantidad total: miles de unidades. Cantidad media: unidades", "Codigo":None, "Abrev":"Cantidad total: miles de unidades. Cantidad media: unidades"}
,
{"Id":131, "Nombre":"Personas y porcentajes", "Codigo":None, "Abrev":"Personas y %"}
,
{"Id":133, "Nombre":"Índice", "Codigo":None, "Abrev":None}
,
{"Id":134, "Nombre":"Municipios", "Codigo":None, "Abrev":"Municipios"}
,
{"Id":135, "Nombre":"Tasas", "Codigo":None, "Abrev":None}
,
{"Id":142, "Nombre":"Personas que se casan por primera vez por cada mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":155, "Nombre":"Movimientos migratorios", "Codigo":None, "Abrev":None}
,
{"Id":156, "Nombre":"Mil kWh", "Codigo":None, "Abrev":"1.000 kWh"}
,
{"Id":157, "Nombre":"Kilogramo de sustancia activa", "Codigo":None, "Abrev":"kg. act. sub"}
,
{"Id":158, "Nombre":"Mil metros cúbicos", "Codigo":None, "Abrev":"mil m3"}
,
{"Id":159, "Nombre":"---", "Codigo":None, "Abrev":"---"}
,
{"Id":160, "Nombre":"Tonelada de nitrogeno", "Codigo":None, "Abrev":"t. N"}
,
{"Id":161, "Nombre":"Unidades", "Codigo":None, "Abrev":"Unidades"}
,
{"Id":162, "Nombre":"Tonelada de trióxido  de dialuminio (alúmina)", "Codigo":None, "Abrev":"t. Al2O3"}
,
{"Id":163, "Nombre":"Tonelada de materia seca al 90%", "Codigo":None, "Abrev":"t. 90% s.d.t."}
,
{"Id":166, "Nombre":"Tonelada de pirosulfito de sodio", "Codigo":None, "Abrev":"t. Na2S2O5"}
,
{"Id":167, "Nombre":"Kilogramo", "Codigo":None, "Abrev":"kg"}
,
{"Id":169, "Nombre":"Hectolitro de alcohol puro 100%", "Codigo":None, "Abrev":"hl. alc. 100%"}
,
{"Id":170, "Nombre":"Mil metros", "Codigo":None, "Abrev":"mil metros"}
,
{"Id":171, "Nombre":"Tonelada de óxido de potasio", "Codigo":None, "Abrev":"t. K2O"}
,
{"Id":173, "Nombre":"Kilogramo de dióxido de titanio", "Codigo":None, "Abrev":"kg. TiO2"}
,
{"Id":174, "Nombre":"Tonelada de dióxido de azufre", "Codigo":None, "Abrev":"t. SO2"}
,
{"Id":176, "Nombre":"Mil litros", "Codigo":None, "Abrev":"mil litros"}
,
{"Id":177, "Nombre":"Hectolitro", "Codigo":None, "Abrev":"hectolitro"}
,
{"Id":178, "Nombre":"Terajulios", "Codigo":None, "Abrev":"terajulios"}
,
{"Id":180, "Nombre":"Tonelada de cloruro de hidrógeno", "Codigo":None, "Abrev":"t. HCl"}
,
{"Id":181, "Nombre":"Tonelada de peróxido de hidrógeno", "Codigo":None, "Abrev":"t. H2O2"}
,
{"Id":182, "Nombre":"Arqueo bruto compensado", "Codigo":None, "Abrev":"CGT"}
,
{"Id":183, "Nombre":"Tonelada de dióxido de silicio", "Codigo":None, "Abrev":"t. SiO2"}
,
{"Id":184, "Nombre":"Tonelada de anhídrido fosfórico", "Codigo":None, "Abrev":"t. P2O5"}
,
{"Id":185, "Nombre":"Gramo", "Codigo":None, "Abrev":"gramo"}
,
{"Id":186, "Nombre":"Mil pares", "Codigo":None, "Abrev":"mil pares"}
,
{"Id":187, "Nombre":"Mil metros cuadrados", "Codigo":None, "Abrev":"mil m2"}
,
{"Id":188, "Nombre":"........", "Codigo":None, "Abrev":"........"}
,
{"Id":189, "Nombre":"Mil unidades", "Codigo":None, "Abrev":"mil unidades"}
,
{"Id":190, "Nombre":"Tonelada de cloro", "Codigo":None, "Abrev":"t. Cl"}
,
{"Id":191, "Nombre":"Tonelada de hidróxido de sodio (sosa cáustica)", "Codigo":None, "Abrev":"t. NaOH"}
,
{"Id":192, "Nombre":"Kilovatios", "Codigo":None, "Abrev":"Kw"}
,
{"Id":193, "Nombre":"Tonelada de trióxido de diboro", "Codigo":None, "Abrev":"t. B2O3"}
,
{"Id":196, "Nombre":"Tonelada de fluor", "Codigo":None, "Abrev":"t. F"}
,
{"Id":197, "Nombre":"Número de celdas", "Codigo":None, "Abrev":"Nº celdas"}
,
{"Id":199, "Nombre":"Metros cúbicos", "Codigo":None, "Abrev":"m3"}
,
{"Id":200, "Nombre":"Tonelada de hidróxido de potasio (potasa cáustica)", "Codigo":None, "Abrev":"t. KOH"}
,
{"Id":201, "Nombre":"Tonelada de floruro de hidrógeno", "Codigo":None, "Abrev":"t. HF"}
,
{"Id":202, "Nombre":"Metro", "Codigo":None, "Abrev":"m."}
,
{"Id":203, "Nombre":"Kilogramo de nitrógeno", "Codigo":None, "Abrev":"kg. N"}
,
{"Id":204, "Nombre":"Kilogramo de carbonato de sodio", "Codigo":None, "Abrev":"kg. Na2CO3"}
,
{"Id":207, "Nombre":"Puestos de trabajo", "Codigo":None, "Abrev":None}
,
{"Id":213, "Nombre":"Viajeros", "Codigo":None, "Abrev":None}
,
{"Id":214, "Nombre":"Vivienda", "Codigo":None, "Abrev":None}
,
{"Id":219, "Nombre":"Tipo marginal", "Codigo":None, "Abrev":"Tipo marginal"}
,
{"Id":220, "Nombre":"Media", "Codigo":None, "Abrev":"Media"}
,
{"Id":221, "Nombre":"Base dic85 = 100", "Codigo":None, "Abrev":"Base dic85 = 100"}
,
{"Id":222, "Nombre":"USD/EUR", "Codigo":None, "Abrev":"USD/EUR"}
,
{"Id":229, "Nombre":"Horas/trabajador (semana)", "Codigo":None, "Abrev":None}
,
{"Id":231, "Nombre":"Porcentaje de personas", "Codigo":None, "Abrev":None}
,
{"Id":232, "Nombre":"Porcentaje de hogares", "Codigo":None, "Abrev":"% hogares"}
,
{"Id":234, "Nombre":"Matrimonios por persona", "Codigo":None, "Abrev":None}
,
{"Id":235, "Nombre":"Tanto por mil de casados", "Codigo":None, "Abrev":None}
,
{"Id":236, "Nombre":"Tanto por mil de matrimonios", "Codigo":None, "Abrev":None}
,
{"Id":237, "Nombre":"Tanto por mil de personas", "Codigo":None, "Abrev":None}
,
{"Id":239, "Nombre":"Vacante", "Codigo":None, "Abrev":None}
,
{"Id":240, "Nombre":"Porcentaje de centros", "Codigo":None, "Abrev":"Porcentaje de centros"}
,
{"Id":242, "Nombre":"Pernoctaciones", "Codigo":None, "Abrev":"Pernoctaciones"}
,
{"Id":243, "Nombre":"Apartamentos", "Codigo":None, "Abrev":None}
,
{"Id":244, "Nombre":"Establecimientos", "Codigo":None, "Abrev":None}
,
{"Id":245, "Nombre":"Plazas", "Codigo":None, "Abrev":None}
,
{"Id":246, "Nombre":"Parcelas", "Codigo":None, "Abrev":"Parcelas"}
,
{"Id":249, "Nombre":"Emigraciones por habitante", "Codigo":None, "Abrev":None}
,
{"Id":251, "Nombre":"Migraciones por habitante", "Codigo":None, "Abrev":None}
,
{"Id":252, "Nombre":"Finca", "Codigo":None, "Abrev":None}
,
{"Id":254, "Nombre":"Tanto por uno", "Codigo":None, "Abrev":None}
,
{"Id":255, "Nombre":"Porcentaje de fallecidos", "Codigo":None, "Abrev":"%"}
,
{"Id":256, "Nombre":"Viajes", "Codigo":None, "Abrev":None}
,
{"Id":257, "Nombre":"Indicadores", "Codigo":None, "Abrev":"Indicadores"}
,
{"Id":260, "Nombre":"Euros", "Codigo":None, "Abrev":None}
,
{"Id":261, "Nombre":"Euros", "Codigo":None, "Abrev":"Euros"}
,
{"Id":262, "Nombre":"Gold fine troy ounces", "Codigo":None, "Abrev":None}
,
{"Id":263, "Nombre":"Excursiones", "Codigo":None, "Abrev":None}
,
{"Id":264, "Nombre":"Habitaciones", "Codigo":None, "Abrev":None}
,
{"Id":273, "Nombre":"Nacidos por mil defunciones", "Codigo":None, "Abrev":None}
,
{"Id":274, "Nombre":"Crecimiento por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":275, "Nombre":"Emigraciones por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":276, "Nombre":"Inmigraciones por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":277, "Nombre":"Migraciones por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":278, "Nombre":"Primeros Matrimonios por habitante", "Codigo":None, "Abrev":None}
,
{"Id":279, "Nombre":"Primeros Matrimonios por hombre", "Codigo":None, "Abrev":None}
,
{"Id":280, "Nombre":"Primeros Matrimonios por mujer", "Codigo":None, "Abrev":None}
,
{"Id":281, "Nombre":"Matrimonios por habitante", "Codigo":None, "Abrev":None}
,
{"Id":282, "Nombre":"Matrimonios por hombre", "Codigo":None, "Abrev":None}
,
{"Id":283, "Nombre":"Matrimonios por mujer", "Codigo":None, "Abrev":None}
,
{"Id":284, "Nombre":"Contrayentes por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":285, "Nombre":"Defunciones por mil nacidos", "Codigo":None, "Abrev":None}
,
{"Id":286, "Nombre":"Defunciones por mil nacidos vivos", "Codigo":None, "Abrev":None}
,
{"Id":287, "Nombre":"Nacidos por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":288, "Nombre":"Hipotecas", "Codigo":None, "Abrev":None}
,
{"Id":289, "Nombre":"Ácido sulfúrico", "Codigo":None, "Abrev":"t. H2SO4"}
,
{"Id":290, "Nombre":"Etapas", "Codigo":None, "Abrev":None}
,
{"Id":291, "Nombre":"Viajes por cada mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":293, "Nombre":"Mujeres por cada 100 hombres", "Codigo":None, "Abrev":None}
,
{"Id":294, "Nombre":"Tanto por 100.000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":295, "Nombre":"Excursiones por cada mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":296, "Nombre":"Libros", "Codigo":None, "Abrev":None}
,
{"Id":297, "Nombre":"Bibliotecas", "Codigo":None, "Abrev":None}
,
{"Id":298, "Nombre":"Visitas", "Codigo":None, "Abrev":None}
,
{"Id":299, "Nombre":"Turistas", "Codigo":None, "Abrev":None}
,
{"Id":300, "Nombre":"Asunto", "Codigo":None, "Abrev":None}
,
{"Id":301, "Nombre":"Sentencias", "Codigo":None, "Abrev":None}
,
{"Id":302, "Nombre":"Partos", "Codigo":None, "Abrev":None}
,
{"Id":303, "Nombre":"Nulidades", "Codigo":None, "Abrev":None}
,
{"Id":304, "Nombre":"Separaciones", "Codigo":None, "Abrev":None}
,
{"Id":305, "Nombre":"Divorcios", "Codigo":None, "Abrev":None}
,
{"Id":306, "Nombre":"Disoluciones matrimoniales", "Codigo":None, "Abrev":None}
,
{"Id":307, "Nombre":"Número de asuntos", "Codigo":None, "Abrev":"Nº asuntos"}
,
{"Id":308, "Nombre":"UTI", "Codigo":None, "Abrev":"UTI"}
,
{"Id":309, "Nombre":"UTI en TEU", "Codigo":None, "Abrev":"UTI en TEU"}
,
{"Id":310, "Nombre":"Trenes-Km", "Codigo":None, "Abrev":None}
,
{"Id":311, "Nombre":"Accidentes", "Codigo":None, "Abrev":None}
,
{"Id":312, "Nombre":"Toneladas-Km (1000)", "Codigo":None, "Abrev":"Toneladas-Km (1000)"}
,
{"Id":313, "Nombre":"Viajeros-Km (1000)", "Codigo":None, "Abrev":None}
,
{"Id":315, "Nombre":"Divorcios por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":316, "Nombre":"Divorciados por mil habitantes", "Codigo":None, "Abrev":None}
,
{"Id":317, "Nombre":"Divorcios por habitante", "Codigo":None, "Abrev":None}
,
{"Id":318, "Nombre":"Divorcios por hombre", "Codigo":None, "Abrev":None}
,
{"Id":319, "Nombre":"Divorcios por mujer", "Codigo":None, "Abrev":None}
,
{"Id":320, "Nombre":"Porcentaje sobre el PIB", "Codigo":None, "Abrev":None}
,
{"Id":321, "Nombre":"Infracciones", "Codigo":None, "Abrev":"Infracciones"}
,
{"Id":322, "Nombre":"Horas/dia", "Codigo":None, "Abrev":"H/d"}
,
{"Id":323, "Nombre":"Años-persona", "Codigo":None, "Abrev":None}
,
{"Id":324, "Nombre":"Años-persona", "Codigo":None, "Abrev":None}
,
{"Id":325, "Nombre":"Medidas", "Codigo":None, "Abrev":None}
,
{"Id":326, "Nombre":"Hogares", "Codigo":None, "Abrev":None}
,
{"Id":327, "Nombre":"Hectómetros cúbicos", "Codigo":None, "Abrev":"hm3"}
,
{"Id":328, "Nombre":"Litros habitante y día", "Codigo":None, "Abrev":None}
,
{"Id":329, "Nombre":"Euros por metro cúbico", "Codigo":None, "Abrev":"euros/m3"}
,
{"Id":330, "Nombre":"Equivalencia jornada completa", "Codigo":None, "Abrev":"EJC"}
,
{"Id":331, "Nombre":"Kilogramos/habitante/año", "Codigo":None, "Abrev":None}
,
{"Id":332, "Nombre":"Número medio", "Codigo":None, "Abrev":None}
,
{"Id":334, "Nombre":"Decretos", "Codigo":None, "Abrev":None}
,
{"Id":335, "Nombre":"Madres fallecidas por cada 100.000 nacidos vivos", "Codigo":None, "Abrev":None}
,
{"Id":336, "Nombre":"Suicidios por 100.000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":337, "Nombre":"Defunciones por cada 100.000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":338, "Nombre":"Porcentaje fumadores diarios", "Codigo":None, "Abrev":None}
,
{"Id":339, "Nombre":"Toneladas por habitante", "Codigo":None, "Abrev":None}
,
{"Id":340, "Nombre":"Toneladas por millón de euros", "Codigo":None, "Abrev":None}
,
{"Id":342, "Nombre":"Investigadores (EJC) por cada millón de habitantes", "Codigo":None, "Abrev":None}
,
{"Id":343, "Nombre":"Tanto por 100.000", "Codigo":None, "Abrev":None}
,
{"Id":344, "Nombre":"Por 100.000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":345, "Nombre":"Accidentes por cada cien mil trabajadores", "Codigo":None, "Abrev":None}
,
{"Id":346, "Nombre":"Dolares constantes de 2015", "Codigo":None, "Abrev":None}
,
{"Id":347, "Nombre":"Admisiones", "Codigo":None, "Abrev":None}
,
{"Id":348, "Nombre":"Km2/Ha", "Codigo":None, "Abrev":None}
,
{"Id":349, "Nombre":"Fallecidos por millón", "Codigo":None, "Abrev":None}
,
{"Id":350, "Nombre":"Tasa por cada 100.000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":351, "Nombre":"Kg CO2 equivalente/ Euros", "Codigo":None, "Abrev":None}
,
{"Id":352, "Nombre":"Toneladas CO2 equivalente per cápita", "Codigo":None, "Abrev":None}
,
{"Id":353, "Nombre":"Kilogramo/habitante/día", "Codigo":None, "Abrev":None}
,
{"Id":354, "Nombre":"Toneladas per cápita", "Codigo":None, "Abrev":None}
,
{"Id":355, "Nombre":"LOGICA", "Codigo":None, "Abrev":"NO~SI"}
,
{"Id":356, "Nombre":"tep/M€", "Codigo":None, "Abrev":None}
,
{"Id":357, "Nombre":"Litros de alcohol puro consumido per cápita", "Codigo":None, "Abrev":None}
,
{"Id":358, "Nombre":"Porcentaje de diputadas", "Codigo":None, "Abrev":"%"}
,
{"Id":359, "Nombre":"Porcentaje de senadoras", "Codigo":None, "Abrev":"%"}
,
{"Id":360, "Nombre":"Porcentaje de consejeras", "Codigo":None, "Abrev":"%"}
,
{"Id":361, "Nombre":"Porcentaje de alcaldesas", "Codigo":None, "Abrev":"%"}
,
{"Id":363, "Nombre":"Porcentaje de concejalas", "Codigo":None, "Abrev":"%"}
,
{"Id":364, "Nombre":"Puntos porcentuales", "Codigo":None, "Abrev":None}
,
{"Id":365, "Nombre":"Licencias", "Codigo":None, "Abrev":None}
,
{"Id":366, "Nombre":"Organizaciones", "Codigo":None, "Abrev":None}
,
{"Id":367, "Nombre":"Años al cuadrado", "Codigo":None, "Abrev":None}
,
{"Id":369, "Nombre":"Proporción", "Codigo":None, "Abrev":None}
,
{"Id":370, "Nombre":"Penas", "Codigo":None, "Abrev":"Penas"}
,
{"Id":371, "Nombre":"Por 1.000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":372, "Nombre":"Investigadores (en personas físicas) por cada millón de habitantes", "Codigo":None, "Abrev":None}
,
{"Id":373, "Nombre":"Euros per cápita", "Codigo":None, "Abrev":None}
,
{"Id":374, "Nombre":"Kilogramos per cápita", "Codigo":None, "Abrev":None}
,
{"Id":375, "Nombre":"Euros en relación con dólares americanos", "Codigo":None, "Abrev":None}
,
{"Id":376, "Nombre":"Personas admitidas a tratamiento", "Codigo":None, "Abrev":None}
,
{"Id":377, "Nombre":"Número de tablas", "Codigo":None, "Abrev":None}
,
{"Id":378, "Nombre":"Rango [0,1]", "Codigo":None, "Abrev":None}
,
{"Id":379, "Nombre":"Rango [1,6]", "Codigo":None, "Abrev":None}
,
{"Id":380, "Nombre":"Rango [0,9]", "Codigo":None, "Abrev":None}
,
{"Id":381, "Nombre":"Rango [0,5]", "Codigo":None, "Abrev":None}
,
{"Id":382, "Nombre":"Rango [0,4]", "Codigo":None, "Abrev":None}
,
{"Id":383, "Nombre":"Número de abonados por cada 100 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":384, "Nombre":"Kilotoneladas", "Codigo":None, "Abrev":None}
,
{"Id":385, "Nombre":"Microgramos/metro cúbico", "Codigo":None, "Abrev":None}
,
{"Id":386, "Nombre":"Mil kilómetros cuadrados", "Codigo":None, "Abrev":None}
,
{"Id":387, "Nombre":"Valor de pH", "Codigo":None, "Abrev":None}
,
{"Id":388, "Nombre":"Gramos/euros", "Codigo":None, "Abrev":None}
,
{"Id":389, "Nombre":"Rango [0,10]", "Codigo":None, "Abrev":None}
,
{"Id":390, "Nombre":"€/jornal", "Codigo":None, "Abrev":None}
,
{"Id":392, "Nombre":"Dolares", "Codigo":None, "Abrev":"$"}
,
{"Id":393, "Nombre":"Rango [0,100]", "Codigo":None, "Abrev":None}
,
{"Id":394, "Nombre":"Rango [0,20]", "Codigo":None, "Abrev":None}
,
{"Id":395, "Nombre":"0=NO, 1=SI", "Codigo":None, "Abrev":None}
,
{"Id":396, "Nombre":"Toneladas CO2 equivalente", "Codigo":None, "Abrev":None}
,
{"Id":397, "Nombre":"Muertes por cada 100000 habitantes", "Codigo":None, "Abrev":None}
,
{"Id":398, "Nombre":"Kg por mil euros, volúmenes encadenados (2020)", "Codigo":None, "Abrev":None}
,
{"Id":399, "Nombre":"Empleo equivalente a tiempo completo", "Codigo":None, "Abrev":None}
,
{"Id":400, "Nombre":"Gigajulios por habitante", "Codigo":None, "Abrev":"GJ/hab"}
,
{"Id":401, "Nombre":"Terajulios por millón de euros", "Codigo":None, "Abrev":"TJ/M euros"}
,
{"Id":402, "Nombre":"Millones de euros", "Codigo":None, "Abrev":"mill. €"}
,
{"Id":403, "Nombre":"Kilotoneladas equivalentes de petróleo", "Codigo":None, "Abrev":"ktep"}
,
{"Id":405, "Nombre":"Euros por habitante", "Codigo":None, "Abrev":None}
,
{"Id":406, "Nombre":"Millones de toneladas equivalentes de petróleo (Mtep)", "Codigo":None, "Abrev":None}
,
{"Id":407, "Nombre":"Toneladas equivalentes de petróleo por habitante (tep/hab)", "Codigo":None, "Abrev":None}
,
{"Id":408, "Nombre":"Vatios per cápita", "Codigo":None, "Abrev":None}
,
{"Id":409, "Nombre":"Rango [0,3]", "Codigo":None, "Abrev":None}
,
{"Id":410, "Nombre":"Rango [1,4]", "Codigo":None, "Abrev":None}
,
{"Id":411, "Nombre":"Megajulios per cápita", "Codigo":None, "Abrev":None}
,
{"Id":412, "Nombre":"Kg de CO2 equivalente per capita", "Codigo":None, "Abrev":None}
,
{"Id":413, "Nombre":"Miles de personas", "Codigo":None, "Abrev":"miles de personas"}
,
{"Id":414, "Nombre":"Miles de Toneladas CO2 equivalente", "Codigo":None, "Abrev":"miles de t. CO2 eq."}
,
{"Id":415, "Nombre":"Euros por unidad de consumo", "Codigo":None, "Abrev":None}
,
{"Id":416, "Nombre":"Euros/m2", "Codigo":None, "Abrev":None}
,
{"Id":417, "Nombre":"Miles de toneladas netas", "Codigo":None, "Abrev":None}
,
{"Id":418, "Nombre":"Millones de viajeros-km", "Codigo":None, "Abrev":None}
,
{"Id":419, "Nombre":"Miles de Toneladas", "Codigo":None, "Abrev":None}
,
{"Id":420, "Nombre":"Migraciones", "Codigo":None, "Abrev":None}
]

Es = [{"Id":1, "Nombre":" ", "Factor":"1E0", "Codigo":"0", "Abrev":None}
,{"Id":2, "Nombre":"Decenas", "Factor":"1E1", "Codigo":"1", "Abrev":"Decenas"}
,{"Id":3, "Nombre":"Centenas", "Factor":"1E2", "Codigo":"2", "Abrev":"Centenas"}
,{"Id":4, "Nombre":"Miles", "Factor":"1E3", "Codigo":"3", "Abrev":"Miles"}
,{"Id":5, "Nombre":"Décimas", "Factor":"1E-1", "Codigo":"-1", "Abrev":"Décimas"}
,{"Id":6, "Nombre":"Millonésimas", "Factor":"1E-6", "Codigo":"-6", "Abrev":"Millonésimas"}
,{"Id":7, "Nombre":"Centésimas de milésimas", "Factor":"1E-5", "Codigo":"-5", "Abrev":"Centésimas de milésimas"}
,{"Id":8, "Nombre":"Décimas de milésimas", "Factor":"1E-4", "Codigo":"-4", "Abrev":"Décimas de milésimas"}
,{"Id":9, "Nombre":"Milésimas", "Factor":"1E-3", "Codigo":"-3", "Abrev":"Milésimas"}
,{"Id":10, "Nombre":"Centésimas", "Factor":"1E-2", "Codigo":"-2", "Abrev":"Centésimas"}
,{"Id":11, "Nombre":"Decenas de miles", "Factor":"1E4", "Codigo":"4", "Abrev":"Decenas de miles"}
,{"Id":12, "Nombre":"Centenas de miles", "Factor":"1E5", "Codigo":"5", "Abrev":"Centenas de miles"}
,{"Id":13, "Nombre":"Millones", "Factor":"1E6", "Codigo":"6", "Abrev":"Millones"}
,{"Id":14, "Nombre":"Decenas de millones", "Factor":"1E7", "Codigo":"7", "Abrev":"Decenas de millones"}
,{"Id":15, "Nombre":"Centenas de millones", "Factor":"1E8", "Codigo":"8", "Abrev":"Centenas de millones"}
,{"Id":16, "Nombre":"Miles de millones", "Factor":"1E9", "Codigo":"9", "Abrev":"Miles de millones"}
,{"Id":17, "Nombre":"Decenas de miles de millones", "Factor":"1E10", "Codigo":"10", "Abrev":"Dec. de miles de millones"}
,{"Id":18, "Nombre":"Centenas de miles de millones", "Factor":"1E11", "Codigo":"11", "Abrev":"Cent. miles de millones"}
,{"Id":19, "Nombre":"Billones", "Factor":"1E12", "Codigo":"12", "Abrev":"Billones"}
,{"Id":20, "Nombre":"Decenas de billones", "Factor":"1E13", "Codigo":"13", "Abrev":"Decenas de billones"}
,{"Id":21, "Nombre":"Centenas de billones", "Factor":"1E14", "Codigo":"14", "Abrev":"Centenas de billones"}
,{"Id":22, "Nombre":"Miles de billones", "Factor":"1E15", "Codigo":"15", "Abrev":"Miles de billones"}
,{"Id":24, "Nombre":"Décimas de millones", "Factor":"1E-7", "Codigo":"-7", "Abrev":"Décimas de millones"}
,{"Id":25, "Nombre":"Centésimas de millones", "Factor":"1E-8", "Codigo":"-8", "Abrev":"Centésimas de millones"}
,{"Id":26, "Nombre":"Billonésimas", "Factor":"1E-9", "Codigo":"-9", "Abrev":"Billonésimas"}
,{"Id":27, "Nombre":"Décimas de billones", "Factor":"1E-10", "Codigo":"-10", "Abrev":"Décimas de billones"}
,{"Id":28, "Nombre":"Centésimas de billones", "Factor":"1E-11", "Codigo":"-11", "Abrev":"Centésimas de billones"}
,{"Id":29, "Nombre":"Trillonésimas", "Factor":"1E-12", "Codigo":"-12", "Abrev":"Trillonésimas"}
]

Pe = [{"Id":0, "Nombre":"Al Detalle", "Codigo":"N"}
,
{"Id":1, "Nombre":"Mensual", "Codigo":"M"}
,
{"Id":2, "Nombre":"Bimestral", "Codigo":"BM"}
,
{"Id":3, "Nombre":"Trimestral", "Codigo":"Q"}
,
{"Id":4, "Nombre":"Cuatrimestral", "Codigo":"F"}
,
{"Id":6, "Nombre":"Semestral", "Codigo":"S"}
,
{"Id":7, "Nombre":"Semanal", "Codigo":"W"}
,
{"Id":12, "Nombre":"Anual", "Codigo":"A"}
,
{"Id":13, "Nombre":"Bienal Impar", "Codigo":"ABI"}
,
{"Id":14, "Nombre":"Bienal Par", "Codigo":"ABP"}
,
{"Id":30, "Nombre":"Diario", "Codigo":"D"}
,
{"Id":31, "Nombre":"Diario-business week", "Codigo":"B"}
,
{"Id":100, "Nombre":"SIN PERIODICIDAD", "Codigo":"SP"}
,
{"Id":103, "Nombre":"Cada hora", "Codigo":"H"}
,
{"Id":104, "Nombre":"Cada minuto", "Codigo":""}
,
{"Id":105, "Nombre":"Cuatrienal", "Codigo":"C"}
,
{"Id":106, "Nombre":"Trienal", "Codigo":""}
,
{"Id":107, "Nombre":"Anual sin determinar", "Codigo":""}
,
{"Id":108, "Nombre":"Quinquenal", "Codigo":""}
,
{"Id":111, "Nombre":"Cuatrienal Base 3", "Codigo":"C3"}
,
{"Id":112, "Nombre":"Trienal Base 2003", "Codigo":"T3"}
]
