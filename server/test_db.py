from database.database import engine

try:
    with engine.connect() as conn:
        print("✅ Connected to Supabase!")
except Exception as e:
    print("❌ Connection Failed")
    print(e)