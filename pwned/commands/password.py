import hashlib
import requests
from typing import Tuple


def hash_password(password: str) -> str:
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()


def pwned_api(hashed_password_head: str):
    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{hashed_password_head}"
    )

    return response


def password_pwned_search(password: str) -> Tuple[str, int]:
    hashed_password = hash_password(password)
    return ("Hey", 1)
