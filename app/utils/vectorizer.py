from dotenv import load_dotenv
import openai
import os


load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")


def vectorize_text(text:str)->list[float]:
    response=openai.embeddings.create(
         model="text-embedding-3-small",
         input=text
    )
    return response.data[0].embedding


