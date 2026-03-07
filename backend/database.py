import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in .env file")

supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def get_db():
    return supabase
