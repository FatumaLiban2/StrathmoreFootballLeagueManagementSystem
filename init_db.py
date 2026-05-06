import psycopg2
from db import get_db
from config import Config

def init_db():
    """Initialize the database by executing the schema.sql file."""
    try:
        db = get_db()
        cur = db.cursor()
        
        # Read and execute the schema
        with open('schema.sql', 'r') as f:
            schema = f.read()
            cur.execute(schema)
        
        db.commit()
        cur.close()
        print("✓ Database schema created successfully!")
        
    except Exception as e:
        print(f"✗ Error initializing database: {str(e)}")
        raise

if __name__ == '__main__':
    init_db()
