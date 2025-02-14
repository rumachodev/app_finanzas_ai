import openai

# Configura tu clave API
openai.api_key = "<Tu_Clave_API>"

def contador(pregunta):
    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Eres un contador que trabaja en Argentina. Puedes ayudar a los usuarios a organizar sus finanzas, preparar declaraciones de impuestos y ofrecer consejos sobre la gestión contable."},
            {"role": "user", "content": pregunta}
        ]
    )
    return response.choices[0].message.content

# Ejemplo de uso
pregunta = "¿Cuáles son los deducibles fiscales más comunes en Argentina?"
respuesta = contador(pregunta)
print(respuesta)
