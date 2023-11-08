import random
import datetime
import string
from typing import List


COUNTRIES = ('Russia', 'Argentina', 'Brazil', 'Canada', 'Denmark', 'Estonia', 'France', 'Germany', 'Honduras', 'India', 'Japan', 'Kenya', 'Lithuania', 'Malaysia', 'Netherlands', 'Oman', 'Poland', 'Qatar', 'South Korea', 'Tanzania', 'Venezuela', 'Wales', 'Xinjiang', 'Yemen', 'Zimbabwe')

PRODUCT_CATEGORIES = ('OS', 'VR', 'Business', 'Education', 'Finance', 'Graphics & Design', 'Kids', 'Magazines & Newspapers', 'Music', 'News', 'Productivity', 'Browser Extension', 'Social Networking', 'Travel', 'Books', 'Developer Tools', 'Entertainment', 'Food & Drink', 'Health & Fitness', 'Lifestyle', 'Medical', 'Navigation', 'Photo & Video', 'Reference', 'Shopping', 'Sports', 'Utilities')

FIRST_NAMES = ('John', 'Jane', 'Mike', 'Emily', 'Chris', 'Sarah', 'David', 'Olivia', 'Matthew', 'Emma', 'Daniel', 'Grace', 'Michael', 'Lily', 'William', 'Sophia', 'James', 'Ava', 'Benjamin', 'Mia', 'Jacob', 'Chloe', 'Ethan', 'Abigail', 'Ryan', 'Ella', 'Alexander', 'Natalie', 'Joseph', 'Hannah')

LAST_NAMES = ('Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Clark', 'Lewis', 'Lee', 'Walker', 'Hall', 'Young', 'King', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson', 'Hill', 'Ramirez')

SOFTWARE_NAMES = ('Word', 'Excel', 'PowerPoint', 'Photoshop', 'Illustrator', 'Premiere Pro', 'After Effects', 'InDesign', 'Sketch', 'Figma', 'Visual Studio Code', 'PyCharm', 'Eclipse', 'Android Studio', 'Xcode', 'Unity', 'Unreal Engine', 'Blender', 'AutoCAD', 'MATLAB', 'RStudio', 'TensorFlow', 'Tableau', 'SAS', 'Git', 'Jira', 'Slack', 'Trello', 'Zoom', 'Google Docs', 'Notepad++')

ORGANIZATIONS = ('Google', 'Microsoft', 'Apple', 'Amazon', 'Facebook', 'IBM', 'Intel', 'Oracle', 'Adobe', 'Cisco', 'Samsung', 'Sony', 'Netflix', 'Tesla', 'SpaceX', 'NASA', 'Tesla', 'Toyota', 'Volkswagen', 'Ford', 'General Electric', 'Verizon', 'AT&T', 'Boeing', 'Walmart', 'Target', 'Nike', 'McDonalds', 'Coca-Cola', 'Pepsi')

EMAIL_DOMENS = ('google.com', 'yandex.ru', 'yahoo.com', 'mail.ru', 'hotmail.com')


def gen_countries() -> List[str]:
    QUERY_TEMPLATE = 'INSERT INTO "public"."countries" ("id", "name") VALUES (\'{}\', \'{}\');'
    
    queries = []
    for id, name in enumerate(COUNTRIES, start=1):
        queries.append(QUERY_TEMPLATE.format(id, name))

    return queries


def gen_product_categories() -> List[str]:
    QUERY_TEMPLATE = 'INSERT INTO "public"."product_categories" ("id", "name") VALUES (\'{}\', \'{}\');'

    queries = []
    for id, name in enumerate(PRODUCT_CATEGORIES, start=1):
        queries.append(QUERY_TEMPLATE.format(id, name))

    return queries


def get_random_date():
    current_date = datetime.date.today()
    delta = datetime.timedelta(days=random.randint(1, 3000))
    return str(current_date - delta)


def gen_products(count: int) -> List[str]:
    QUERY_TEMPLATE = 'INSERT INTO "public"."products" ("id", "name", "organization", "release_date", "category", "migration_price", "license_price") VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'

    ids = list(range(1, count + 1))
    names = SOFTWARE_NAMES
    organizations = [random.choice(ORGANIZATIONS) for _ in range(count)]
    release_dates = [get_random_date() for _ in range(count)]
    categories = [random.randint(1, len(PRODUCT_CATEGORIES)) for _ in range(count)]
    license_prices = [random.randint(1, 1000) for _ in range(count)]
    migration_prices = [int(license_prices[i] * 0.3) for i in range(count)]
    
    queries = []
    for row_data in zip(ids, names, organizations, release_dates, categories, migration_prices, license_prices):
        queries.append(QUERY_TEMPLATE.format(*row_data))

    return queries


def get_random_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    return ''.join(random.choices(lowercase + uppercase + digits, k=random.randint(6, 12)))


def gen_users(count: int) -> List[str]:
    QUERY_TEMPLATE = 'INSERT INTO "public"."users" ("id", "username", "email", "password", "first_name", "last_name", "country") VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'

    ids = list(range(1, count + 1))
    first_names = [random.choice(FIRST_NAMES) for _ in range(count)]
    last_names = [random.choice(LAST_NAMES) for _ in range(count)]
    countries = [random.randint(1, len(COUNTRIES)) for _ in range(count)]
    usernames = [first_names[i].lower() + str(random.randint(1, 9999)) for i in range(count)]
    emails = [f'{first_names[i].lower()}.{last_names[i].lower()}{random.randint(1, 9999)}@{random.choice(EMAIL_DOMENS)}' for i in range(count)]
    passwords = [get_random_password() for _ in range(count)]

    queries = []
    for row_data in zip(ids, usernames, emails, passwords, first_names, last_names, countries):
        queries.append(QUERY_TEMPLATE.format(*row_data))

    return queries


def gen_installations(count: int) -> List[str]:
    QUERY_TEMPLATE = 'INSERT INTO "public"."installations" ("id", "installation_date", "uninstallation_date", "user_id", "software_id") VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'

    ids = list(range(1, count + 1))
    installation_dates = [get_random_date() for _ in range(count)]
    uninstallation_dates = [datetime.datetime.strptime(installation_dates[i], '%Y-%m-%d') + datetime.timedelta(days=random.randint(1, 500)) for i in range(count)]
    user_ids = [random.randint(1, count) for _ in range(count)]
    software_ids = [random.randint(1, len(SOFTWARE_NAMES)) for _ in range(count)]

    queries = []
    for row_data in zip(ids, installation_dates, uninstallation_dates, user_ids, software_ids):
        queries.append(QUERY_TEMPLATE.format(*row_data))

    return queries


def save(queries: List[str], path: str) -> None:
    with open(path, mode='w') as file:
        file.write('\n'.join(queries))


def main():
    count = 5000000

    queries = []
    queries += gen_countries()
    queries += gen_product_categories()
    queries += gen_products(count)
    queries += gen_users(count)
    queries += gen_installations(count)

    save(queries, './_all.sql')

    # queries = []
    # queries += gen_countries()
    # queries += gen_product_categories()
    # queries += gen_products(count)
    # queries += gen_users(count)
    # queries += gen_installations(count)
    #
    # save(queries, './all.sql')
    

if __name__ == '__main__':
    main()
