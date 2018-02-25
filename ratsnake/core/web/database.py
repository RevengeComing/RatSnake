from ratsnake.ext import db

def create_table(table_name):
    if not db.Model.metadata.tables[table_name].exists(db.get_engine()):
        db.Model.metadata.tables[table_name].create(db.get_engine())

def create_all():
    create_table('rs_permissions')
    create_table('rs_groups')
    create_table('rs_groups_permissions')
    create_table('rs_users')
    create_table('rs_options')