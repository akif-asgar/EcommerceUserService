from django.test import TestCase
# user_service/tests.py
import requests

def test_profile():
    
    login_url = "http://127.0.0.1:8000/api/user/login/"
    login_data = {
        "email": "user@gmail.com",
        "password": "pydev@123k1"
    }

    login_response = requests.post(login_url, json=login_data)
    tokens = login_response.json()['tokens']
    access_token = tokens['access']

    print("Access token:", access_token)


    profile_url = "http://127.0.0.1:8000/api/user/profile/"
    headers = {"Authorization": f"Bearer {access_token}"}
    profile_response = requests.get(profile_url, headers=headers)

    print("User profile data:", profile_response.json())


if __name__ == "__main__":
    test_profile()

