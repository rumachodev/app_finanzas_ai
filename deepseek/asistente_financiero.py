import openai

# Configura tu clave API
openai.api_key = "<Tu_Clave_API>"

def asistente_financiero(pregunta):
    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Eres un asistente financiero que vive en Argentina. Tienes acceso a datos económicos locales y puedes ayudar a los usuarios a gestionar sus finanzas personales."},
            {"role": "user", "content": pregunta}
        ]
    )
    return response.choices[0].message.content

# Ejemplo de uso
pregunta = "¿Cuáles son las mejores estrategias para ahorrar en un contexto de alta inflación en Argentina?"
respuesta = asistente_financiero(pregunta)
print(respuesta)
