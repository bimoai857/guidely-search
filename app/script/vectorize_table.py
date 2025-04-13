import os
import openai
from dotenv import load_dotenv
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.vectorizer import vectorize_text


load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

db_name=os.getenv("DB_NAME");
username=os.getenv("DB_USERNAME");
password=os.getenv("DB_PASSWORD");
port=os.getenv("DB_PORT");

DATABASE_URL=f"postgresql://{username}:{password}@127.0.0.1:{port}/{db_name}"

engine=create_engine(DATABASE_URL)
SessionLocale=sessionmaker(bind=engine)

session=SessionLocale()

guides=session.execute(text('SELECT id,name from guides')).fetchall()

    
for guide in guides:
    guide_id, text_value = guide
    if text_value:
        embedding = vectorize_text(text_value)

        if embedding:
            session.execute(
                text("UPDATE guides SET vector = :vector WHERE id = :id"),
                {"vector": embedding, "id": guide_id}
            )

session.commit()
session.close()
print("Vectors updated successfully!")