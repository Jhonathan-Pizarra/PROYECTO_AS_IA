from pysentimiento import create_analyzer

class Animo:
    def __init__(self, emoji, sentimiento):
        self.emoji = emoji
        self.sentimiento = sentimiento
    
    def __repr__(self):
        return f"Animo(emoji='{self.emoji}', sentimiento={self.sentimiento})"

def obtener_animo(texto_entrada: str, *, sensibilidad: float) -> Animo:
    analyzer = create_analyzer(task="sentiment", lang="es")
    result = analyzer.predict(texto_entrada)
    polaridad = result.probas[result.output]
    Umbral_amistoso: float = sensibilidad
    Umbral_hostil: float = -sensibilidad
    
    if result.output == "POS":
        return Animo('😄', polaridad)
    elif result.output == "NEG":
        return Animo('😞', polaridad)
    else:
        return Animo('😐', polaridad)

def ejecutar_bot():
    print('Bot: Introduce algún texto y realizaré un análisis de sentimiento sobre él.')
    while True:
        entrada_usuario: str = input('Tú: ')
        animo: Animo = obtener_animo(entrada_usuario, sensibilidad=0.3)
        print(f'Bot: {animo.emoji} ({animo.sentimiento})')

ejecutar_bot()
