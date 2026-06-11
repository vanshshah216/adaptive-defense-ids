import sqlite3

filename=input("Enter the log file name: ")

conn=sqlite3.connect('alerts.db')
cursor=conn.cursor()

failed_logins=0
access_denied=0

with open(filename, 'r') as file:
    for line in file:
        if "Failed Password" in line:
            failed_logins+=1
            cursor.execute("INSERT INTO alerts(event) VALUES(?)",(line,))
        elif "Access denied" in line:
            access_denied+=1
            cursor.execute("INSERT INTO alerts(event) VALUES(?)",(line,))

conn.commit()
print("\nSecurity Alerts Summary:")
print("Failed Logins:", failed_logins)
print("Access Denied:", access_denied)

conn.close()
