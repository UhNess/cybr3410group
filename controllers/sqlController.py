from config.dbConfig import get_db_connection

def login(username, password):
    conn = get_db_connection()
    # sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"  # SQL Injection Vulnerability
    sql = "SELECT * FROM users WHERE username = ? AND password = ?"
    # user = conn.execute(sql).fetchone()
    user = conn.execute(sql, (username, password)).fetchone()
    conn.close()
    return user
    # noted out code is original code, but has the  ' OR '1'='1  for user and any password (ex: password123) for the password vulnerability
    # making a search into SQL code looking like; SELECT * FROM users WHERE username = '' OR '1'='1' AND password = 'password123'
    # the code doesnt use prepared statements or parameterized queries, which are designed to separate SQL code from data.
    # the "?" placeholder is used in the SQL query and any actual values are passed as a tuple.


def search(query):
    conn = get_db_connection()
    sql = f"SELECT * FROM users WHERE username LIKE '%{query}%'"
    rows = conn.execute(sql).fetchall()
    conn.close()
    results = [dict(row) for row in rows]  # Convert each row to a dictionary
    print(f"Results from DB: {results}")  # Debugging output
    return results


def get_profile(user_id):
    conn = get_db_connection()
    sql = f"SELECT * FROM users WHERE id = {user_id}"  # SQL Injection Vulnerability
    user = conn.execute(sql).fetchone()
    conn.close()
    return user
