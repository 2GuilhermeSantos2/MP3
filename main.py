from time import sleep
from playsound import playsound


print('*' * ((50 - len("TOCADOR MP3")) // 2) + "TOCADOR MP3" + '*' * ((50 - len("TOCADOR MP3")) // 2))


while True:
    escolha = str(input("Escolha uma musica: "
                        "\n1 = Impossible"
                        "\n2 = Legends Never Die"
                        "\n3 = Enemy"
                        "\n:"))

    if int(escolha) < 1 or int(escolha) > 3:
        print('Escolha uma opção correta!!!')

    elif int(escolha) == 1:

        playsound("src/audios/impossible.mp3")

        continuar = str(input("Deja ouvir outra musica?"
                              "\n1 - Sim"
                              "\n2 - Não"
                              "\n:"))

        if int(continuar) < 1 or int(continuar) > 2:
            print('Escolha uma opção correta!!!')

        elif int(continuar) == 2:
            print('Encerrando Programa...')
            sleep(2.5)
            quit()

    elif int(escolha) == 2:

        playsound("legends.mp3")

        continuar = str(input("Deja ouvir outra musica?"
                              "\n1 - Sim"
                              "\n2 - Não"
                              "\n:"))

        if int(continuar) < 1 or int(continuar) > 2:
            print('Escolha uma opção correta!!!')

        elif int(continuar) == 2:
            print('Encerrando Programa...')
            sleep(2.5)
            quit()

    elif int(escolha) == 3:

        playsound("enemy.mp3")

        continuar = str(input("Deja ouvir outra musica?"
                              "\n1 - Sim"
                              "\n2 - Não"
                              "\n:"))

        if int(continuar) < 1 or int(continuar) > 2:
            print('Escolha uma opção correta!!!')

        elif int(continuar) == 2:
            print('Encerrando Programa...')
            sleep(2.5)
            quit()