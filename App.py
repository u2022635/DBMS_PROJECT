from flask import Flask, render_template, request, flash, redirect, url_for
import psycopg2

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_conn():
    try:
        conn = psycopg2.connect(
            dbname="db_LibraryManagement",
            user="postgres",
            password="pgadmin4",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        flash(f"Error connecting to the database: {e}", "error")
        return None

def fetch_books_issued():
    conn = get_conn()
    if not conn:
        return []

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM book_issue")
    books_issued = cur.fetchone()[0]
    cur.close()
    conn.close()
    return books_issued

def fetch_pending_requests():
    conn = get_conn()
    if not conn:
        return []

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM pending_book_requests")
    pending_requests = cur.fetchone()[0]
    cur.close()
    conn.close()
    return pending_requests

def fetch_overdue_books():
    conn = get_conn()
    if not conn:
        return []

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM book_issue WHERE due_date < CURRENT_DATE")
    overdue_books = cur.fetchone()[0]
    cur.close()
    conn.close()
    return overdue_books

@app.route('/')
@app.route('/homepage')
def index():
    books_issued = fetch_books_issued()
    pending_requests = fetch_pending_requests()
    overdue_books = fetch_overdue_books()
    return render_template('homepage.html')

@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        price = request.form['price']
        copies = request.form['copies']

        conn = get_conn()
        if not conn:
            return redirect(url_for('addbook'))

        cur = conn.cursor()
        cur.execute("INSERT INTO book (title, author, category, price, copies) VALUES (%s, %s, %s, %s, %s)", (title, author, category, price, copies))
        conn.commit()
        cur.close()
        conn.close()

        flash('New book added successfully!', 'success')
        return redirect(url_for('addbook'))

    return render_template('addbook.html')

@app.route('/updatebook', methods=['GET', 'POST'])
def update_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        price = request.form['price']
        copies = request.form['copies']

        conn = get_conn()
        if not conn:
            flash('Error connecting to database', 'error')
            return redirect(url_for('updatebook'))

        try:
            cur = conn.cursor()
            cur.execute("UPDATE book SET title=%s, author=%s, category=%s, price=%s, copies=%s WHERE id=%s", 
                        (title, author, category, price, copies, book_id))
            conn.commit()
            cur.close()
            conn.close()

            flash('Book details updated successfully!', 'success')
            return redirect(url_for('updatebook.html'))
        except Exception as e:
            flash(f'Error updating book: {e}', 'error')
            return redirect(url_for('updatebook'))

    return render_template('updatebook.html')
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/issue')
def book_issues_and_returns():
    return render_template('issue.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_username = request.form['signup-username']
        new_password = request.form['signup-password']
        confirm_password = request.form['confirm-password']

        if new_password != confirm_password:
            error_message = 'Passwords do not match'
            return render_template('signup.html', error_message=error_message)

        # Add registration logic here
        # For example, you can store the user data in a database
        # In this example, we just display a success message
        success_message = 'Registration successful'
        return render_template('signup.html', success_message=success_message)

    return render_template('signup.html')

@app.route('/accmanagement', methods=['GET', 'POST'])
def account_management():
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        # Add account update logic here
        # For example, you can update the user data in a database
        # In this example, we just display a success message
        success_message = 'Account updated successfully'
        return render_template('accmanagement.html', success_message=success_message)

    return render_template('accmanagement.html')
if __name__ == '__main__':
    app.run(debug=True)