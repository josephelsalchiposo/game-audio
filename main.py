import random
import speech_recognition as sr
from googletrans import Translator

# ----------------------------
# Diccionario por dificultad
# ----------------------------
words_by_level = {
    "facil": ["gato", "perro", "manzana", "leche", "sol"],
    "medio": ["banano", "escuela", "amigo", "ventana", "amarillo"],
    "dificil": ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"]
}

# ----------------------------
# Variables del juego
# ----------------------------
score = 0
errors = 0
MAX_ERRORS = 3

recognizer = sr.Recognizer()
translator = Translator()

# ----------------------------
# Selección de dificultad
# ----------------------------
print("🎮 BIENVENIDO AL JUEGO DE VOZ 🎮")
print("Selecciona la dificultad:")
print("🟢 facil | 🟡 medio | 🔴 dificil")

level = input("👉 Dificultad: ").lower()

if level not in words_by_level:
    print("❌ Dificultad no válida")
    exit()

print(f"\n✅ Dificultad seleccionada: {level.upper()}")

# ----------------------------
# Loop principal del juego
# ----------------------------
while errors < MAX_ERRORS:
    word = random.choice(words_by_level[level])
    print(f"\n🗣️ Pronuncia esta palabra: 👉 **{word.upper()}**")

    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            recognized = recognizer.recognize_google(audio, language="es-ES")
            recognized = recognized.lower()

            translated = translator.translate(recognized, dest="es").text.lower()

            print(f"🔎 Dijiste: {recognized}")

            if translated == word:
                score += 10
                print("✅ ¡Correcto! +10 puntos 🎉")
            else:
                errors += 1
                print(f"❌ Incorrecto. Errores: {errors}/3")

    except:
        errors += 1
        print(f"⚠️ No se pudo reconocer la voz. Errores: {errors}/3")

# ----------------------------
# Fin del juego
# ----------------------------
print("\n💀 GAME OVER 💀")
print(f"🏆 Puntaje final: {score}")

