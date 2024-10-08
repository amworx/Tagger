import models
db = models.db
AssetType = models.AssetType
Building = models.Building
EmployeeDepartment = models.EmployeeDepartment


def initialize():
    # Create the tables
    db.create_all()

    # Insert data into the tables
    asset_types = [
        AssetType(title='Access Point', code='APN'),
        AssetType(title='CCTV IPC', code='IPC'),
        AssetType(title='Firewall', code='FWL'),
        AssetType(title='GSM Booster', code='GSM'),
        AssetType(title='Laptop', code='LTP'),
        AssetType(title='Monitor', code='MON'),
        AssetType(title='NVR', code='NVR'),
        AssetType(title='Phone', code='PHN'),
        AssetType(title='POS', code='POS'),
        AssetType(title='Printer', code='PRT'),
        AssetType(title='Projector', code='PRO'),
        AssetType(title='Router', code='RTR'),
        AssetType(title='Switch', code='SWT'),
        AssetType(title='Tablet', code='TAB'),
        AssetType(title='Wireless Dish', code='WDS'),
    ]

    buildings = [
        Building(title='Guest House', code='GHS'),
        Building(title='Programs', code='PRG'),
        Building(title='Quality', code='QLT'),
        Building(title='Systems', code='SYS'),
        Building(title='Warehouse Back', code='WHB'),
        Building(title='Warehouse Front', code='WHF'),
        Building(title='Warehouse Middle', code='WHM'),
    ]

    employee_departments = [
        EmployeeDepartment(title='Access', code='ACC'),
        EmployeeDepartment(title='Accountability', code='ACT'),
        EmployeeDepartment(title='Area', code='ARE'),
        EmployeeDepartment(title='Bakeries', code='BAK'),
        EmployeeDepartment(title='Cargo', code='CRG'),
        EmployeeDepartment(title='CFM', code='CFM'),
        EmployeeDepartment(title='Communication', code='COM'),
        EmployeeDepartment(title='Compliance', code='CPL'),
        EmployeeDepartment(title='CVA', code='CVA'),
        EmployeeDepartment(title='Distribution', code='DIS'),
        EmployeeDepartment(title='Emergency', code='EMR'),
        EmployeeDepartment(title='Finance', code='FIN'),
        EmployeeDepartment(title='Fleet', code='FLT'),
        EmployeeDepartment(title='Food Security CVA & Basic Needs', code='FSB'),
        EmployeeDepartment(title='HR', code='HUM'),
        EmployeeDepartment(title='Hygiene', code='HYG'),
        EmployeeDepartment(title='Investigation', code='INV'),
        EmployeeDepartment(title='IT', code='ITC'),
        EmployeeDepartment(title='Logistic', code='LOG'),
        EmployeeDepartment(title='Markets', code='MKT'),
        EmployeeDepartment(title='Media', code='MED'),
        EmployeeDepartment(title='MEL', code='MEL'),
        EmployeeDepartment(title='MIS', code='MIS'),
        EmployeeDepartment(title='Nutrition', code='NUT'),
        EmployeeDepartment(title='Outreach', code='OUT'),
        EmployeeDepartment(title='Procurement', code='PRC'),
        EmployeeDepartment(title='Protection & Safeguarding', code='PRT'),
        EmployeeDepartment(title='Selection', code='SEL'),
        EmployeeDepartment(title='Shelter', code='SHL'),
        EmployeeDepartment(title='SME', code='SME'),
        EmployeeDepartment(title='Verification', code='VER'),
        EmployeeDepartment(title='WASH', code='WSH'),
        EmployeeDepartment(title='Spare', code='SPR'),
    ]

    db.session.add_all(asset_types)
    db.session.add_all(buildings)
    db.session.add_all(employee_departments)
    db.session.commit()

if __name__ == "__main__":
    initialize()