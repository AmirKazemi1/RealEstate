import csv
import sqlite3


class db:
    def sql(sql, data):
        with sqlite3.connect('logins.db') as database:
            cursor = database.cursor()
            cursor.execute(sql, data)
            return cursor.fetchall()

    def getuserid(username, password):
        auth = db.sql("SELECT `userId` FROM `logins` WHERE `username` = ? AND `passwd` = ?", (username, password))
        if len(auth) == 0:
            return -1
        else:
            return auth[0][0]

    def register(username, password):
        db.sql("INSERT INTO `logins`(`username`,`passwd`) VALUES (?,?)", (username, password))
        return

    def getinfo(userid):
        return db.sql("SELECT * FROM `logins` WHERE `userId` = ?", (userid,))

    def newad(room_count, age, area, owner, username):
        with open('ads.csv', 'a+', newline='') as f:
            w = csv.writer(f)
            w.writerow([str(room_count), str(age), str(area), owner, str(username)])

    def delete(username):
        db.sql("DELETE FROM `logins` where `username`=?", (username))
