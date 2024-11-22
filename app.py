from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, template_folder='templates')

# Database setup
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",      # Your MySQL username
        password="mysql",  # Your MySQL password
        database="library"   # Database name
    )
    return conn

# Home Page with menu
@app.route('/')
def index():
    return render_template('index.html')

# Add a Book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        code = request.form['code']
        total = request.form['total']
        subject = request.form['subject']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO book (Name, Code, TotalBooks, Subject)
            VALUES (%s, %s, %s, %s)
        """, (name, code, total, subject))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/display_books')
def display_books():
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    books = cur.fetchall() 
    conn.close()
    print("Books Data:", books)
    return render_template('display_book.html', books=books)

# Issue Book
@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        name = request.form['name']
        reg_no = request.form['reg_no']
        book_code = request.form['book_code']
        date = request.form['date']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO issue (Name, RegNo, BookCode, Date)
            VALUES (%s, %s, %s, %s)
        """, (name, reg_no, book_code, date))
        conn.commit()
        
        # Update the book total
        cur.execute("""
            UPDATE book SET TotalBooks = TotalBooks - 1 WHERE Code = %s
        """, (book_code,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('issue_book.html')

# Submit Book
@app.route('/submit_book', methods=['GET', 'POST'])
def submit_book():
    if request.method == 'POST':
        name = request.form['name']
        reg_no = request.form['reg_no']
        book_code = request.form['book_code']
        date = request.form['date']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO submit (Name, RegNo, BookCode, Date)
            VALUES (%s, %s, %s, %s)
        """, (name, reg_no, book_code, date))
        conn.commit()
        
        # Update the book total
        cur.execute("""
            UPDATE book SET TotalBooks = TotalBooks + 1 WHERE Code = %s
        """, (book_code,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('submit_book.html')
# Delete Book
@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'POST':
        book_code = request.form['code']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM book WHERE Code = %s
        """, (book_code,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete_book.html')
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
