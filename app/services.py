from models import AssetType, Building, EmployeeDepartment
from flask import current_app

class TagGenerator:
    def __init__(self, asset_type, building, employee_department):
        self.asset_type = asset_type
        self.building = building
        self.employee_department = employee_department

    def generate_tag(self):
        # Generate a unique tag based on the asset type, building, and employee department
        # For example, you could use a combination of the asset type code, building code, and employee department code
        # You could also add a random number or a timestamp to make the tag more unique
        tag = f"{self.asset_type.code}-{self.building.code}-{self.employee_department.code}"
        return tag