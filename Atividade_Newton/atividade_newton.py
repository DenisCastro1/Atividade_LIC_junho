#exercício 1

def media(nota1,nota2):
    media=(nota1+nota2)/2
    return media


#exercicio 2
series=open("series.csv","r")

lista_series=series.readlines()

series_novas=open("series_novas.csv","r")

lista_series_novas=series_novas.readlines()

lista_completa=lista_series+lista_series_novas

#exercicio 3
temp1=0
temp2=0
temp3=0
temp4=0
temp5=0
temp6=0
temp7=0
temp8=0
temp9=0
temp10=0
temp11=0
temp12=0
somatoria=0
somatoria2=0
tempo1=0
tempo2=0
tempo3=0
tempo4=0
tempo5=0
tempo6=0
tempo7=0
tempo8=0
tempo9=0
tempo10=0
somatoria3=0
somatoria4=0
black1=0
black2=0
black3=0
black4=0
black5=0
somatoria5=0
somatoria6=0
breaking1=0
breaking2=0
breaking3=0
breaking4=0
breaking5=0
somatoria7=0
somatoria8=0


for elemento in lista_completa:
    separado=elemento.split(",")
    if separado[0]=="The Big Bang Theory" and separado[1]=="1":
        temp1=temp1+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="2":
        temp2=temp2+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="3":
        temp3=temp3+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="4":
        temp4=temp4+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="5":
        temp5=temp5+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="6":
        temp6=temp6+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="7":
        temp7=temp7+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="8":
        temp8=temp8+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="9":
        temp9=temp9+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="10":
        temp10=temp10+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="11":
        temp11=temp11+1
    elif separado[0]=="The Big Bang Theory" and separado[1]=="12":
        temp12=temp12+1

    elif separado[0]=="Friends" and separado[1]=="1":
        tempo1=tempo1+1
    elif separado[0]=="Friends" and separado[1]=="2":
        tempo2=tempo2+1
    elif separado[0]=="Friends" and separado[1]=="3":
        tempo3=tempo3+1
    elif separado[0]=="Friends" and separado[1]=="4":
        tempo4=tempo4+1
    elif separado[0]=="Friends" and separado[1]=="5":
        tempo5=tempo5+1
    elif separado[0]=="Friends" and separado[1]=="6":
        tempo6=tempo6+1
    elif separado[0]=="Friends" and separado[1]=="7":
        tempo7=tempo7+1
    elif separado[0]=="Friends" and separado[1]=="8":
        tempo8=tempo8+1
    elif separado[0]=="Friends" and separado[1]=="9":
        tempo9=tempo9+1
    elif separado[0]=="Friends" and separado[1]=="10":
        tempo10=tempo10+1
        
    elif separado[0]=="Black Mirror" and separado[1]=="1":
        black1=black1+1
    elif separado[0]=="Black Mirror" and separado[1]=="2":
        black2=black2+1
    elif separado[0]=="Black Mirror" and separado[1]=="3":
        black3=black3+1
    elif separado[0]=="Black Mirror" and separado[1]=="4":
        black4=black4+1
    elif separado[0]=="Black Mirror" and separado[1]=="5":
        black5=black5+1
        
    elif separado[0]=="Breaking Bad" and separado[1]=="1":
        breaking1=breaking1+1
    elif separado[0]=="Breaking Bad" and separado[1]=="2":
        breaking2=breaking2+1
    elif separado[0]=="Breaking Bad" and separado[1]=="3":
        breaking3=breaking3+1
    elif separado[0]=="Breaking Bad" and separado[1]=="4":
        breaking4=breaking4+1
    elif separado[0]=="Breaking Bad" and separado[1]=="5":
        breaking5=breaking5+1
    
    
        

        
    #exercicio 4- media das notas+dicionario
    if separado[0]=="The Big Bang Theory":
        somatoria=somatoria+float(separado[5])
        somatoria2=somatoria2+float(separado[6])
    elif separado[0]=="Friends":
        somatoria3=somatoria3+float(separado[5])
        somatoria4=somatoria4+float(separado[6])
    elif separado[0]=="Black Mirror":
        somatoria5=somatoria5+float(separado[5])
        somatoria6=somatoria6+float(separado[6])
    elif separado[0]=="Breaking Bad":
        somatoria7=somatoria7+float(separado[5])
        somatoria8=somatoria8+float(separado[6])
    
        
media_imdb=somatoria/(temp1+temp2+temp3+temp4+temp5+temp6+temp7+temp8+temp9+temp10+temp11+temp12)
media_netflix=somatoria2/(temp1+temp2+temp3+temp4+temp5+temp6+temp7+temp8+temp9+temp10+temp11+temp12)
media_imdb2=somatoria3/(tempo1+tempo2+tempo3+tempo4+tempo5+tempo6+tempo7+tempo8+tempo9+tempo10)
media_netflix2=somatoria4/(tempo1+tempo2+tempo3+tempo4+tempo5+tempo6+tempo7+tempo8+tempo9+tempo10)
media_final=media(media_imdb,media_netflix)
media_final2=media(media_imdb2,media_netflix2)
media_imdb3=somatoria5/(black1+black2+black3+black4+black5)
media_netflix3=somatoria6/(black1+black2+black3+black4+black5)
media_final3=media(media_imdb3,media_netflix3)
media_netflix4=somatoria7/(breaking1+breaking2+breaking3+breaking4+breaking5)
media_imdb4=somatoria8/(breaking1+breaking2+breaking3+breaking4+breaking5)
media_final4=media(media_imdb4,media_netflix4)

dicionario={"The Big Bang Theory:" : media_final,"Friends:":media_final2,"Black Mirror:":media_final3,"Breaking Bad:":media_final4}
        
print("The Big Bang Theory:",end='')
print("Temporada 1:",end='')
print("Episodios:",temp1)
print("Temporada 2:",end='')
print("Episodios:",temp2)
print("Temporada 3:",end='')
print("Episodios:",temp3)
print("Temporada 4:",end='')
print("Episodios:",temp4)
print("Temporada 5:",end='')
print("Episodios:",temp5)
print("Temporada 6:",end='')
print("Episodios:",temp6)
print("Temporada 7:",end='')
print("Episodios:",temp7)
print("Temporada 8:",end='')
print("Episodios:",temp8)
print("Temporada 9:",end='')
print("Episodios:",temp9)
print("Temporada 10:",end='')
print("Episodios:",temp10)
print("Temporada 11:",end='')
print("Episodios:",temp11)
print("Temporada 12:",end='')
print("Episodios:",temp12)

print("Friends:",end='')
print("Temporada 1:",end='')
print("Episodios:",tempo1)
print("Temporada 2:",end='')
print("Episodios:",tempo2)
print("Temporada 3:",end='')
print("Episodios:",tempo3)
print("Temporada 4:",end='')
print("Episodios:",tempo4)
print("Temporada 5:",end='')
print("Episodios:",tempo5)
print("Temporada 6:",end='')
print("Episodios:",tempo6)
print("Temporada 7:",end='')
print("Episodios:",tempo7)
print("Temporada 8:",end='')
print("Episodios:",tempo8)
print("Temporada 9:",end='')
print("Episodios:",tempo9)
print("Temporada 10:",end='')
print("Episodios:",tempo10)

print("Black Mirror:",end='')
print("Temporada 1:",end='')
print("Episodios:",black1)
print("Temporada 2:",end='')
print("Episodios:",black2)
print("Temporada 3:",end='')
print("Episodios:",black3)
print("Temporada 4:",end='')
print("Episodios:",black4)
print("Temporada 5:",end='')
print("Episodios:",black5)

print("Breaking Bad:",end='')
print("Temporada 1:",end='')
print("Episodios:",breaking1)
print("Temporada 2:",end='')
print("Episodios:",breaking2)
print("Temporada 3:",end='')
print("Episodios:",breaking3)
print("Temporada 4:",end='')
print("Episodios:",breaking4)
print("Temporada 5:",end='')
print("Episodios:",breaking5)


#exercicio5

melhores=open("melhores.csv","w")

if dicionario["The Big Bang Theory:"]>(7.5):
    melhores.write("The Big Bang Theory")
if dicionario["Friends:"]>(7.5):
    melhores.write("Friends:")
if dicionario["Black Mirror:"]>(7.5):
    melhores.write("Black Mirror")
if dicionario["Breaking Bad:"]>(7.5):
    melhores.write("Breaking Bad")


melhores.close()
    









        
    

    
    







    
    


