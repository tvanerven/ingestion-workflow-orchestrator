import factory
from faker import Faker
from datetime import datetime
import random

fake = Faker()

class AssetFactory(factory.Factory):
    class Meta:
        model = dict

    title = factory.LazyFunction(lambda: ' '.join(fake.words(nb=random.randint(1, 6))))
    description = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=3))
    doi = factory.LazyFunction(lambda: f"https://doi.org/{fake.doi()}")
    start_date = factory.LazyFunction(lambda: fake.date_between(start_date='-3y', end_date='-1y').strftime('%Y-%m-%d'))
    end_date = factory.LazyFunction(lambda: fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'))

    # ✅ This now generates 1–10 random keywords
    keywords = factory.LazyFunction(lambda: fake.words(nb=random.randint(1, 10)))

    alternative_url = factory.Faker("url")
    language = factory.LazyFunction(lambda: random.choice(["English", "Spanish", "German", "French", "Dutch"]))
    subject = factory.LazyFunction(lambda: random.choice([
        "Agricultural Sciences", 
        "Arts and Humanities", 
        "Astronomy and Astrophysics", 
        "Business and Management", 
        "Chemistry",
        "Computer and Information Science",
        "Earth and Environmental Sciences",
        "Engineering",
        "Law",
        "Mathematical Sciences",
        "Medicine, Health and Life Sciences",
        "Physics",
        "Social Sciences",
        "Other",
    ]))

    @factory.post_generation
    def dataset_contacts(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self['dataset_contacts'] = extracted

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self['authors'] = extracted


class ContactFactory(factory.Factory):
    class Meta:
        model = dict

    name = factory.LazyFunction(lambda: fake.name())
    email = factory.LazyFunction(lambda: fake.email())
    affiliation = factory.LazyFunction(lambda: fake.company())


class AuthorFactory(factory.Factory):
    class Meta:
        model = dict

    name = factory.LazyFunction(lambda: fake.name())
    affiliation = factory.LazyFunction(lambda: fake.company())
    identifier_scheme = factory.LazyFunction(lambda: random.choice([
        "ORCID",
        "ROR",
        "ISNI",
        "LCNA",
        "VIAF",
        "GND",
        "DAI", 
        "ResearcherID", 
        "ScopusID",
    ]))
    identifier = factory.LazyFunction(lambda: fake.uuid4())
