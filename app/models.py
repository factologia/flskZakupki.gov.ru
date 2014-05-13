from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Zakup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.String(120), index = True, unique = True)
    author = db.Column(db.String(120), index = True)
    published = db.Column(db.String(120), index = True)
    title = db.Column(db.String(120), index = True)
    summary = db.Column(db.String(1024), index = True)
    def __repr__(self):
        return '<Zakupka %r>' % (self.title)