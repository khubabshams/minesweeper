from utility import UtilityMixin
from firebase_admin import credentials
from firebase_admin import firestore
from getpass import getpass
import firebase_admin
import bcrypt
from typing import Union
import re

EMAIL_REGEX = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
CHAR_START_REGEX = r'^[a-zA-Z]'
NAME_LENGTH = 4
PASSWORD_LENGTH = 8

CRED = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(CRED)
FIREBASE_CLIENT = firestore.client()


class User(UtilityMixin):

    def get_firestore_collection(self) -> object:
        """
        Get firebase game users collection
        """
        return FIREBASE_CLIENT.collection(u'GameUsers')

    def _set_user_data(self, user_data: dict) -> None:
        """
        Set user's object attributes
        """
        self.email = user_data.get('email')
        self.password = user_data.get('password')
        self.username = user_data.get('username')

    def _authentication_response(self, user_data: dict) -> None:
        """
        Set user's attributes and print auth success message
        """
        self._set_user_data(user_data)
        self.print_success_message(
            f"Hi {user_data.get('username')}, enjoy playing ...\n")

    def _verify_user_record(self, user_record: dict, password: str) -> dict:
        """
        Check the user record and compare the hashed password
        with the one from user record and give feedback accordingly
        """
        verified_password = user_record and bcrypt.\
            checkpw(password.encode('utf-8'), user_record["key"]) or False
        if not user_record or not verified_password:
            self.print_failure_message(
                "Wrong email or password, please try again")
            self.login()
        return user_record

    def _search_user_record(self, email: str) -> Union[dict, bool]:
        """
        Search the game users table by email for a record of user
        """
        firestore_collection = self.get_firestore_collection()
        docs = firestore_collection.where(u'email', u'==', email).\
            limit(1).get()
        return docs and docs[0].to_dict() or False

    def authenticate(self, email: str, password: str) -> dict:
        """
        Identify if there's a record exist for user
        by searching by the given credentials
        """
        print("Getting things done ...")
        user_record = self._search_user_record(email)
        self._verify_user_record(user_record, password)
        self._authentication_response(user_record)
        return user_record

    def _is_email_registered(self, email: str) -> bool:
        """
        Check if the email in use already in game users table
        """
        user_record = self._search_user_record(email)
        return user_record and True or False

    def _validate_email(self, email: str) -> bool:
        """
        Check if entered email is valid and provide a feedback
        """
        if re.search(EMAIL_REGEX, email):
            if not self._is_email_registered(email):
                return True
            self.print_failure_message("Email already exists, "
                                       "please use a different email")
        else:
            self.print_failure_message("Please enter a valid email")
        return False

    def _get_hashed_password(self, password: str) -> bool:
        """
        Hashing a given password using bcrypt
        """
        return bcrypt.hashpw(password.encode('utf-8'),
                             bcrypt.gensalt(rounds=10))

    def _validate_credential(self, cred: str, length: int,
                             cred_name: str) -> bool:
        """
        Check if the entered credential meets validity requirements
        (starting by letter, minimum characters size)
        """
        if re.search(CHAR_START_REGEX, cred):
            if len(cred) >= length:
                return True
            self.print_failure_message(
                f"{cred_name} must be a minimum of {length} characters")
        else:
            self.print_failure_message(f"{cred_name} must start with a letter")
        return False

    def _validate_username(self, name: str) -> bool:
        """
        Check if entered name is starting with a letter,
        and have amin of NAME_LENGTH
        """
        return self._validate_credential(name, NAME_LENGTH, 'Name')

    def _validate_password(self, password: str, confirm: bool = False) -> bool:
        """
        Check if entered password is starting with a letter,
        and have amin of PASSWORD_LENGTH
        """
        return self._validate_credential(password, PASSWORD_LENGTH, 'Password')

    def _validate_confirmed_password(self, password: str,
                                     password_confirm: str) -> str:
        """
        Match password with confirmation password
        re-ask for password if it's not matched
        """
        if password != password_confirm:
            self.print_failure_message(
                "Confirm password doesn't match entered password")
            return self._get_confirmed_password()
        else:
            return password

    def _get_username(self, validate: bool = True) -> str:
        """
        Get the user input of his name and validate it
        """
        name = input("Enter your name here:\n")
        validate and not self._validate_username(name) and \
            self._get_username(validate)
        return name

    def _get_email(self, validate: bool = True) -> str:
        """
        Get the user input of his email and validate it
        """
        email = input("Enter your email here:\n")
        validate and not self._validate_email(email) and \
            self._get_email(validate)
        return email

    def _get_password(self, confirm: bool = False,
                      validate: bool = True) -> str:
        """
        Get the user input of his login [confirmation] password and validate it
        """
        confirmation = confirm and " confirmation" or ""
        password = getpass(prompt=f"Enter your password{confirmation}"
                           " here (hidden characters):")
        validate and not self._validate_password(password, confirm) and \
            self._get_password(confirm, validate)
        return password

    def _get_confirmed_password(self) -> str:
        """
        Get the user input of password and a confirmation and validate it
        """
        password = self._get_password()
        password_confirm = self._get_password(confirm=True)
        return self._validate_confirmed_password(password, password_confirm)

    def _do_signup(self, username: str, email: str,
                   password: str) -> object:
        """
        Prepare user data and create a database record with it
        """
        hashed_password = self._get_hashed_password(password)
        user_data = {
            u'username': username,
            u'email': email,
            u'key': hashed_password
        }
        firestore_collection = self.get_firestore_collection()
        _, doc_ref = firestore_collection.add(user_data)
        return doc_ref

    def login(self) -> dict:
        """
        Ask for email, password. authenticate user credentials
        and show feedback
        """
        email = self._get_email(validate=False)
        password = self._get_password(validate=False)
        return self.authenticate(email, password)

    def signup(self) -> dict:
        """
        Rigister user data for first time in the database and authenticate
        """
        username = self._get_username()
        email = self._get_email()
        password = self._get_confirmed_password()
        doc_ref = self._do_signup(username, email, password)
        return self.authenticate(email, password)
