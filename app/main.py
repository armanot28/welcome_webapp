from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Configuración de la conexión a la base de datos PostgreSQL
DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'mydatabase'
DB_USER = 'arman'
DB_PASSWORD = 'arman_rq'

def get_data_from_database():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    # Obtener datos de la base de datos
    data = get_data_from_database()
    return render_template('index.html', data=data)

@app.route('/api')
def api():
    # Obtener datos de la base de datos
    data = get_data_from_database()
    return render_template('api.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
