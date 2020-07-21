import unittest
from database import db
import csv
from UI import User


class TestDb(unittest.TestCase):

    def test_newad(self):
        a = ['1', '2', '30m', 'ali','mohammad']
        db.newad(a[0], a[1], a[2], a[3],a[4])

        with open('ads.csv', 'r') as f:
            r = csv.reader(f)
            r = list(r)
        self.assertEqual(r[len(r) - 1], a)

    def test_getinfo(self):
        u = db.getinfo(1)
        self.assertEqual(u, [(1, 'joe', '123456', 0)])

    def test_userid(self):
        uid = db.getuserid('joe', '123456')
        self.assertEqual(uid, 1)
        uid = db.getuserid('sdfsdf', 'sywt')
        self.assertEqual(uid, -1)

    def test_delete(self):
        db.delete('1')
        uid = db.getuserid('1', '1')
        self.assertEqual(uid, -1)


class TestLogin(unittest.TestCase):
    def testuser(self):
        u = User(-1)
        self.assertEqual(u.username, None)
        self.assertEqual(u.user_id, None)

    def testregister(self):
        uid = db.getuserid('username', 'pass')
        u = db.getinfo(uid)
        self.assertEqual('username', u[0][1])
