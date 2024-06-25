# main.py
from utils import (
    is_valid_type, is_mobile_length_valid, is_excluded, is_valid_country,
    is_valid_email, is_valid_dob, is_valid_gender, is_valid_blood_group
)
from constants import data
from log import logger


def is_valid_mobile(mobile):
    """
    Validate the mobile number based on type, length, exclusion list, and country code.
    :param mobile: int - The mobile number.
    :return: bool - True if the mobile number is valid, False otherwise.
    """
    try:
        # Convert the mobile number to a string for easier manipulation
        converted_str = str(mobile)

        # Extract the main number part after the country code
        mobile_num = int(converted_str[2:])

        # Perform the various checks
        if is_valid_type(mobile) and is_mobile_length_valid(converted_str):
            # Excluded numbers require no further validation
            if is_excluded(mobile_num):
                return True
            if is_valid_country(converted_str):
                return True
        return False
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return False


def add_user(name, email, mobile, dob, gender, blood_group):
    """
    Add a new user to the data dictionary after validating the email, mobile number, DOB, gender, and blood group.
    :param name: str - The name of the user.
    :param email: str - The email of the user.
    :param mobile: int - The mobile number of the user.
    :param dob: str - The date of birth of the user in YYYY-MM-DD format.
    :param gender: str - The gender of the user.
    :param blood_group: str - The blood group of the user.
    """
    try:
        if (
                is_valid_email(email) and is_valid_mobile(mobile) and
                is_valid_dob(dob) and is_valid_gender(gender) and
                is_valid_blood_group(blood_group)
        ):
            user = {
                "name": name,
                "email": email,
                "mobile": mobile,
                "dob": dob,
                "gender": gender,
                "blood_group": blood_group
            }
            data["records"].append(user)
            logger.info(f"User {name} added successfully!")
        else:
            logger.warning("User could not be added due to validation errors.")
    except ValueError as e:
        logger.error(f"Error: {e}")


    # Example test cases to verify various scenarios
users = [
        {"name": "Kiran1", "email": "a@gmail.com", "mobile": 919898989898, "dob": "1990-01-01", "gender": "Female",
         "blood_group": "A+"},  # Valid
        {"name": "Kiran2", "email": "b@gmail.com", "mobile": 459898989898, "dob": "1985-05-15", "gender": "Male",
         "blood_group": "B+"},  # Valid
        {"name": "Kiran3", "email": "c@gmail.com", "mobile": 759898989898, "dob": "2000-12-12", "gender": "Other",
         "blood_group": "O+"},  # Valid
        {"name": "Kiran4", "email": "d@gmail.com", "mobile": 329999999999, "dob": "1995-07-25", "gender": "Male",
         "blood_group": "AB+"},  # Invalid country code
        {"name": "Kiran5", "email": "e@gmail.com", "mobile": 919999999999, "dob": "1992-03-10", "gender": "Female",
         "blood_group": "A-"},  # Excluded number
        {"name": "Kiran6", "email": "f@gmail.com", "mobile": [43432754], "dob": "1988-09-09", "gender": "Male",
         "blood_group": "B-"},  # Invalid type
        {"name": "Kiran7", "email": "g@gmail.com", "mobile": 919898989, "dob": "2001-04-04", "gender": "Female",
         "blood_group": "O-"},  # Invalid length
        {"name": "Kiran8", "email": "h@gmail.com", "mobile": 919898989898, "dob": "1998-02-30", "gender": "Male",
         "blood_group": "AB-"},  # Invalid DOB
        {"name": "Kiran9", "email": "i@gmail.com", "mobile": 919898989898, "dob": "1993-08-08",
         "gender": "InvalidGender", "blood_group": "A+"},  # Invalid gender
        {"name": "Kiran10", "email": "j@gmail.com", "mobile": 919898989898, "dob": "1997-11-11", "gender": "Male",
         "blood_group": "InvalidBloodGroup"},  # Invalid blood group
    ]

for user in users:
    add_user(user["name"], user["email"], user["mobile"], user["dob"], user["gender"], user["blood_group"])

logger.info("\nData records:")
logger.info(data)
