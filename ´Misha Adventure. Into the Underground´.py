print("Bienvenido a ´Misha Adventure: Into the Underground´")
print("No nos hacemos responsables de este juego ni de los elementos referenciados.")
print("Ah, y esta historia fue escrita como una broma... así que no te lo tomes demasiado en serio.")
a=input("Antes de que empieces, dime... ¿eres chico o chica?: ")
print("SIKE! No, espera, ¿quién necesita respuestas serias?")
print("La verdad es que ni siquiera le pagamos bien al programador que hizo esto...") 
print("Así que no te sorprendas si las elecciones son más básicas que una pizza con solo queso.")
print("Por cierto, eres una jirafa. Sí, una jirafa. Y no, no voy a explicar porque decidimos eso.")
print("En fin, siendo una jirafa, supongo que eres lo suficientemente mayor para entender lo que viene a continuación.")
print("Bueno, ya me estoy quedando sin papel, así que... ¡arranca la historia!")
print("")
print("Hace mucho, mucho, pero MUCHO tiempo atrás... Existieron dos dioses: Bien y Caos.")
print("Ok, ya sé, esto suena a cliché... pero aguanta, que se pone interesante.")
print("Era una guerra eterna, sin fin, una lucha constante de poder... hasta que llegaron a un punto:")
print("En la batalla 1236.647cta (sí, CTA, porque claramente eso es una unidad de tiempo válida)")
print("...ambos empezaron a cuestionarse algo.")
print("Y luego en la 176.346´247.285cta, la situación fue aún más surrealista...")
print("..empezaron a preguntarse... ¿por qué seguimos luchando?")
print("Eso ya era raro, ¿no?")
print("Pero justo cuando pensaban que se quedarían atrapados en una rutina de ‘nada más que guerra’, sucedió lo impensable...")
print("El Dios del Bien, en pleno combate, miró a su enemigo, el Dios del Caos, y dijo...")
print("")
b=input("Presiona Enter para saber qué dijo el Dios del Bien..." )
print("Él dijo: “¿Por qué seguimos peleando, Caos? ¿No podemos... hacer algo diferente? Como... no sé, jugar ajedrez o algo?”.")
print("Caos, totalmente confundido, se detuvo en medio de su furia destructiva. Por un segundo, ambos se quedaron en silencio.")
print("Entonces, Caos, con una expresión seria (para lo que él podía, considerando su naturaleza), respondió:")
print("“No sé... nunca lo había pensado. Pero... ¿ajedrez, dices? ¿Y qué tal algo más épico, como lanzar meteoritos?”")
print("El Dios del Bien lo pensó por un segundo... luego se encogió de hombros.")
print("“Nah, eso ya lo hemos hecho mil veces. Mejor cambiamos el guion. ¿Qué tal… un concurso de hacer un imperio de nuestras creaciones?”")
print("")
print("Y así comenzó la batalla más ridícula de la historia de los dioses... una guerra sin fin... pero de .")
print("El destino del universo dependía de qué tan bien podían mover sus tropas. ¿Y tú, qué papel juegas en todo esto?")
print("¡Acompáñanos en esta aventura, Misha (nunca te dimos la opcion de nombre jaja)! Pero cuidado... ¡el estar preparado lo es todo!")
print("")
import random
print("=== Misha Adventure: Into the Underground ===")
print("Bienvenido, valiente guerrera del destino.\n")
x=1
# Datos del jugador
player = {
    "nombre": input("¿Cómo te llamas, noble jirafa?: "),
    "vida": 100,
    "ataque": 15,
    "defensa": 8,
    "nivel": 1,
    "experiencia": 0
}
# Datos del enemigo
enemy = {
    "nombre": "Slime del Caos",
    "vida": 50,
    "ataque": 8,
    "defensa": 2,
}
enemy = {
    "nombre": "HogGoblin Sangriento",
    "vida": 45,
    "ataque": 12,
    "defensa": 7,
}
if x>=8:
    enemy = {
        "nombre": "Orco Montañoso",
        "vida": 65,
        "ataque": 15,
        "defensa": 12,
}
if x>=12:
    enemy = {
        "nombre": "ArchiDemonio ",
        "vida": 70,
        "ataque": 20,
        "defensa": 20,
}
if x>=15:
    enemy = {
        "nombre": "Sabueso Infernal",
        "vida": 67,
        "ataque": 18,
        "defensa": 19,
}
if x>=25:
    enemy = {
        "nombre": "Beelzebul, Parca ´El que trae la muerte´",
        "vida": 80,
        "ataque": 31,
        "defensa": 27,
}
print(f"\nTe enfrentas a un {enemy['nombre']}!")
print("¡Prepárate para la batalla!\n")
Op="Y"
while Op=="Y":
    while player["vida"] > 0 and enemy["vida"] > 0:
        action = input("¿Qué haces? (a) Atacar  (h) Curarte (d) defender: ").lower()
        if action == "a":
            daño = max(0, player["ataque"] - enemy["defensa"])
            enemy["vida"] -= daño
            print(f"Atacas al {enemy['nombre']} y le haces {daño} de daño. Vida restante del enemigo: {enemy['vida']}")
        elif action == "h":
            cura = random.randint(10, 20)
            player["vida"] += cura
            print(f"Te curas {cura} puntos de vida. Vida actual: {player['vida']}")
        elif action == "d":
            defender = random.randint(10, 30)
            player["defensa"] += defender
            print(f"Te defiendes de los ataques enemigos")
        else:
            print("Te confundiste... ¡y pierdes el turno!")
        if enemy["vida"] > 0:
            daño_enemigo = max(0, enemy["ataque"] - player["defensa"])
            player["vida"] -= daño_enemigo
            print(f"El {enemy['nombre']} te ataca y te hace {daño_enemigo} de daño. Tu vida: {player['vida']}\n")
    if player["vida"] > 0:
        print("¡Has vencido al enemigo! 🏆")
        x+=1
        player["experiencia"] += 20
        if player["experiencia"] >= 40:
            player["nivel"] += 1
            player["ataque"] += 5
            player["defensa"] += 3
            player["vida"] = 100
            print(f"¡Has subido al nivel {player['nivel']}! Tus estadísticas mejoran.")
    else:
        print("Has sido derrotado... 💀")
        print("Tu record hasta ahora es: ",x)
        if x>Rx:
            print("Felicidades, superaste tu anterior record (",Rx,")")
Op=input("Deseas volver a empezar?(Y/N)")
