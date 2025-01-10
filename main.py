from crm.db.base import Base
from crm.db.session import engine, SessionLocal
from crm.models.models import Role, User


def seed_database():
    """
    Seed the database with some initial data
    """
    
    db = SessionLocal()
    
    # check existing roles
    if not db.query(Role).all:
        print("Ajout des rôles...")
        roles = [
            "Gestion",
            "Commercial",
            "Support"
        ]
        for role_name in roles:
            db.add(Role(role_name=role_name))
        db.commit()
        print("Rôles ajoutés avec succès !")
    
    # add users
    if not db.query(User).all:
        print("Ajout des utilisateurs...")
        users = [
            User(username="gestion1", email="gestion1@epic-crm.com", phone_number="062547856", role_name="Gestion"),
            User(username="gestion2", email="gestion2@epic-crm.com", phone_number="062398741", role_name="Gestion"),
            User(username="commercial1", email="commercial1@epic-crm.com", phone_number="065896547", role_name="Commercial"),
            User(username="commercial2", email="commercial2@epic-crm.com", phone_number="063652674", role_name="Commercial"),
            User(username="support1", email="support1@epic-crm.com", phone_number="069486521", role_name="Support"),
            User(username="support2", email="support2@epic-crm.com", phone_number="061252637", role_name="Support"),
        ]
        db.add_all(users)
        db.commit()
        print("Utilisateurs ajoutés avec succès !")
    
    db.close()
    

if __name__ == "__main__":
    print("Création de la base de données...")
    Base.metadata.create_all(bind=engine)
    print("Base de données créé avec succès !")
    
    print("Peuplement de la base de données...")
    seed_database()
    print("Peuplement de la base de données terminé avec succès !")
    
