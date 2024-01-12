import psycopg2

def test_postgresql_connection():
    try:
        # Modifier les informations de connexion selon votre configuration
        connection = psycopg2.connect(
            user="admin",
            password="admin",
            host="localhost",
            port="5454", 
            database="sentiment_analysis"
        )
        print("Connected to the database.")
        connection.close()
    except psycopg2.Error as e:
        print(f"Unable to connect to the database. Error: {e}")

# Appeler la fonction de test
test_postgresql_connection()