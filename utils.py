# utils.py
import re
from datetime import datetime
from constants import EXCLUDED_NUMBERS, VALID_COUNTRY_LIST, VALID_GENDERS, VALID_BLOOD_GROUPS
from log import logger


def is_excluded(mobile_num):
    """
    Check if the mobile number is in the excluded list.
    :param mobile_num: int - The mobile number to check.
    :return: bool - True if the number is excluded, False otherwise.
    """
    if mobile_num in EXCLUDED_NUMBERS:
        logger.info(f"{mobile_num} is in the excluded list.")
        logger.info("Mobile verification is successful.")
        return True
    return False


def is_valid_country(converted_str):
    """
    Validate the country code in the mobile number.
    :param converted_str: str - The mobile number string.
    :return: bool - True if the country code is valid, raises ValueError otherwise.
    """
    if converted_str[:2] in VALID_COUNTRY_LIST:
        logger.info("Mobile verification is successful.")
        return True
    else:
        raise ValueError(f"Invalid country code - {converted_str[:2]}. Valid country codes are {VALID_COUNTRY_LIST}")


def is_mobile_length_valid(converted_str):
    """
    Validate the length of the mobile number.
    :param converted_str: str - The mobile number string.
    :return: bool - True if the length is valid, raises ValueError otherwise.
    """
    if len(converted_str) == 12:
        return True
    else:
        raise ValueError(f"Invalid mobile number length {len(converted_str)}. The valid length is 12.")


def is_valid_type(mobile):
    """
    Validate the type of the mobile number.
    :param mobile: int - The mobile number.
    :return: bool - True if the type is valid, raises ValueError otherwise.
    """
    if isinstance(mobile, int):
        return True
    else:
        raise ValueError(f"Invalid mobile number type - {type(mobile)}")


def is_valid_email(email):
    """
    Validate the email format.
    :param email: str - The email to validate.
    :return: bool - True if the email is valid, raises ValueError otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        raise ValueError(f"Invalid email format - {email}")


def is_valid_dob(dob):
    """
    Validate the date of birth format (YYYY-MM-DD) and check if it's a valid date.
    :param dob: str - The date of birth to validate.
    :return: bool - True if the date is valid, raises ValueError otherwise.
    """
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError(f"Invalid date of birth format - {dob}. The valid format is YYYY-MM-DD")


def is_valid_gender(gender):
    """
    Validate the gender to be either 'Male', 'Female', or 'Other'.
    :param gender: str - The gender to validate.
    :return: bool - True if the gender is valid, raises ValueError otherwise.
    """
    if gender in VALID_GENDERS:
        return True
    else:
        raise ValueError(f"Invalid gender - {gender}. Valid options are {VALID_GENDERS}")


def is_valid_blood_group(blood_group):
    """
    Validate the blood group.
    :param blood_group: str - The blood group to validate.
    :return: bool - True if the blood group is valid, raises ValueError otherwise.
    """
    if blood_group in VALID_BLOOD_GROUPS:
        return True
    else:
        raise ValueError(f"Invalid blood group - {blood_group}. Valid options are {VALID_BLOOD_GROUPS}")
