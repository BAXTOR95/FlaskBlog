import os
import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash
from sqlalchemy import exists


@click.command("create-admin")
@click.argument("email")
@click.argument("password")
@click.argument("name")
@with_appcontext
def create_admin(email, password, name):
    from main import db, User  # Import locally to avoid circular import

    hashed_password = generate_password_hash(
        password, method='pbkdf2:sha256', salt_length=8
    )
    admin_user = User(email=email, name=name, password=hashed_password, is_admin=True)
    db.session.add(admin_user)
    db.session.commit()
    click.echo(f"Admin {name} created successfully.")


def create_admin_if_not_exists():
    from main import db, User  # Import locally to avoid circular import

    # Ensure environment variables are set
    admin_email = os.getenv('ADMIN_EMAIL')
    admin_password = os.getenv('ADMIN_PASSWORD')
    admin_name = os.getenv('ADMIN_NAME')

    # Check if the admin already exists
    admin_exists = db.session.query(exists().where(User.email == admin_email)).scalar()

    if not admin_exists and all([admin_email, admin_password, admin_name]):
        hashed_password = generate_password_hash(
            admin_password, method='pbkdf2:sha256', salt_length=8
        )
        admin_user = User(
            email=admin_email, name=admin_name, password=hashed_password, is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print(f"Admin user {admin_name} created.")
    elif admin_exists:
        print("Admin user already exists.")
    else:
        print("Admin environment variables are not set correctly.")


@click.command("init-db")
@with_appcontext
def init_db():
    from main import db, Base  # Import locally to avoid circular import

    Base.metadata.create_all(db.engine)
    click.echo('Database initialized!')
