import random

game = ["Piedra", "Papel", "Tijeras"]
usuario = -1
count_me = 0
count_IA = 0
round = 1
dificult = ["Facil", "Medio", "Dificil"]

def IA_balanceada_medio(usuario, game):
    prob = random.random()
    
    if prob < 0.2:
        return usuario
    elif prob < 0.6:
                # IA pierde (40% del tiempo): elige lo que el jugador gana
        if usuario == "Piedra":
            return "Tijeras"
        elif usuario == "Papel":
            return "Piedra"
        elif usuario == "Tijeras":
            return "Papel"
    else:
        # IA gana (40% del tiempo): elige lo que vence al jugador
        if usuario == "Piedra":
            return "Papel"
        elif usuario == "Papel":
            return "Tijeras"
        elif usuario == "Tijeras":
            return "Piedra"
def IA_balanceada_facil(usuario, game):
    prob = random.random()
    
    if prob < 0.2:
        return usuario
    elif prob < 0.8:
                # IA pierde (40% del tiempo): elige lo que el jugador gana
        if usuario == "Piedra":
            return "Tijeras"
        elif usuario == "Papel":
            return "Piedra"
        elif usuario == "Tijeras":
            return "Papel"
    else:
        # IA gana (40% del tiempo): elige lo que vence al jugador
        if usuario == "Piedra":
            return "Papel"
        elif usuario == "Papel":
            return "Tijeras"
        elif usuario == "Tijeras":
            return "Piedra"

def IA_balanceada_dificil(usuario, game):
    prob = random.random()
    
    if prob < 0.2:
        return usuario
    elif prob < 0.4:
                # IA pierde (40% del tiempo): elige lo que el jugador gana
        if usuario == "Piedra":
            return "Tijeras"
        elif usuario == "Papel":
            return "Piedra"
        elif usuario == "Tijeras":
            return "Papel"
    else:
        # IA gana (40% del tiempo): elige lo que vence al jugador
        if usuario == "Piedra":
            return "Papel"
        elif usuario == "Papel":
            return "Tijeras"
        elif usuario == "Tijeras":
            return "Piedra"

print("Holaa !!, Vamos a jugar a Piedra Papel y Tijeras")
print("------------------------------------------------")
nivel = -1
while nivel not in dificult:
    nivel = input(" Elige entre (Facil, Medio, Dificil) de nivel: ").capitalize()

while count_me != 3 and count_IA != 3:
    print(f"round {round}")
    usuario = input("elige : ").capitalize()
    if usuario not in game:
        print( f"Has elegido {usuario} y no es valido")
        continue
    if nivel == dificult[0]:
        IA = IA_balanceada_facil(usuario, game)
    elif nivel == dificult[1]:
        IA = IA_balanceada_medio(usuario, game)
    else:
        IA = IA_balanceada_dificil(usuario, game)
    print(f"la IA eligio {IA} y tu elegiste {usuario}")
    if usuario == game[0] and IA == game[2]:
        print("Has ganado !!")
        count_me += 1
    elif usuario == game [1] and IA == game [0]:
        print("Has ganado !!")
        count_me += 1
    elif usuario == game [2] and IA == game[1]:
        print(" Has ganado !!")
        count_me += 1
    elif usuario == IA:
        print("Habeis empatado")
    else:
        print("has perdido")
        count_IA += 1
    round += 1
    print("--------------------------------------")
    print(f"usuario = {count_me} IA = {count_IA}")    
if count_me == 3:
    print("\n🎉 ¡Felicidades! Ganaste el juego.")
else:
    print("\n💀 La IA ganó. ¡Suerte la próxima!")
