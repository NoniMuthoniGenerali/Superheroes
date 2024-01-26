

from app import create_app, db
from models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")

    heroes_data = [
        {'name': 'Mama', 'super_name': 'Milka'},
        {'name': 'Milka', 'super_name': 'Bonye'},
        {'name': 'Bonye', 'super_name': 'Waru'},
        {'name': 'Waru', 'super_name': 'Chipsi'},
        {'name': 'Sisi', 'super_name': 'Nani'},

    ]

    for hero_info in heroes_data:
        hero = Hero(**hero_info)
        db.session.add(hero)

    db.session.commit()
    print("Heroes data added successfully.")

    powers_data = [
        {'name': 'Flight', 'description': 'Ability to fly'},
        {'name': 'Strength', 'description': 'Superhuman strength'},
        {'name': 'Strength', 'description': 'Superhuman strength'},
        {'name': 'Strength', 'description': 'Superhuman strength'},
        {'name': 'Strength', 'description': 'Superhuman strength'},
        {'name': 'Strength', 'description': 'Superhuman strength'},
    ]

    for power_info in powers_data:
        power = Power(**power_info)
        db.session.add(power)

    db.session.commit()
    print("Powers data added successfully.")

    hero_powers_data = [
        {'hero_id': 1, 'power_id': 1, 'strength': 'Average'},
        {'hero_id': 2, 'power_id': 2, 'strength': 'Weak'},
        {'hero_id': 3, 'power_id': 2, 'strength': 'Average'},
        {'hero_id': 4, 'power_id': 1, 'strength': 'Strong'},
        {'hero_id': 5, 'power_id': 2, 'strength': 'Average'},
        {'hero_id': 6, 'power_id': 1, 'strength': 'Strong'},
    ]

    for hero_power_info in hero_powers_data:
        hero_power = HeroPower(**hero_power_info)
        db.session.add(hero_power)

    db.session.commit()
    print("Hero powers data added successfully.")

    print("Seed data added successfully.")