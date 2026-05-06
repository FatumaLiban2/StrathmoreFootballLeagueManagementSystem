import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_db():
    """Initialize the database by executing the schema.sql file."""
    try:
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            print("✗ DATABASE_URL not set. Skipping database initialization.")
            return
        
        # Connect directly to the database
        db = psycopg2.connect(database_url)
        cur = db.cursor()
        
        # Read and execute the schema
        with open('schema.sql', 'r') as f:
            schema = f.read()
            cur.execute(schema)
        
        db.commit()
        cur.close()
        db.close()
        print("✓ Database schema created successfully!")
        
    except Exception as e:
        print(f"⚠ Database initialization: {str(e)}")
        # Don't raise - let app continue even if init fails

if __name__ == '__main__':
    init_db()
