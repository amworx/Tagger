from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AssetType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'AssetType({self.title}, {self.code})'

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'Building({self.title}, {self.code})'

class EmployeeDepartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'EmployeeDepartment({self.title}, {self.code})'