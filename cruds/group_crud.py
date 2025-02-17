from conf.db import session
from conf.models import Group

def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"Group '{name}' created with ID {group.id}")

def list_groups():
    groups = session.query(Group).all()
    for group in groups:
        print(f"ID: {group.id}, Name: {group.name}")

def update_group(group_id, name):
    group = session.query(Group).filter_by(id=group_id).first()
    if group:
        group.name = name
        session.commit()
        print(f"Group ID {group_id} updated to '{name}'")
    else:
        print("Group not found.")

def remove_group(group_id):
    group = session.query(Group).filter_by(id=group_id).first()
    if group:
        session.delete(group)
        session.commit()
        print(f"Group ID {group_id} removed.")
    else:
        print("Group not found.")