
NOTAS = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]
NOTAS1 = [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]

v1 = int(input("Desea calcular la media aritmética? (1 si 0 no): "))

if v1 == 1:
    
    media = 0
        
    for x in range(len(NOTAS)):
        media += NOTAS[x]

    media = media/len(NOTAS)

    print("La media aritmética es de "+str(media))



media1 = 0
        
for x in range(len(NOTAS)):
    media1 += NOTAS[x]

media1 = media1/len(NOTAS)



v2 = int(input("Desea calcular la mediana? (1 si 0 no): "))

if v2 ==1:
    NOTAS1.sort()

    if len(NOTAS1)%2 == 0:
        x = int(len(NOTAS1)/2)
        rra = NOTAS1[x-1]+NOTAS1[x]
        rra/= 2
        print("Mediana es "+str(rra))

    else: 
        x = int(len(NOTAS1)/2)
        print("Mediana es "+str(NOTAS1[x]))






v3 = int(input("Desea calcular la moda? (1 si 0 no): "))

if v3 ==1:
    w = 0
    q =0
    NOTAS1.sort()
    
    x11=[]
    y11=0


    for x in range(len(NOTAS1)):
        
        if x != 0 and NOTAS1[x]==NOTAS1[x-1]:
            w+=1
            
            
            if w > q:

                moda=NOTAS1[x]
                q = w
                #print("q es : "+str(q))
                y11=0
                x11.clear()

            if w == q:
                
                x11.append(moda)
                x11.append(NOTAS1[x])
                y11=1


        else:
            w=1

    
    if y11==0:
        print("La moda es "+str(moda))
    else:
        x11 = list(set(x11))
        print("Las modas son: "+str(x11))


v4 = int(input("Desea calcular la varianza? (1 si 0 no): "))

if v4 == 1:
    VARIABLE_AYUDA=0
    for x in range(len(NOTAS)):
        VARIABLE_AYUDA+= NOTAS[x]*NOTAS[x]

    
    varianza = (VARIABLE_AYUDA/len(NOTAS))-(media1*media1)

    print("La varianza es de "+str(varianza))



VARIABLE_AYUDA=0
for x in range(len(NOTAS)):
    VARIABLE_AYUDA+= NOTAS[x]*NOTAS[x]

    
varianza = (VARIABLE_AYUDA/len(NOTAS))-(media1*media1)




v5 = int(input("Desea calcular la desviacion típica? (1 si 0 no): "))
if v5 ==1:
    resu = varianza ** 0.5
    print("La desviación tipica es de "+str(resu))

resu = varianza ** 0.5    

v6 = int(input("Desea calcular el coeficiente de variación? (1 si 0 no): "))
if v6==1:
    cv = resu/media1
    print("El coeficiente de variación es de: "+str(cv))




