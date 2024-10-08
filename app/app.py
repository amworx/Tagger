from flask import Flask, render_template, request
from forms import AssetForm
from models import AssetType, Building, EmployeeDepartment
from services import TagGenerator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AssetForm()
    if form.validate_on_submit():
        asset_type = AssetType.query.get(form.asset_type.data)
        building = Building.query.get(form.building.data)
        employee_department = EmployeeDepartment.query.get(form.employee_department.data)
        tag_generator = TagGenerator(asset_type, building, employee_department)
        generated_tag = tag_generator.generate_tag()
        return render_template('generate_tag.html', generated_tag=generated_tag)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)