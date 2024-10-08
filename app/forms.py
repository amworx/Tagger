from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired

class AssetForm(Form):
    asset_type = SelectField('Asset Type', choices=[(at.id, at.title) for at in AssetType.query.all()])
    building = SelectField('Building', choices=[(b.id, b.title) for b in Building.query.all()])
    employee_department = SelectField('Employee Department', choices=[(ed.id, ed.title) for ed in EmployeeDepartment.query.all()])