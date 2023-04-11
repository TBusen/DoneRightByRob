from basicWithdb import db, Puppy

## create##

my_puppy = Puppy('Rufus', 5)

db.session.add(my_puppy)
db.session.commit()

## read##

all_puppies = Puppy.query.all() # list of puppies objects in the table
print(all_puppies)

# select ID

puppy_one = Puppy.query.get(1)
print(puppy_one)


#Filter

puppy_frankie = Puppy.query.filter_by(name='Frankie') # produces sql
print(puppy_frankie.all()) # gets all of them


## UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


## Delete

second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()


all_puppies= Puppy.query.all()
print(all_puppies)

