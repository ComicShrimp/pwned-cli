import hashlib
import requests
from typing import Tuple


class PasswordPwnedSearch:
    def __init__(self, password_typed: str) -> None:
        self.password_hashed = self.__hash_password(password_typed)

    def __hash_password(self, password_typed: str) -> str:
        return hashlib.sha1(password_typed.encode("utf-8")).hexdigest().upper()

    def __pwned_api(self, hashed_password_head: str):
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{hashed_password_head}"
        )
        return response

    def verify(self) -> Tuple[str, int]:
        head, tail = self.password_hashed[:5], self.password_hashed[5:]
        res = self.__pwned_api(head)
        if not res.ok:
            raise RuntimeError('Error fetching "{}": {}'.format(url, res.status_code))
        hashes = (line.split(":") for line in res.text.splitlines())
        count = next((int(count) for t, count in hashes if t == tail), 0)
        return self.password_hashed, count
