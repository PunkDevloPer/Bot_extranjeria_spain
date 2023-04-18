# Bot_extranjeria_spain

I program this automated process to make my asylum application in Spain.
To use it, you just have to download it and edit the dictionary with the following parameters
data = [{"passaport": "here", "Name": "here", "birthdate": here, "Country": "here"},
        {"passaport": "here", "Name": "here", "birthdate": here, "Country": "here"}
         ]
  and edit the paramether of repetition alone if it is necesary in line 46 for default is 6
  
if your procedure and province  is  different edit the lines
26 and 27 of province 
selection = driver.find_element(By.XPATH, "//*[@id='form']/option[16]") 
selection.send_keys("Castellón")

# Provinces
"//*[@id='form']/option[2]" = A Coruña
"//*[@id='form']/option[3]" = Albacete
"//*[@id='form']/option[4]" = Alicante
"//*[@id='form']/option[5]" = Almeria
"//*[@id='form']/option[6]" = Araba
"//*[@id='form']/option[7]" = asturias
"//*[@id='form']/option[8]" = avila
"//*[@id='form']/option[9]" =  badajoz
"//*[@id='form']/option[10]" = Barcelona
"//*[@id='form']/option[11]" = Bizkaia
"//*[@id='form']/option[12]" = Burgos
"//*[@id='form']/option[13]" = Caseres
"//*[@id='form']/option[14]" = Cadiz
"//*[@id='form']/option[15]" = Cantabria
"//*[@id='form']/option[16]" = Castellón
"//*[@id='form']/option[17]" = Ceuta
"//*[@id='form']/option[18]" = Ciudad Real
"//*[@id='form']/option[19]" = Cordoba
"//*[@id='form']/option[20]"=  Cuenca
"//*[@id='form']/option[21]"=  Gipuzkoa
"//*[@id='form']/option[22]"= Girona
"//*[@id='form']/option[23]"= Granada
"//*[@id='form']/option[24]"= Guadalaraja
"//*[@id='form']/option[25]"= Huelva
"//*[@id='form']/option[26]" = huesca
"//*[@id='form']/option[27]" = Illes Balears
"//*[@id='form']/option[28]" = Jaén
"//*[@id='form']/option[29]" = La Rioja
"//*[@id='form']/option[30]" = Las Palmas
"//*[@id='form']/option[31]" = León
"//*[@id='form']/option[32]" = Lleida
"//*[@id='form']/option[33]" = Lugo
"//*[@id="form"]/option[34]" = Madrid
"//*[@id='form']/option[35]" = Málaga
"//*[@id='form']/option[36]" = Melilla
"//*[@id='form']/option[37]" = Murcia
"//*[@id='form']/option[38]" = Navarra
"//*[@id='form']/option[39]" = Ourense
"//*[@id='form']/option[40]" = Palencia
"//*[@id='form']/option[41]" = Pontevedra
"//*[@id='form']/option[42]" = Salamanca
"//*[@id='form']/option[43]" = S.Cruz Tenerife
"//*[@id='form']/option[44]" = Segovia
"//*[@id='form']/option[45]" = Sevilla
"//*[@id='form']/option[46]" = Soria
"//*[@id='form']/option[47]" = Tarragona
"//*[@id='form']/option[48]" = Teruel
"//*[@id='form']/option[47]" = Toled
"//*[@id='form']/option[49]" = Valenia
"//*[@id='form']/option[50]" = Vallaolid
"//*[@id='form']/option[51]" = Zamor
"//*[@id='form']/option[52]" = Zaragoza

and lines 
33 to 38 of procedure

droptramit = Select(driver.find_element(
    By.XPATH, "//*[@id='tramiteGrupo[0]']")) -> here  procedure tramiegroup 
droptramit.select_by_visible_text("POLICIA- SOLICITUD ASILO") -> here procedure name

NOTE: in some provinces the procedure group changes, so it is advisable to investigate the page to find out if the procedure is in group 0 or group 1


"//*[@id='sede']/option"  = All office

Procedure in office of extranger
"//*[@id='tramiteGrupo[0]']/option[2]" = ACCESO A 1ª AUT. DE RESIDENCIA DE LARGA DURACIÓN Y LARGA DURACIÓN UE
"//*[@id='tramiteGrupo[0]']/option[3]" = AUT. DE RESIDENCIA TEMPORAL POR CIRCUNS. EXCEPCIONALES POR ARRAIGO
"//*[@id='tramiteGrupo[0]']/option[4]" = AUTORIZACIONES DE TRABAJO POR ESTUDIOS
"//*[@id='tramiteGrupo[0]']/option[5]" = ESTANCIA POR ESTUDIOS
"//*[@id='tramiteGrupo[0]']/option[6]" = FAMILIARES DE RESIDENTES COMUNITARIOS
"//*[@id='tramiteGrupo[0]']/option[7]" = PRORROGA DE ESTANCIA POR ESTUDIOS
"//*[@id='tramiteGrupo[0]']/option[8]" = REAGRUPACIÓN FAMILIAR
"//*[@id='tramiteGrupo[0]']/option[9]" = RENOVACIONES DE AUT. DE RESIDENCIA  y/o  AUT. DE RESIDENCIA Y TRABAJO
"//*[@id='tramiteGrupo[0]']/option[10]" = RENOVACIONES DE AUTORIZACIÓN DE RESIDENCIA CON TRABAJO
"//*[@id='tramiteGrupo[0]']/option[11]" = RENOVACIÓN AUTORIZACIÓN RESIDENCIA POR REAGRUPACIÓN FAMILIAR
"//*[@id='tramiteGrupo[0]']/option[12]" = TRABAJO Y RESIDENCIA INICIAL POR CUENTA AJENA


procedure of department of police
"//*[@id='tramiteGrupo[1]']/option[2]" = POLICIA - RECOGIDA DE TARJETA DE IDENTIDAD DE EXTRANJERO (TIE)
"//*[@id='tramiteGrupo[1]']/option[3]" = POLICIA- EXPEDICIÓN/RENOVACIÓN DE DOCUMENTOS DE SOLICITANTES DE ASILO
"//*[@id='tramiteGrupo[1]']/option[4]" = POLICIA- SOLICITUD ASILO
"//*[@id='tramiteGrupo[1]']/option[5]" = POLICIA-ASIGNACIÓN DE NIE
"//*[@id='tramiteGrupo[1]']/option[6]" = POLICIA-ASILO INFORMACION 
"//*[@id='tramiteGrupo[1]']/option[7]" = POLICIA-AUTORIZACIÓN DE REGRESO
"//*[@id='tramiteGrupo[1]']/option[8]" = POLICIA-CARTA DE INVITACIÓN
"//*[@id='tramiteGrupo[1]']/option[9]"= POLICIA-CERTIFICADOS (DE RESIDENCIA, DE NO RESIDENCIA Y DE CONCORDANCIA)
"//*[@id='tramiteGrupo[1]']/option[10]" = POLICIA-CERTIFICADOS UEs
"//*[@id='tramiteGrupo[1]']/option[11]" = POLICIA-CERTIFICADOS Y ASIGNACION NIE
"//*[@id='tramiteGrupo[1]']/option[12]" = POLICIA-INFORMACION DE TRÁMITES DE LA COMISARÍA DE POLICIA
"//*[@id='tramiteGrupo[1]']/option[13]" = POLICÍA - UCRANIA : SOLICITUD PROTECCIÓN TEMPORAL DESPLAZADOS
"//*[@id='tramiteGrupo[1]']/option[14]" = POLICÍA TARJETA CONFLICTO UCRANIA–ПОЛІЦІЯ -КАРТКА ДЛЯ ПЕРЕМІЩЕНИХ ОСІБ ВНАСЛІДОК КОНФЛІКТУ В УКРАЇНІ
"//*[@id='tramiteGrupo[1]']/option[15]" = POLICÍA-EXP.TARJETA ASOCIADA AL ACUERDO DE RETIRADA CIUDADANOS BRITÁNICOS Y SUS FAMILIARES (BREXIT)
