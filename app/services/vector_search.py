from app.utils.vectorizer import vectorize_text
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://postgres@127.0.0.1:5434/guidely2"

engine=create_engine(DATABASE_URL)
SessionLocale=sessionmaker(bind=engine)

session=SessionLocale()

def find_similar_items(query:str):
    input_vector = vectorize_text(query)
    similar_items = session.execute(
    text("""
        SELECT id, name, vector 
        FROM guides
        ORDER BY vector <=> CAST(:query_vector AS vector)
        LIMIT 10
    """),
        {'query_vector': input_vector}  
        ).fetchall()
        
    return [{"id": item.id, "name": item.name} for item in similar_items]
    