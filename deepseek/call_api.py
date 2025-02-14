from openai import OpenAI

client = OpenAI(api_key="<Tu_Clave_API>", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "¡Hola!"}
    ],
    stream=False
)

print(response.choices[0].message.content)
