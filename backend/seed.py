from app import app, db
import requests
from tqdm import tqdm

from models.user import User
from models.companies import Company


with app.app_context():

    db.drop_all()

    db.create_all()

    print('Adding to database:')

    kasia = User(
        firstname="Kasia",
        lastname="Wiśniewska",
        age=29,
        role="Backend Developer",
        email="kasia.w@dev.com",
        company="Apple"
    )

    kasjan = User(
        firstname="Kasjan",
        lastname="Hinc",
        age=24,
        role="Frontend Developer",
        email="kasjan.h@dev.com",
        company="Apple"
    )

    michael = User(
        firstname="Michael",
        lastname="Jordan",
        age=33,
        role="Full Stack Developer",
        email="michael.j@dev.com",
        company="Microsoft"
    )

    david = User(
        firstname="Dawid",
        lastname="Hansen",
        age=48,
        role="Full Stack Developer",
        email="david.h@dev.com",
        company="Microsoft"
    )

    amanda = User(
        firstname="Amanda",
        lastname="Hayes",
        age=25,
        role="Recruitor",
        email="amanda.h@dev.com",
        company="Shell"
    )

    bill = User(
        firstname="Bill",
        lastname="Gates",
        age=42,
        role="UX Designer",
        email="bill.g@dev.com",
        company="Shell"
    )

    alex = User(
        firstname="Alex",
        lastname="Davidson",
        age=37,
        role="Team Manager",
        email="alex.d@dev.com",
        company="Last Minute"
    )

    mark = User(
        firstname="Mark",
        lastname="Smith",
        age=28,
        role="Team Manager",
        email="mark.s@dev.com",
        company="Shell"
    )

    maya = User(
        firstname="Maya",
        lastname="Angeles",
        age=24,
        role="UI Designer",
        email="maya.a@dev.com",
        company="Apple"
    )

    john = User(
        firstname="John",
        lastname="Sawyer",
        age=38,
        role="Senior Developer",
        email="john.s@dev.com",
        company="Shell"
    )

    natalia = User(
        firstname="Natalia",
        lastname="Zielińska",
        age=25,
        role="Mid Developer",
        email="natalia.z@dev.com",
        company="Last Minute"
    )

    kevin = User(
        firstname="Kevin",
        lastname="Lake",
        age=34,
        role="Mid Developer",
        email="kevin.l@dev.com",
        company="Microsoft"
    )

    robert = User(
        firstname="Robert",
        lastname="Piszczek",
        age=52,
        role="Junior Developer",
        email="robert.p@dev.com",
        company="Last Minute"
    )

    jack = User(
        firstname="Jack",
        lastname="Ball",
        age=54,
        role="Mid Developer",
        email="jack.b@dev.com",
        company="Shell"
    )

    bob = User(
        firstname="Bob",
        lastname="Frieda",
        age=29,
        role="UX Designer",
        email="bob.f@dev.com",
        company="Apple"
    )

    gary = User(
        firstname="Gary",
        lastname="Hall",
        age=33,
        role="Mid Developer",
        email="gary.h@dev.com",
        company="Last Minute"
    )

    anna = User(
        firstname="Anna",
        lastname="Middleton",
        age=34,
        role="Mid Developer",
        email="anna.m@dev.com",
        company="Shell"
    )

    paul = User(
        firstname="Paul",
        lastname="Blazer",
        age=47,
        role="Team Manager",
        email="paul.b@dev.com",
        company="Apple"
    )

    jessica = User(
        firstname="Jessica",
        lastname="Blanc",
        age=28,
        role="Junior Developer",
        email="jessica.b@dev.com",
        company="Last Minute"
    )

    kate = User(
        firstname="Kate",
        lastname="Kowalska",
        age=31,
        role="UX Designer",
        email="kate.k@dev.com",
        company="Shell"
    )

    apple = Company(
        name="Apple",
        users=[kasjan, kasia]
    )

    microsoft = Company(
        name="Microsoft"
    )
    lastminute = Company(
        name="Last Minute"
    )
    shell = Company(
        name="Shell"
    )

    db.session.add_all([kasia] + [kasjan] + [michael] +
                       [amanda] + [bill] + [alex] + [apple] + [microsoft] + [lastminute] + [shell] + [david] + [mark] + [maya] + [john] + [natalia] + [kevin] + [robert] + [shell] + [bob] + [gary] + [jack] + [anna] + [paul] + [jessica] + [kate])
    db.session.commit()

    print('Completed!')
