#!/usr/bin/python3
"""
User model
"""
import hashlib
import uuid


class user():
    """
    user class:
    - id: public string unique (uuid)
    - password: private string has in MD5
    """

    __password = None

    def __init__(self):
        """
        Initialize a new user.
        - assigned an uniue `id`
        """
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """
        password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        password setter:
        - `None` if `pwd` is `None`
        - `None` if `pwd` is not a string
        - Hash `pwd` in MD5 before assign to `__password`
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        valid password:
        - `False` if `pwd` is `None`
        - `False` if `pwd` is not a string
        - `False` if `__password` is `None`
        - Compare `__password` and the MD5 value of `pwd`
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().upper() == self.__password
    

    if __name__ == '__main__':
        print("Test User")

