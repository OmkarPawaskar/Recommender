import csv
import datetime
from django.conf import settings
from faker import Faker

MOVIE_METADATA_CSV = settings.DATA_DIR / "movies_metadata.csv"

def validate_date_str(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except:
        return None
    return date_text

def load_movie_data(limit=1):
    with open(MOVIE_METADATA_CSV, newline="", encoding="UTF-8") as csv_file:
        reader = csv.DictReader(csv_file)
        dataset = []

        for i, row in enumerate(reader):
            _id = row.get("id")
            try:
                _id = int(_id)
            except:
                id = None
            release_date = validate_date_str(row.get("release_date"))

            dataset.append({
                "id" : _id,
                "title" : row.get("title"),
                "overview" : row.get("overview"),
                "release_date" : release_date
            })

            if i+1 > limit:
                break
        return dataset

def get_fake_profiles(count=10):
    fake = Faker()
    user_data = []

    for _ in range(count):
        profile = fake.profile()

        data = {
            "username" : profile.get("username"),
            "email" : profile.get("mail"),
            "is_active" : True
        }

        if "name" in profile:
            fname,lname = profile.get("name").split(" ")[:2]
            data["first_name"] = fname
            data["last_name"] = lname
        
        user_data.append(data)

    return user_data    