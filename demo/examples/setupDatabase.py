from basicWithdb import db, Puppy

db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

print(sam.id)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)