import hashlib
from typing import Tuple

import requests


class PasswordPwnedSearch:
    def __init__(self, password_typed: str) -> None:
        self.password_hashed = self.__hash_password(password_typed)

    def __hash_password(self, password_typed: str) -> str:
        return hashlib.sha1(password_typed.encode("utf-8")).hexdigest().upper()

    def __divide_hashed_password(self, hashed_password: str) -> Tuple[str, str]:
        return hashed_password[:5], hashed_password[5:]

    def __pwned_api(self, hashed_password_head: str):
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{hashed_password_head}"
        )
        return response

    def verify(self) -> Tuple[str, int]:
        head, tail = self.__divide_hashed_password(self.password_hashed)
        response = self.__pwned_api(head)

        if not response.ok:
            raise RuntimeError("Error: {}".format(response.status_code))

        hashes = (line.split(":") for line in response.text.splitlines())
        count = next((int(count) for t, count in hashes if t == tail), 0)
        return self.password_hashed, count
