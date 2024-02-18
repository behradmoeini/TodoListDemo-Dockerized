from flask import Flask, request, render_template_string
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'))
    return conn

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT message FROM greetings;')
    greetings_list = cur.fetchall()
    cur.close()
    conn.close()
    greetings_html = ''.join([f"<li>{greeting[0]}</li>" for greeting in greetings_list])
    return render_template_string("""
        <h1>Task list</h1>
        <ul>
            {{ greetings_html | safe }}
        </ul>
        <h2>Add a New Task</h2>
        <form action="/add" method="post">
            <input type="text" name="message" required>
            <input type="submit" value="Add Greeting">
        </form>
    """, greetings_html=greetings_html)

@app.route('/add', methods=['POST'])
def add_greeting():
    message = request.form['message']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO greetings (message) VALUES (%s);', (message,))
    conn.commit()
    cur.close()
    conn.close()
    return 'Task added successfully! <a href="/">Go back to the list.</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
