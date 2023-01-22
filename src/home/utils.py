from faker import Faker

def get_user_profiles(count=10):
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
            data["fname"] = fname
            data["lname"] = lname
        
        user_data.append(data)

    return user_data    