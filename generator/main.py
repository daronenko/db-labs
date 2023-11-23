import random
import uuid
import datetime
from typing import Optional, Set, List, Tuple

import wonderwords

import data


def get_countries_sql() -> List[str]:
    QUERY_TEMPLATE = "INSERT INTO store.countries (\"name\", \"language\") " \
                     "VALUES ('{}', '{}');"

    queries = [
        QUERY_TEMPLATE.format(country, language)
        for country, language in data.COUNTRIES.items()
    ]

    return queries


def filter_str(text: str):
    return text.replace('"', '').replace("'", "")


class User:
    _uuids: Set[str] = set()
    _usernames: Set[str] = set()

    QUERY_TEMPLATE = "INSERT INTO store.users " \
                     "VALUES ('{}', '{}', '{}', '{}', '{}');"

    def __init__(self) -> None:
        self.id = User._gen_id()
        User._uuids.add(self.id)

        self.username = User._gen_username()
        User._usernames.add(self.username)

        self.country = User._gen_country()

        if random.randint(0, 4):
            self.user_type = 'individual'
        else:
            self.user_type = User._gen_user_type()

        if self.user_type == 'individual':
            self.application = 'default'
        else:
            self.application = User._gen_application()

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
            username = filter_str(
                r.word(include_parts_of_speech=["adjectives"])
            ) + username.capitalize()

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
    _uuids: Set[str] = set()
    _names: Set[str] = set()

    QUERY_TEMPLATE = "INSERT INTO store.softwares " \
        "VALUES ('{}', '{}', '{}', '{}', '{}'::varchar[], '{}', '{}', '{}', '{}');"

    def __init__(self) -> None:
        self.id = Software._gen_id()
        Software._uuids.add(self.id)

        self.name = Software._gen_name()
        self._names.add(self.name)

        self.description = Software._gen_description()
        self.category = Software._gen_category()
        self.tags = Software._gen_tags()
        self.version = Software._gen_version()
        self.release_date = Software._gen_release_date()
        self.license_price = Software._gen_license_price()
        self.migration_price = Software._gen_migration_price(
            self.license_price
        )

    @staticmethod
    def _gen_id() -> str:
        while (id := str(uuid.uuid4())) in Software._uuids:
            pass

        return id

    @staticmethod
    def _gen_name() -> str:
        r = wonderwords.RandomWord()
        name = ''
        while (name := f'{name}{filter_str(r.word()).capitalize()}') \
                in Software._names:
            pass

        return name

    @staticmethod
    def _gen_description() -> str:
        rs = wonderwords.RandomSentence()
        return rs.sentence()

    @staticmethod
    def _gen_category() -> str:
        return random.choice(data.SOFTWARE_CATEGORIES)

    @staticmethod
    def _gen_tags() -> str:
        rw = wonderwords.RandomWord()
        tags = '{' + ', '.join([
            rw.word(include_parts_of_speech=["nouns"])
            for _ in range(random.randint(0, 5))
        ]) + '}'
        return filter_str(tags)

    @staticmethod
    def _gen_version() -> str:
        major = random.randint(0, 20)
        minor = random.randint(0, 20)
        patches = random.randint(0, 20)
        return f'{major}.{minor}.{patches}'

    @staticmethod
    def _gen_release_date() -> datetime.date:
        current_date = datetime.date.today()
        days_before = random.randint(2000, 7000)
        return current_date - datetime.timedelta(days=days_before)

    @staticmethod
    def _gen_license_price() -> int:
        return 5 * random.randint(0, 30)

    @staticmethod
    def _gen_migration_price(license_price: int) -> int:
        return int(license_price * 0.3)

    def __str__(self) -> str:
        return f"Software(id='{self.id}', name='{self.name}', " \
               f"description='{self.description}'" \
               f"category='{self.category}', tags='{self.tags}', " \
               f"version='{self.version}', " \
               f"release_date='{self.release_date}', " \
               f"license_price='{self.license_price}', " \
               f"migration_price='{self.migration_price}')"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(
            self.id, self.name, self.description, self.category, self.tags,
            self.version, self.release_date,
            self.license_price, self.migration_price
        )


class Purchase:
    _uuids: Set[str] = set()
    _purchases: Set[Tuple[str, str]] = set()

    QUERY_TEMPLATE = "INSERT INTO store.purchase_history " \
                     "VALUES ('{}', '{}', '{}', '{}', '{}');"

    def __init__(self) -> None:
        self.id = Purchase._gen_id()
        Purchase._uuids.add(self.id)

        self.software_id = Purchase._gen_software_id()

        self.user_id = Purchase._gen_user_id()
        while (self.user_id, self.software_id) in Purchase._purchases:
            self.user_id = Purchase._gen_user_id()
        Purchase._purchases.add((self.user_id, self.software_id))

        self.price = Purchase._gen_price()
        self.purchase_date = Purchase._gen_purchase_date()

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
        days_before = random.randint(1000, 2000)
        return current_date - datetime.timedelta(days=days_before)

    def __str__(self) -> str:
        return f"Purchase(id='{self.id}', user_id='{self.user_id}', " \
               f"software_id='{self.software_id}', price='{self.price}, " \
               f"purchase_date='{self.purchase_date}')"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(
            self.id, self.user_id, self.software_id,
            self.price, self.purchase_date
        )


class Review:
    _uuids: Set[str] = set()
    _reviews: Set[Tuple[str, str]] = set()

    QUERY_TEMPLATE = "INSERT INTO store.reviews " \
        "VALUES ('{}', '{}', '{}', '{}', '{}'::jsonb, '{}');"

    def __init__(self) -> None:
        self.id = Review._gen_id()
        Review._uuids.add(self.id)

        self.software_id = Review._gen_software_id()

        self.user_id = Review._gen_user_id()
        while (self.user_id, self.software_id) in Review._reviews:
            self.user_id = Review._gen_user_id()
        Review._reviews.add((self.user_id, self.software_id))

        self.rating = Review._gen_rating()

        if random.randint(0, 3):
            self.review_content = '{}'
        else:
            self.review_content = Review._gen_review_content()

        self.review_date = Review._gen_review_date()

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
        rw = wonderwords.RandomWord()
        title = filter_str(' '.join(rw.random_words(3)).title())

        rs = wonderwords.RandomSentence()
        sentences = [
            filter_str(rs.sentence())
            for _ in range(random.randint(1, 5))
        ]
        body = ' '.join(sentences)

        return f'{{"title": "{title}", "body": "{body}"}}'

    @staticmethod
    def _gen_review_date() -> datetime.date:
        current_date = datetime.date.today()
        days_before = random.randint(0, 1000)
        return current_date - datetime.timedelta(days=days_before)

    def __str__(self) -> str:
        return f"Review(id='{self.id}', user_id='{self.user_id}', " \
               f"software_id='{self.software_id}', rating='{self.rating}', " \
               f"review_content='{self.review_content}', " \
               f"review_date='{self.review_date}')"

    def get_sql(self) -> str:
        return self.QUERY_TEMPLATE.format(
            self.id, self.user_id, self.software_id, self.rating,
            self.review_content, self.review_date
        )


def save(queries: List[str], path: str, *, create_new: bool = True) -> None:
    mode = 'w' if create_new else 'a'
    with open(path, mode=mode) as file:
        file.write('\n'.join(queries) + '\n')


if __name__ == '__main__':
    queries = []

    # filename = '../big-dump.sql'
    # buckets_count = 10
    # users_count = 200_000
    # softwares_count = 900
    # purchases_count = 400_000
    # reviews_count = 100_000

    filename = '../test-dump.sql'
    buckets_count = 1
    users_count = 3000
    softwares_count = 500
    purchases_count = 4000
    reviews_count = 700

    queries.extend(get_countries_sql())
    save(queries, filename)
    print('[debug]: countries generated')

    for bucket in range(buckets_count):
        queries.clear()

        for i in range(users_count):
            if i > 0 and i % 20_000 == 0:
                print(f'[debug]: users generated {int(i / users_count * 100)}%')
            queries.append(User().get_sql())
        else:
            print('[debug]: users generated')

        for i in range(softwares_count):
            if i > 0 and i % 20_000 == 0:
                print(f'[debug]: softwares generated {int(i / softwares_count * 100)}%')
            queries.append(Software().get_sql())
        else:
            print('[debug]: softwares completed')

        global user_ids, software_ids
        user_ids = tuple(User._uuids)
        software_ids = tuple(Software._uuids)

        for i in range(purchases_count):
            if i > 0 and i % 20_000 == 0:
                print(f'[debug]: purchases generated {int(i / purchases_count * 100)}%')
            queries.append(Purchase().get_sql())
        print('[debug]: purchases completed')

        for i in range(reviews_count):
            if i > 0 and i % 20_000 == 0:
                print(f'[debug]: reviews generated {int(i / reviews_count * 100)}%')
            queries.append(Review().get_sql())
        else:
            print('[debug]: reviews completed')

        save(queries, filename, create_new=False)
        print(f'[debug]: bucket generated {bucket + 1}')
    else:
        print('[debug]: all buckets generated')
