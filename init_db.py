"""
Note:

1. Run to create the DB tables
2. when models change, remove the old one and create the new one

"""
from apps import db
def init_db():
    db.create_all()

if __name__ == "__main__":
    init_db()
