import random
import uuid
import datetime
from typing import Optional, Set, List

import wonderwords

import data


def get_countries_sql() -> List[str]:
    QUERY_TEMPLATE = "INSERT INTO public.countries (\"name\", \"language\") " \
                     "VALUES ('{}', '{}');"

    queries = [
        QUERY_TEMPLATE.format(country, language)
        for country, language in data.COUNTRIES.items()
    ]

    return queries


class User:
    _uuids: Set[str] = set()
    _usernames: Set[str] = set()

    QUERY_TEMPLATE = "INSERT INTO store.users " \
                     "VALUES ('{}', '{}', '{}', '{}', '{}');"

    def __init__(self, *, id: Optional[str] = None, username: Optional[str] = None,
                 country: Optional[int] = None, user_type: Optional[str] = None,
                 application: Optional[str] = None) -> None:
        if id in User._uuids:
            raise ValueError(f"passed id='{id}' has already been used")
        else:
            self.id = id or self._gen_id()
            User._uuids.add(self.id)

        if username in self._usernames:
            raise ValueError(f"passed username='{username}' has already "
                             "been used")
        else:
            self.username = username or self._gen_username()
            self._usernames.add(self.username)

        if country and not (1 <= country <= len(data.COUNTRIES)):
            raise ValueError(f"passed country number '{country}' goes beyond the boundaries")
        else:
            self.country = country or self._gen_country()

        if user_type and user_type not in data.USER_TYPES:
            raise ValueError(f"passed user_type='{user_type}' is not contained in data.USER_TYPES")
        else:
            self.user_type = user_type or self._gen_user_type()
            if user_type:
                self.user_type = user_type
            else:
                self.user_type = 'individual' if random.randint(0, 4) else self._gen_user_type()

        if application and application not in data.USER_APPLICATIONS:
            raise ValueError(f"passed application='{application}' is not contained in data.USER_APPLICATIONS")
        else:
            self.application = application or self._gen_application()
            if application:
                self.application = application
            else:
                self.application = 'default' if self.user_type == 'individual' else self._gen_application()


    @staticmethod
    def _gen_id() -> str:
        while (id := str(uuid.uuid4())) in User._uuids:
            pass

        return id

    @staticmethod
    def _gen_username() -> str:
        username = random.choice(data.FIRST_NAMES + data.LAST_NAMES).lower()

        if username in User._usernames:
            r = wonderwords.RandomWord()
            username = r.word(include_parts_of_speech=["adjectives"]) \
                     + username.capitalize()

        while username in User._usernames:
            username += hex(random.randint(0, 9999))[2:]

        return username

    @staticmethod
    def _gen_country() -> int:
        if not data.COUNTRIES:
            raise AssertionError("'COUNTRIES' collection is empty")

        return random.randint(1, len(data.COUNTRIES))

    @staticmethod
    def _gen_user_type() -> str:
        if not data.USER_TYPES:
            raise AssertionError("'USER_TYPES' collection is empty")

        return random.choice(data.USER_TYPES)

    @staticmethod
    def _gen_application() -> str:
        if not data.USER_APPLICATIONS:
            raise AssertionError("'USER_APPLICATIONS' collection is empty")

        return random.choice(data.USER_APPLICATIONS)

    def __str__(self) -> str:
        return f"User(id='{self.id}', username='{self.username}', " \
               f"country='{self.country}', user_type='{self.user_type}', " \
               f"application='{self.application}'"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(self.id, self.username, self.country,
                                          self.user_type, self.application)


class Software:
    _uuids = set()
    _names = set()

    QUERY_TEMPLATE = "INSERT INTO store.softwares " \
                     "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');"

    def __init__(self, *, id: Optional[str] = None, name: Optional[str] = None,
                 category: Optional[str] = None, version: Optional[str] = None,
                 release_date: Optional[datetime.date] = None, license_price: Optional[int] = None,
                 migration_price: Optional[int] = None) -> None:
        if id in self._uuids:
            raise ValueError(f"passed id='{id}' has already been used")
        else:
            self.id = id or self._gen_id()
            Software._uuids.add(self.id)

        if name in self._names:
            raise ValueError(f"passed name={name} has already been used")
        else:
            self.name = name or self._gen_name()
            self._names.add(self.name)

        if category and category not in data.SOFTWARE_CATEGORIES:
            raise ValueError(f"passed category='{category}' is not contained in data.SOFTWARE_CATEGORIES")
        else:
            self.category = category or self._gen_category()

        self.version = version or self._gen_version()
        self.release_date = release_date or self._gen_release_date()
        
        if license_price and license_price < 0:
            raise ValueError(f"license_price={license_price} cannot be negative")
        else:
            self.license_price = license_price or self._gen_license_price()

        if migration_price and not (0 <= migration_price <= self.license_price):
            raise ValueError(f"migration_price={migration_price} cannot be negative and be more than license_price")
        else:
            self.migration_price = migration_price or self._gen_migration_price(self.license_price)
        

    @staticmethod
    def _gen_id() -> str:
        while (id := str(uuid.uuid4())) in Software._uuids:
            pass

        return id

    @staticmethod
    def _gen_name() -> str:
        r = wonderwords.RandomWord()
        name = ''
        while (name := f'{name}{r.word().capitalize()}') in Software._names:
            pass

        return name

    @staticmethod
    def _gen_category() -> str:
        return random.choice(data.SOFTWARE_CATEGORIES)

    @staticmethod
    def _gen_version() -> str:
        major = random.randint(0, 20)
        minor = random.randint(0, 20)
        patches = random.randint(0, 20)
        return f'{major}.{minor}.{patches}'

    @staticmethod
    def _gen_release_date() -> datetime.date:
        current_date = datetime.date.today()
        days_before = random.randint(1000, 5000)
        return current_date - datetime.timedelta(days=days_before)

    @staticmethod
    def _gen_license_price() -> int:
        return 5 * random.randint(0, 30)

    @staticmethod
    def _gen_migration_price(license_price: int) -> int:
        return int(license_price * 0.3)

    def __str__(self) -> str:
        return f"Software(id='{self.id}', name='{self.name}', category='{self.category}', " \
               f"version='{self.version}', release_date='{self.release_date}', " \
               f"license_price='{self.license_price}', migration_price='{self.migration_price}')"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(self.id, self.name, self.category,
                                          self.version, self.release_date,
                                          self.license_price, self.migration_price)


class Purchase:
    _uuids = set()
    _purchases = set() 

    QUERY_TEMPLATE = "INSERT INTO store.purchase_history " \
                     "VALUES ('{}', '{}', '{}', '{}', '{}');"

    def __init__(self, *, id: Optional[str] = None, user_id: Optional[str] = None,
                 software_id: Optional[str] = None, price: Optional[int] = None,
                 purchase_date: Optional[datetime.date] = None) -> None:
        if id in Purchase._uuids:
            raise ValueError(f"passed id='{id}' has already been used")
        else:
            self.id = id or self._gen_id()
            Purchase._uuids.add(self.id)

        if software_id and software_id not in Software._uuids:
            raise ValueError(f"there is not software with id='{software_id}'")
        else:
            self.software_id = software_id or self._gen_software_id()

        if user_id and user_id not in User._uuids:
            raise ValueError(f"there is not user with id='{user_id}'")
        else:
            self.user_id = self._gen_user_id()
            while (self.user_id, self.software_id) in Purchase._purchases:
                self.user_id = self._gen_user_id()
            Purchase._purchases.add((self.user_id, self.software_id))

        if price and price < 0:
            raise ValueError(f"passed price='{price}' cannot be negative")
        else:
            self.price = price or self._gen_price()

        if purchase_date and purchase_date > datetime.date.today():
            raise ValueError(f"passed purchase_date={purchase_date} cannot be later than the current date")
        else:
            self.purchase_date = purchase_date or self._gen_purchase_date()

    @staticmethod
    def _gen_id() -> str:
        while (id := str(uuid.uuid4())) in Purchase._uuids:
            pass

        return id

    @staticmethod
    def _gen_user_id() -> str:
        return random.choice(user_ids)

    @staticmethod
    def _gen_software_id() -> str:
        return random.choice(software_ids)

    @staticmethod
    def _gen_price() -> int:
        return 5 * random.randint(0, 30)

    @staticmethod
    def _gen_purchase_date() -> datetime.date:
        current_date = datetime.date.today()
        days_before = random.randint(0, 1000)
        return current_date - datetime.timedelta(days=days_before)

    def __str__(self) -> str:
        return f"Purchase(id='{self.id}', user_id='{self.user_id}', " \
               f"software_id='{self.software_id}', price='{self.price}, " \
               f"purchase_date='{self.purchase_date}')"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(self.id, self.user_id, self.software_id,
                                          self.price, self.purchase_date)


class Review:
    _uuids = set()
    _reviews = set()

    QUERY_TEMPLATE = "INSERT INTO store.reviews " \
                     "VALUES ('{}', '{}', '{}', '{}', '{}', '{}');"

    def __init__(self, *, id: Optional[str] = None, user_id: Optional[str] = None,
                 software_id: Optional[str] = None, rating: Optional[int] = None,
                 review_content: Optional[str] = None,
                 review_date: Optional[datetime.date] = None) -> None:
        if id in Review._uuids:
            raise ValueError(f"passed id='{id}' has already been used")
        else:
            self.id = id or self._gen_id()
            Review._uuids.add(self.id)

        if software_id and software_id in Software._uuids:
            raise ValueError(f"there is software with id='{software_id}'")
        else:
            self.software_id = software_id or self._gen_software_id()

        if user_id and user_id in User._uuids:
            raise ValueError(f"there is user with id='{user_id}'")
        else:
            self.user_id = self._gen_user_id()
            while (self.user_id, self.software_id) in Review._reviews:
                self.user_id = self._gen_user_id()
            Review._reviews.add((self.user_id, self.software_id))

        if rating and not (1 <= rating <= 5):
            raise ValueError(f"passed rating='{raing}' must be at least 1 and not more than 5")
        else:
            self.rating = rating or self._gen_rating()

        if review_content:
            self.review_content = review_content
        else:
            self.review_content = self._gen_review_content() if not random.randint(0, 3) else 'NULL'

        if review_date and review_date > datetime.date.today():
            raise ValueError(f"passed review_date={review_date} cannot be later than the current date")
        else:
            self.review_date = review_date or self._gen_review_date()

    @staticmethod
    def _gen_id() -> str:
        while (id := str(uuid.uuid4())) in Purchase._uuids:
            pass

        return id
    
    @staticmethod
    def _gen_user_id() -> str:
        return random.choice(user_ids)

    @staticmethod
    def _gen_software_id() -> str:
        return random.choice(software_ids)

    @staticmethod
    def _gen_rating() -> int:
        return random.randint(1, 5)
    
    @staticmethod
    def _gen_review_content() -> str:
        r = wonderwords.RandomSentence()
        sentences = [r.sentence() for _ in range(random.randint(1, 5))]
        return ' '.join(sentences).replace("'", "").replace('"', '')

    @staticmethod
    def _gen_review_date() -> datetime.date:
        current_date = datetime.date.today()
        days_before = random.randint(0, 500)
        return current_date - datetime.timedelta(days=days_before)

    def __str__(self) -> str:
        return f"Review(id='{self.id}', user_id='{self.user_id}', " \
               f"software_id='{self.software_id}', rating='{self.rating}', " \
               f"review_content='{self.review_content}', review_date='{self.review_date}')"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(self.id, self.user_id, self.software_id, self.rating,
                                          self.review_content, self.review_date)


def save(queries: List[str], path: str, *, create_new: bool = True) -> None:
    mode = 'w' if create_new else 'a'
    with open(path, mode=mode) as file:
        file.write('\n'.join(queries) + '\n')


if __name__ == '__main__':
    filename = '_dump.sql'
    queries = []

    queries.extend(get_countries_sql())
    print('[debug]: countries generated')

    for i in range(1_000_000):
        if i > 0 and i % 10_000 == 0:
            print(f'[debug]: users generated {i}')
        queries.append(User().get_sql())
    else:
        print('[debug]: users generated')

    for i in range(300_000):
        if i > 0 and i % 10_000 == 0:
            print(f'[debug]: softwares generated {i}')
        queries.append(Software().get_sql())
    else:
        print('[debug]: softwares completed')

    global user_ids, software_ids
    user_ids = tuple(User._uuids)
    software_ids = tuple(Software._uuids)

    for i in range(3_000_000):
        if i > 0 and i % 10_000 == 0:
            print(f'[debug]: purchases generated {i}')
        queries.append(Purchase().get_sql())
    print('[debug]: purchases completed')

    for i in range(700_000):
        if i > 0 and i % 10_000 == 0:
            print(f'[debug]: reviews generated {i}')
        queries.append(Review().get_sql())
    else:
        print('[debug]: reviews completed')

    save(queries, filename)
