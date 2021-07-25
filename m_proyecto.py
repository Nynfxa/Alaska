#mudulos
from random import choice

#colores
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado
G = "\033[32m"    # Green
BB = "\033[34;1m" # Blue light

#chistes
c_1 = G + "-Que bonito perro, ¿Como se llama?\n-Wi-fi\n-¿Wi-fi? ¿Por que?\n-Porque se lo robe a mi vecino. ¡Jaja!"
c_2 = G + "-Mama, ¿que haces en frente de la computadora con los ojos cerrados?\n-Nada, hijo, es que Windows me dijo que cerrara las pestañas."
c_3 = G + "-¿Asi que eres informatico?\n-¿Que se siente que todos te pregunten si sabes hackear facebook?"
c_4 = G + "-911 ¡Tengo un herido!\n-¡Vamos para alla! ¿Cual es su estado?\n-Hey There! I Am Using WhatsApp\n-¡No! Del herido\n-Ah, Mejor solo que mal acompañado\n-¡No! ¿Como esta?\n-Bien ¿Y usted?\n-¡No! ¿Como esta el herido?\n-Pues herido, por eso le hablo"
c_5 = G + "-Tu hablas ingles?\n-Obvio\n-¿Como se dice pan?\n-Bread\n-¿Como se dice que?\n-What\n-¿Y panqueque?\n-Breadwhatwhat"

#frases_motivadoras
f_1 = C + "Si crees que puedes o crees que no puedes tienes razon...\nHenry Ford"
f_2 = C + "Preguntate si lo que estas haciendo hoy te acerca al lugar en el que quieres estar mañana...\nWalt Disney"
f_3 = C + "Hay una fuerza motriz mas poderosa que el vapor, la electricidad y la energia atomica: la voluntad...\nAlbert Einstein"
f_4 = C + "Siempre se puede cuando se quiere...\nJose Luis Sampedro"
f_5 = C + "No te amargues con tu propio fracaso ni se lo cargues a otro. Aceptate ahora o seguiras justificandote como un niño.\n Recuerda que cualquier momento es bueno para comenzar y que ninguno es tan terrible para claudicar...\nPablo Neruda"
f_6 = C + "Nuestra gloria mas grande no consiste en no haberse caido nunca, sino en haberse levantado despues de cada caida...\nConfucio"
f_7 = C + "Nunca se ha logrado nada sin entusiasmo...\nEmerson"
f_8 = C + "Siempre se puede ser mejor...\nTiger Woods"
f_9 = C + "Confia en ti mismo sin importar lo que los demas piensen...\nArnold Schwarzenegger"
f_10 = C + "Siempre parece imposible hasta que se hace...\nNelson Mandela"
f_11 = C + "No dejes que lo que no puedes hacer interfiera con lo que puedes hacer...\nJohn R. Wooden"
f_12 = C + "La mejor manera de predecir el futuro es crearlo...\nAbraham Lincoln"
f_13 = C + "El genio se hace con un 1% de talento, y un 99% de trabajo...\nAlbert Einstein"
f_14 = C + "Continua a pesar de que todos esperen que abandones.\n No dejes que se oxide el hierro que hay en ti...\nTeresa de Calcuta"
f_15 = C + "Importa mucho mas lo que tu piensas de ti mismo que lo que otros piensan de ti...\nSeneca"

#preguntas_de_cultura_general
p_1 = M + "¿Cuál es el río más largo del mundo?"
p_2 = M + "¿Cuál es el país con más habitantes del mundo?"
p_3 = M + "¿Cuál es el edificio más alto del mundo?"
p_4 = M + "¿Cuál es el país con menos habitantes del mundo?"
p_5 = M + "¿Cuál es la película con más Óscars de la historia del cine?"
p_6 = M + "¿En qué año cayó el muro de Berlín?"
p_7 = M + "¿Cuántos años duró la Primera Guerra Mundial?"
p_8 = M + "¿Cuántos años duró la Segunda Guerra Mundial?"
p_9 = M + "¿Cuál es el océano más grande del mundo?"
p_10 = M + "¿Cuáles son las siete maravillas del mundo moderno?"
p_11 = M + "¿Cuáles son las siete maravillas del mundo antiguo?"
p_12 = M + "¿Cuándo llegó Cristóbal Colón a América?"
p_13 = M + "¿Cuál es el nombre de especie de los seres humanos?"
p_14 = M + "¿Cuál es el animal más grande de la Tierra?"
p_15 = M + "¿Cuántos huesos tiene el cuerpo humano?"

#respuestas_a_las_preguntas
def p():
    preguntas_l = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15]
    p = choice(preguntas_l)

    if p == preguntas_l[0]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) El Amazonas    2) El Nilo
    3) El Volga
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[1]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) China
    2) India
    3) Rusia
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[2]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) El Burj Khalifa, Ubicado en Dubai
    2) Catedral de san Basilio, Ubicada en Moscu
    3) Torre de Pisa, Ubicada en Toscana
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[3]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) La ciudad del Vaticano
    2) San Marino
    3) Islas Marshall
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[4]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) Titanic, Ben-Hur y el señor de los anillos
    2) Lo que el viento se llevo
    3) El ultimo emperador
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[5]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) En 1989
    2) En 1939
    3) En 1945
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[6]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) De 1914 a 1918
    2) De 1914 a 1916
    3) De 1915 a 1919
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[7]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) De 1939 a 1945
    2) De 1939 a 1940
    3) De 1940 a 1950
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[8]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) El oceano Pacifico
    2) El oceano Indico
    3) El oceano Atlantico
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[9]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) Chichén Itzá,\n Coliseo de Roma,\n El Cristo Redentor,\n La Gran Muralla China,\n Petra,\n Taj Mahal y\n Machu Picchu.
    2) La Gran Piramide de Giza,\nColiseo de Roma,\nColoso de Rodas,\nMachu Picchu,\nEstatua de Zeus,\nPetra,\nFaro de Alejandria
    3) Machu Picchu,\nEstatua de Zeus,\nTemplo de Artemisia,\nEl Cristo redentor,\nPetra,\nChichen Itza
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[10]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) La Gran Pirámide de Giza,\n Estatua de Zeus,\n Coloso de Rodas,\n Templo de Artemisa,\n Faro de Alejandría,\n el Mausoleo de Halicarnaso y\n los Jardines Colgantes de Babilonia.
    2) Machu Picchu,\nPetra,\nEstatua de Zeus,\nColiseo de Roma,\nColoso de Rodas,\n,Templo de Artemisa,\nChichen Itza
    3) Chichen Itza,\nColiseo de Roma,\nEl Criste Redentor,\nEstatua de Zeus,\nColoso de Rodas,\nTemplo de Artemisa,\nPetra
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[11]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) El 12 de octubre de 1492
    2) El 12 de agosto de 1492
    3) El 12 de septiembre de 1492
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[12]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) Homo sapiens sapiens
    2) Homo erectus
    3) Homo neandertal
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[13]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) La ballena azul
    2) Anaconda
    3) Elefante
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")
    elif p == preguntas_l[14]:
        print(p)
        print(BB + "Elige la opcion correcta:")
        print(BB + '''
    1) 206 huesos en total
    2) 210 huesos en total
    3) 280 huesos en total
    ''')
        r = int(input(">"))
        if r == 1:
            print(BB + "Wow, respuesta correcta. ¡Felicidades!")
        elif r == 2:
            print(BB + "Respuesta incorrecta")
        elif r == 3:
            print(BB + "Respuesta incorrecta")

#frases_r
def frases():
    frases_l = [f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11, f_12, f_13, f_14, f_15]
    frases = choice(frases_l)
    print(frases)

#chistes_r
def chistes():
    chistes_l = [c_1, c_2, c_3, c_4, c_5]
    chistes = choice(chistes_l)
    print(chistes)

#menu
def menu():
    while True:
        print('''Elige una opcion:
1) Chistes
2) Frases
3) Preguntas de cultura general
4) Salir
''')
        opcion = input('> ')
        if opcion == "1":
            chistes()
        elif opcion == "2":
            frases()
        elif opcion == "3":
            p()
        elif opcion == "4":
            exit()
        else:
            print("Ingresa una opcion valida")
menu()

