import os
from langchain.chat_models import init_chat_model


os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
response=model.invoke([{"role": "user", "content": "What are AI Agents?"}]) 

print(response.content)

