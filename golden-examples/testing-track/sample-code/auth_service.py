"""
User Authentication Module

A sample module for practicing documentation and testing workflows.
This code intentionally lacks comprehensive documentation and tests.
"""

import hashlib
import secrets
import re
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum


class AuthError(Exception):
    """Base exception for authentication errors."""
    pass


class InvalidCredentialsError(AuthError):
    """Raised when login credentials are invalid."""
    pass


class AccountLockedError(AuthError):
    """Raised when account is locked due to too many failed attempts."""
    pass


class TokenExpiredError(AuthError):
    """Raised when authentication token has expired."""
    pass


class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


@dataclass
class User:
    id: str
    email: str
    password_hash: str
    role: UserRole
    created_at: datetime
    last_login: Optional[datetime] = None
    failed_attempts: int = 0
    locked_until: Optional[datetime] = None


@dataclass
class AuthToken:
    token: str
    user_id: str
    expires_at: datetime
    created_at: datetime


class PasswordValidator:
    def __init__(
        self,
        min_length: int = 8,
        require_uppercase: bool = True,
        require_lowercase: bool = True,
        require_digit: bool = True,
        require_special: bool = True
    ):
        self.min_length = min_length
        self.require_uppercase = require_uppercase
        self.require_lowercase = require_lowercase
        self.require_digit = require_digit
        self.require_special = require_special

    def validate(self, password: str) -> List[str]:
        errors = []
        
        if len(password) < self.min_length:
            errors.append(f"Password must be at least {self.min_length} characters")
        
        if self.require_uppercase and not re.search(r'[A-Z]', password):
            errors.append("Password must contain at least one uppercase letter")
        
        if self.require_lowercase and not re.search(r'[a-z]', password):
            errors.append("Password must contain at least one lowercase letter")
        
        if self.require_digit and not re.search(r'\d', password):
            errors.append("Password must contain at least one digit")
        
        if self.require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("Password must contain at least one special character")
        
        return errors

    def is_valid(self, password: str) -> bool:
        return len(self.validate(password)) == 0


class AuthenticationService:
    MAX_FAILED_ATTEMPTS = 5
    LOCKOUT_DURATION_MINUTES = 30
    TOKEN_EXPIRY_HOURS = 24

    def __init__(self):
        self._users: Dict[str, User] = {}
        self._tokens: Dict[str, AuthToken] = {}
        self._password_validator = PasswordValidator()

    def _hash_password(self, password: str, salt: Optional[str] = None) -> str:
        if salt is None:
            salt = secrets.token_hex(16)
        hash_input = f"{password}{salt}"
        password_hash = hashlib.sha256(hash_input.encode()).hexdigest()
        return f"{salt}${password_hash}"

    def _verify_password(self, password: str, stored_hash: str) -> bool:
        salt, _ = stored_hash.split('$')
        return self._hash_password(password, salt) == stored_hash

    def register(self, email: str, password: str, role: UserRole = UserRole.USER) -> User:
        if email in [u.email for u in self._users.values()]:
            raise AuthError("Email already registered")
        
        validation_errors = self._password_validator.validate(password)
        if validation_errors:
            raise AuthError(f"Invalid password: {', '.join(validation_errors)}")
        
        user_id = secrets.token_urlsafe(16)
        user = User(
            id=user_id,
            email=email,
            password_hash=self._hash_password(password),
            role=role,
            created_at=datetime.utcnow()
        )
        self._users[user_id] = user
        return user

    def login(self, email: str, password: str) -> AuthToken:
        user = self._find_user_by_email(email)
        
        if user is None:
            raise InvalidCredentialsError("Invalid email or password")
        
        if self._is_account_locked(user):
            raise AccountLockedError(
                f"Account locked. Try again after {user.locked_until}"
            )
        
        if not self._verify_password(password, user.password_hash):
            self._record_failed_attempt(user)
            raise InvalidCredentialsError("Invalid email or password")
        
        self._reset_failed_attempts(user)
        user.last_login = datetime.utcnow()
        
        return self._create_token(user)

    def logout(self, token: str) -> bool:
        if token in self._tokens:
            del self._tokens[token]
            return True
        return False

    def validate_token(self, token: str) -> User:
        auth_token = self._tokens.get(token)
        
        if auth_token is None:
            raise AuthError("Invalid token")
        
        if datetime.utcnow() > auth_token.expires_at:
            del self._tokens[token]
            raise TokenExpiredError("Token has expired")
        
        return self._users[auth_token.user_id]

    def change_password(self, user_id: str, old_password: str, new_password: str) -> bool:
        user = self._users.get(user_id)
        
        if user is None:
            raise AuthError("User not found")
        
        if not self._verify_password(old_password, user.password_hash):
            raise InvalidCredentialsError("Current password is incorrect")
        
        validation_errors = self._password_validator.validate(new_password)
        if validation_errors:
            raise AuthError(f"Invalid password: {', '.join(validation_errors)}")
        
        user.password_hash = self._hash_password(new_password)
        return True

    def _find_user_by_email(self, email: str) -> Optional[User]:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def _is_account_locked(self, user: User) -> bool:
        if user.locked_until is None:
            return False
        return datetime.utcnow() < user.locked_until

    def _record_failed_attempt(self, user: User) -> None:
        user.failed_attempts += 1
        if user.failed_attempts >= self.MAX_FAILED_ATTEMPTS:
            user.locked_until = datetime.utcnow() + timedelta(
                minutes=self.LOCKOUT_DURATION_MINUTES
            )

    def _reset_failed_attempts(self, user: User) -> None:
        user.failed_attempts = 0
        user.locked_until = None

    def _create_token(self, user: User) -> AuthToken:
        token = AuthToken(
            token=secrets.token_urlsafe(32),
            user_id=user.id,
            expires_at=datetime.utcnow() + timedelta(hours=self.TOKEN_EXPIRY_HOURS),
            created_at=datetime.utcnow()
        )
        self._tokens[token.token] = token
        return token


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)
