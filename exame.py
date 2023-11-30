


def main():
    while True:
        print("-="*20)
        print("Seja bem vindo")
        print("-="*20)
        print("Gostaria de fazer a avaliação? ")
        print("1-sim // 2-não")
        paciente = input("Digite 1 ou 2: " )

        if paciente == "1":
            sexo()

        elif paciente == "2":
            print ("Ok, encerrando.")
            exit()

        else:
            print(f'Opção {paciente} inválida. Digite apenas sim ou não.')

def sexo():
    while True:
        print("Informe seu sexo biológico")
        print ("M = masculino // F = feminino")
        paciente = input("Digite M ou F: ")
        if paciente == "M":
            tipo_exameM()
        elif paciente == "F":
            tipo_exameF()
            

        else:
            print(f"Opção {paciente} inválida. Digite apenas a letra M ou F")



###################################


#HOMEM


###################################



def tipo_exameM():
    while True:
        print("Você gostaria de receber resultados de quais tipos de exame?")
        print("1- Hemograma Completo")
        print("2- Glicemia")
        print("3- Creatina")
        print("4- Ácido úrico")
        print("5- Transaminase Glutamico Oxalacética - TGO")
        print("6- Trasaminase Glutamico Pirúvica - TGP")
        print("7- Lipidograma Completo")
        print("8- 25-Hidroxivitamina D")
        print("9- TSH Ultra Sensível")
        print("10- T4 Livre")
        print("11 - Opção para receber resultados de todos os exames")
        print("-"*30)
        print("CASO QUEIRA SAIR, DIGITE: 12")
        print("-"*30)

        paciente = input("Digite sua escolha: ")

        if paciente == "1": 
            hemograma()

        elif paciente =="2":
            glicemia()

        elif paciente =="3":
            creatina()
            
        elif paciente =="4":
            acido_urico()
        elif paciente =="5":
            tgo()
        elif paciente =="6":
            tgp()
        elif paciente =="7":
            lipidograma()
        elif paciente =="8":
            hidroxivitamina()
        elif paciente =="9":
            tsh()
        elif paciente =="10":
            t4_livre()
        elif paciente =="11":
            todos()
        elif paciente =="12":
            exit()
        else:
            print(f"Opção {paciente} inválida. Digite Novamente.")

    
def leiaInt(msg):
    ok = False
    valor = 0 
    while True:
         n = str(input(msg))
         if n.isnumeric():
             valor = int(n)
             ok = True
         else:
             print("digite um número ")
         if ok:
             break
    return valor


def hemograma():
    print("Coloque os valores de cada requisito")
    print ("ERITROGRAMA")
    hemacias = leiaInt("Hemácias: ")
    hemoglobina = leiaInt("Hemoglobina: ")
    hematocrito = leiaInt("Hematocrito: ")
    hb_corp_média = leiaInt("Hb corp média: ")
    volume_corp_médio = leiaInt("Volume corp médio: ")
    conc_hb_corp_media = leiaInt("Conc. Hb. Corp. Média: ")
    RDW = leiaInt("RDW: ")


    print("LEUCOGRAMA")
    leucocitos = leiaInt("Leucocitos: ")
    metamielócitos = leiaInt("Metamielócitos: ")
    bastonetes = leiaInt("Bastoneres: ")
    segmentados = leiaInt("Segmentados: ")
    eosinofilos = leiaInt("Eosinófilos: ")
    basofilos = leiaInt("Basofilos: ")
    linfocitos = leiaInt("Linfocitos: ")
    monocitos = leiaInt("Monocitos: ")
    plaquetas = leiaInt("Plaquetas: ")

    if hemacias >=4.5 and hemacias <=6:
        print( "Hemácias: está na média")
    elif hemacias < 4.5:
        print( "Hemácias: abaixo da média")
    
    elif hemacias > 6:
        print( "Hemácias: acima da média")
    
    #########################
    
    if hemoglobina >=13 and hemoglobina <=17.8:
        print( "Hemoglobina: está na média")
    elif hemoglobina <13:
        print( "Hemoglobina: abaixo da média")
    elif hemoglobina > 17.8:
        print( "Hemoglobina: acima da média")
    
    ########################
    if hematocrito >=40 and hematocrito <=54:
        print( "Hematocrito: está na média")
    elif hematocrito < 40:
        print( "Hematocrito: abaixo da média")
    elif hematocrito > 54:
        print( "Hematocrito: acima da média")
    
    ##########################
    if hb_corp_média >=27 and hb_corp_média <=33:
        print( "Hb corp média: está na média")
    elif hb_corp_média < 27:
        print( "Hb corp média: abaixo da média")
    
    elif hb_corp_média > 33:
        print( "Hb corp média: acima da média")
    
    #########################
    if volume_corp_médio >=80 and volume_corp_médio <=100:
        print( "Volume corp médio: está na média")
    elif volume_corp_médio < 80:
        print( "Volume corp médio: abaixo da média")
    
    elif volume_corp_médio > 100:
        print( "Volume corp médio: acima da média")
    
    #########################
    if conc_hb_corp_media >=30 and conc_hb_corp_media <=36:
        print( "Conc. Hb. Corp. Média: está na média")
    elif conc_hb_corp_media < 30:
        print( "Conc. Hb. Corp. Média: abaixo da média")
    
    elif conc_hb_corp_media > 36:
        print( "Conc. Hb. Corp. Média: acima da média")
    
    #########################
    if RDW >=11 and RDW <=14.5:
        print( "RDW: está na média")
    elif RDW < 11:
        print( "RDW: abaixo da média")
    
    elif RDW > 14.5:
        print( "RDW: acima da média")
    
    #########################
    #leucograma
    if leucocitos >=3900 and leucocitos <=12100:
        print( "Leucocitos: está na média")
    elif leucocitos < 3900:
        print( "Leucocitos: abaixo da média")
    
    elif leucocitos > 12100:
        print( "Leucocitos: acima da média")
    
    #########################
    if metamielócitos ==0:
        print( "Metamielócitos: está na média")
    elif metamielócitos < 0:
        print( "Metamielócitos: abaixo da média")
    
    elif metamielócitos > 0:
       print("Metamielócitos: acima da média")
    
    #########################
    if bastonetes >=1 and bastonetes <=6:
        print( "Bastonetes: está na média")
    elif bastonetes < 1:
        print( "Bastonetes: abaixo da média")
    
    elif bastonetes > 6:
        print( "Bastonetes: acima da média")
    
    #########################
    if segmentados >=50 and segmentados <=68:
        print( "Segmentados: está na média")
    elif segmentados < 50:
        print( "Segmentados: abaixo da média")
    
    elif segmentados > 68:
        print( "Segmentados: acima da média")
    
    #########################
    if eosinofilos >=1 and eosinofilos <=8:
        print( "Eosinófilos: está na média")
    elif eosinofilos < 1:
        print("Eosinófilos: abaixo da média")
    
    elif eosinofilos > 8:
        print( "Eosinófilos: acima da média")
    
    #########################
    if basofilos >=0 and basofilos <=2:
        print( "Basófilos: está na média")
    elif basofilos < 0:
        print( "Basófilos: abaixo da média")
    
    elif basofilos > 2:
        print( "Basófilos: acima da média")
    
    #########################
    if linfocitos >=18 and linfocitos <=44:
        print( "Linfócitos: está na média")
    elif linfocitos < 18:
        print( "Linfócitos: abaixo da média")
    
    elif linfocitos> 44:
        print( "Linfócitos: acima da média")
    
    #########################
    if monocitos>=2 and monocitos <=12:
        print( "Monócitos: está na média")
    elif monocitos < 2:
        print( "Monócitos: abaixo da média")
    
    elif monocitos > 12:
        print( "Monócitos: acima da média")
    #########################
    if plaquetas >=150000 and plaquetas <=450000:
        print( "Plaquetas: está na média")
    elif plaquetas < 150000:
        print( "Plaquetas: abaixo da média")
    
    elif plaquetas > 450000:
        print( "Plaquetas: acima da média")
    
    #########################


    
    


########################################

def glicemia():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
 
    if resultado >=60 and resultado<= 99:
        print ("Glicemia: está na média")
    elif resultado < 60:
        print ("Glicemia: abaixo da média")
    
    elif resultado > 99:
        print("Glicemia: acima da média")
   
    
    



########################################



def creatina():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
  

    if resultado >=0.76 and resultado<= 1.24:
        print ("Creatina: está na média")
    elif resultado < 0.76:
        print("Creatina: abaixo da média")
    
    elif resultado > 1.24:
        print("Creatina: acima da média")


########################################
def acido_urico():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
   
    if resultado >=3.7 and resultado<= 7.8:
        print("Ácido úrico: está na média")
    elif resultado < 3.7:
        print("Ácido úrico: abaixo da média")
    
    elif resultado > 7.8:
        print("Ácido úrico: acima da média")



########################################
def tgo():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
   
    
    if resultado <= 40:
        print("TGO: na média")
    
    elif resultado > 40:
        print("TGO: acima da média")


########################################
    
def tgp():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
    

    if resultado <= 58:
        print("TGP: na média")
    
    elif resultado > 58:
        print("TGP: acima da média")



########################################
def lipidograma():
    colesterol = leiaInt("Colesterol total: ")
    hdl = leiaInt("Colesterol HDL: ")
    ldl = leiaInt("Colesterol LDL: ")
    nhdl = leiaInt("Colesterol Não-HDL: ")
    triglicerides = leiaInt("Triglicerides: ")

    if colesterol <= 190:
        print("Colesterol: na média")
    
    elif colesterol > 190:
        print("Colesterol: acima da média")
    
    #########################
    if hdl >= 40:
        print("HDL: na média")
    
    elif hdl < 40:
        print("HDL: abaixo da média")
    
    #########################
    if ldl <= 130:
        print("LDL: risco baixo")

    elif ldl <=100:
        print("LDL: risco intermediario")

    elif ldl <=70:
        print("LDL: risco alto")

    elif ldl <=50:
        print("LDL: risco muito alto")
    
    elif ldl > 130:
        print( "LDL: acima da média")

    
    
    #########################
    
    if nhdl <= 160:
        print("Não-HDL: risco baixo")

    elif nhdl <=130:
        print("Não-HDL: risco intermediario")

    elif nhdl <=100:
        print("Não-HDL: risco alto")

    elif nhdl <=80:
        print("Não-HDL: risco muito alto")
    
    elif nhdl > 160:
        print( "Não-HDL: acima da média")
    
    #########################
    if triglicerides < 150:
        print( "Triglicerides: está na média")
    
    elif triglicerides > 150:
        print( "Triglicerides: acima da média")
    
    #########################





########################################

def hidroxivitamina():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
   

    
    if resultado > 20:
        print( "Hidroxivitamina: saudável")
    
    elif resultado < 20:
        print( "Hidroxivitamina: não saudável")

########################################

def tsh():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
  

    if resultado >=0.38 and resultado<= 5.33:
        print( "TSH: está na média")
    elif resultado < 0.38:
        print( "TSH: abaixo da média")
    
    elif resultado > 5.33:
        print( "TSH: acima da média")

########################################

def t4_livre():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")

    if resultado >=0.54 and resultado<= 1.24:
        print( "T4 Livre: está na média")
    elif resultado < 0.54:
        print( "T4 Livre: abaixo da média")
    
    elif resultado > 1.24:
        print("T4 Livre: acima da média")

########################################
def todos(): 
    hemograma()
    glicemia()
    creatina()
    acido_urico()
    tgo()
    tgp()
    lipidograma()
    hidroxivitamina()
    tsh()
    t4_livre()
    

##################################
 
 
#MULHER
 
 
###################################
 
def tipo_exameF():
    while True:
        print("Você gostaria de cadastrar quais tipos de exame?")
        print("1- Hemograma Completo")
        print("2- Glicemia")
        print("3- Creatina")
        print("4- Ácido úrico")
        print("5- Transaminase Glutamico Oxalacética - TGO")
        print("6- Trasaminase Glutamico Pirúvica - TGP")
        print("7- Lipidograma Completo")
        print("8- 25-Hidroxivitamina D")
        print("9- TSH Ultra Sensível")
        print("10- T4 Livre")
        print("11 - Opção para cadastrar todos os exames")
 
        paciente = input("Digite sua escolha: ")
 
        if paciente == "1":
            hemogramaF()
 
        elif paciente =="2":
            glicemiaF()
 
        elif paciente =="3":
            creatinaF()
           
        elif paciente =="4":
            acido_uricoF()
        elif paciente =="5":
            tgoF()
        elif paciente =="6":
            tgpF()
        elif paciente =="7":
            lipidogramaF()
        elif paciente =="8":
            hidroxivitaminaF()
        elif paciente =="9":
            tshF()
        elif paciente =="10":
            t4_livreF()
        elif paciente =="11":
            todosF()
        else:
            print(f"Opção {paciente} inválida. Digite Novamente.")
 
 
def hemogramaF():
    print("Coloque os valores de cada requisito")
    print ("ERITROGRAMA")
    hemacias = leiaInt("Hemácias: ")
    hemoglobina = leiaInt("Hemoglobina: ")
    hematocrito = leiaInt("Hematocrito: ")
    hb_corp_média = leiaInt("Hb corp média: ")
    volume_corp_médio = leiaInt("Volume corp médio: ")
    conc_hb_corp_media = leiaInt("Conc. Hb. Corp. Média: ")
    RDW = leiaInt("RDW: ")
 
 
    print("LEUCOGRAMA")
    leucocitos = leiaInt("Leucocitos: ")
    metamielócitos = leiaInt("Metamielócitos: ")
    bastonetes = leiaInt("Bastoneres: ")
    segmentados = leiaInt("Segmentados: ")
    eosinofilos = leiaInt("Eosinófilos: ")
    basofilos = leiaInt("Basofilos: ")
    linfocitos = leiaInt("Linfocitos: ")
    monocitos = leiaInt("Monocitos: ")
    plaquetas = leiaInt("Plaquetas: ")
 
    if hemacias >=3.7 and hemacias <=5.2:
        print( "Hemácias: está na média")
    elif hemacias < 3.7:
        print( "Hemácias: abaixo da média")
   
    elif hemacias > 5.2:
        print( "Hemácias: acima da média")
   
    #########################
   
    if hemoglobina >=11 and hemoglobina <=16:
        print( "Hemoglobina: está na média")
    elif hemoglobina <11:
        print( "Hemoglobina: abaixo da média")
    elif hemoglobina > 16:
        print( "Hemoglobina: acima da média")
   
    ########################
    if hematocrito >=36 and hematocrito <=47:
        print( "Hematocrito: está na média")
    elif hematocrito < 36:
        print( "Hematocrito: abaixo da média")
    elif hematocrito > 47:
        print( "Hematocrito: acima da média")
   
    ##########################
    if hb_corp_média >=27 and hb_corp_média <=33:
        print( "Hb corp média: está na média")
    elif hb_corp_média < 27:
        print( "Hb corp média: abaixo da média")
   
    elif hb_corp_média > 33:
        print( "Hb corp média: acima da média")
   
    #########################
    if volume_corp_médio >=80 and volume_corp_médio <=100:
        print( "Volume corp médio: está na média")
    elif volume_corp_médio < 80:
        print( "Volume corp médio: abaixo da média")
   
    elif volume_corp_médio > 100:
        print( "Volume corp médio: acima da média")
   
    #########################
    if conc_hb_corp_media >=30 and conc_hb_corp_media <=36:
        print( "Conc. Hb. Corp. Média: está na média")
    elif conc_hb_corp_media < 30:
        print( "Conc. Hb. Corp. Média: abaixo da média")
   
    elif conc_hb_corp_media > 36:
        print( "Conc. Hb. Corp. Média: acima da média")
   
    #########################
    if RDW >=11 and RDW <=14.5:
        print( "RDW: está na média")
    elif RDW < 11:
        print( "RDW: abaixo da média")
   
    elif RDW > 14.5:
        print( "RDW: acima da média")
   
    #########################
    #leucograma
    if leucocitos >=3900 and leucocitos <=12100:
        print( "Leucocitos: está na média")
    elif leucocitos < 3900:
        print( "Leucocitos: abaixo da média")
   
    elif leucocitos > 12100:
        print( "Leucocitos: acima da média")
   
    #########################
    if metamielócitos ==0:
        print( "Metamielócitos: está na média")
    elif metamielócitos < 0:
        print( "Metamielócitos: abaixo da média")
   
    elif metamielócitos > 0:
       print("Metamielócitos: acima da média")
   
    #########################
    if bastonetes >=1 and bastonetes <=6:
        print( "Bastonetes: está na média")
    elif bastonetes < 1:
        print( "Bastonetes: abaixo da média")
   
    elif bastonetes > 6:
        print( "Bastonetes: acima da média")
   
    #########################
    if segmentados >=50 and segmentados <=68:
        print( "Segmentados: está na média")
    elif segmentados < 50:
        print( "Segmentados: abaixo da média")
   
    elif segmentados > 68:
        print( "Segmentados: acima da média")
   
    #########################
    if eosinofilos >=1 and eosinofilos <=8:
        print( "Eosinófilos: está na média")
    elif eosinofilos < 1:
        print("Eosinófilos: abaixo da média")
   
    elif eosinofilos > 8:
        print( "Eosinófilos: acima da média")
   
    #########################
    if basofilos >=0 and basofilos <=2:
        print( "Basófilos: está na média")
    elif basofilos < 0:
        print( "Basófilos: abaixo da média")
   
    elif basofilos > 2:
        print( "Basófilos: acima da média")
   
    #########################
    if linfocitos >=18 and linfocitos <=44:
        print( "Linfócitos: está na média")
    elif linfocitos < 18:
        print( "Linfócitos: abaixo da média")
   
    elif linfocitos> 44:
        print( "Linfócitos: acima da média")
   
    #########################
    if monocitos>=2 and monocitos <=12:
        print( "Monócitos: está na média")
    elif monocitos < 2:
        print( "Monócitos: abaixo da média")
   
    elif monocitos > 12:
        print( "Monócitos: acima da média")
    #########################
    if plaquetas >=150000 and plaquetas <=450000:
        print( "Plaquetas: está na média")
    elif plaquetas < 150000:
        print( "Plaquetas: abaixo da média")
   
    elif plaquetas > 450000:
        print( "Plaquetas: acima da média")
   
    #########################
 
 
   
   
 
 
########################################
 
def glicemiaF():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
   
 
    if resultado >=60 and resultado<= 99:
        print ("Glicemia: está na média")
    elif resultado < 60:
        print ("Glicemia: abaixo da média")
   
    elif resultado > 99:
        print("Glicemia: acima da média")
   
   
   
 
 
 
########################################
 
 
 
def creatinaF():
    print("Coloque os valores de cada requisito")
    resultado = leiaInt("Resultado: ")
   
    if resultado >=0.4 and resultado<= 1:
        print ("Creatina: está na média")
    elif resultado < 0.4:
        print("Creatina: abaixo da média")
   
    elif resultado > 1:
        print("Creatina: acima da média")
        
###############################
 
#...........FAZER AS FUNÇÕES ÁCIDO, TGO, TGP, LIPIDOGRAMA, TSH, T4 LIVRE PARA MULHER.........
 
###############################
   
def todosF():
    hemogramaF()
    glicemiaF()
    creatinaF()
    acido_uricoF()
    tgoF()
    tgpF()
    lipidogramaF()
    hidroxivitaminaF()
    tshF()
    t4_livreF()

if __name__ == "__main__":
    main()

