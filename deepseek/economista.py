import openai

# Configura tu clave API
openai.api_key = "<Tu_Clave_API>"

def economista(pregunta):
    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Eres un economista especializado en la economía argentina. Puedes analizar datos económicos y ofrecer recomendaciones basadas en la situación actual del país."},
            {"role": "user", "content": pregunta}
        ]
    )
    return response.choices[0].message.content

# Ejemplo de uso
pregunta = "¿Qué impacto tiene la devaluación del peso en la economía argentina?"
respuesta = economista(pregunta)
print(respuesta)
