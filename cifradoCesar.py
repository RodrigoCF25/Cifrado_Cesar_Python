alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def cifrado_Cesar(texto,numero_de_desplazamientos):

    texto_cifrado = []
    for caracter in texto_a_cifrar:
        if caracter.isalpha():
            indice_letra = alfabeto.index(caracter.upper())
            indice_nueva_letra = indice_letra + numero_de_desplazamientos
            if indice_nueva_letra >= len(alfabeto):
                indice_nueva_letra -= (len(alfabeto) -1)

            texto_cifrado.append(alfabeto[indice_nueva_letra].lower() if caracter.islower() else alfabeto[indice_nueva_letra])

        else:
            texto_cifrado.append(caracter)


    return "".join(texto_cifrado)

    





texto_a_cifrar = "Lorem ipsum dolor sit amet. Ut culpa laboriosam ab dignissimos voluptatem et internos rerum sed dolorem autem"

print(cifrado_Cesar(texto_a_cifrar,3))

#Ñruho lsvxo grñru vlw dohw. Xw fxñsd ñderulrvdo de gljplvvlorv yrñxswdwho hw lpwhuprv uhuxo vhg grñruho dxwho