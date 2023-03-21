from app import app
from models import Guest, Episode, Appearance, db
from faker import Faker

fake = Faker()


def seed_data():
    with app.app_context():
        Guest.query.delete()
        Episode.query.delete()
        Appearance.query.delete()

        g1 = Guest(name=fake.name(), occupation=fake.word())
        g2 = Guest(name=fake.name(), occupation=fake.word())
        g3 = Guest(name=fake.name(), occupation=fake.word())
        g4 = Guest(name=fake.name(), occupation=fake.word())
        g5 = Guest(name=fake.name(), occupation=fake.word())

        ep1 = Episode(date='July 04, 1776', number=1)
        ep2 = Episode(date='April 22, 1991', number=2)
        ep3 = Episode(date='Jan 01, 2020', number=3)

        ep1.guests = [g1, g2]
        ep2.guests = [g3, g4, g5]
        ep3.guests = [g2, g4]

        db.session.add_all([g1, g2, g3, g4, g5, ep1, ep2, ep3])
        for ap in g1.appearances:
            ap.rating = 5
        for ap in g2.appearances:
            ap.rating = 4
        for ap in g3.appearances:
            ap.rating = 3
        for ap in g4.appearances:
            ap.rating = 2
        for ap in g5.appearances:
            ap.rating = 1
        db.session.commit()



if __name__ == '__main__':
    seed_data()