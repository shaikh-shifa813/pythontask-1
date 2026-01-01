import sqlite3
def update_user(user_id, name=None, email=None):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # check user exists or not
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        conn.close()
        print(" User not found")
        return

    if name and email:
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (name, email, user_id)
        )
    elif name:
        cursor.execute(
            "UPDATE users SET name = ? WHERE id = ?",
            (name, user_id)
        )
    elif email:
        cursor.execute(
            "UPDATE users SET email = ? WHERE id = ?",
            (email, user_id)
        )
    else:
        print(" Nothing to update")
        conn.close()
        return

    conn.commit()
    conn.close()
    print(" User updated successfully")

update_user(1, name="Ruhin Khan")
update_user(2, email="shifa_new@gmail.com")


