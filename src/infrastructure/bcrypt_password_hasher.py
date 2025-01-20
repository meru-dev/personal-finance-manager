import bcrypt

from src.domain.common.ports.password_hasher import PasswordHasher
from src.domain.user.value_objects import Password, RawPassword


class BcryptPasswordHasher(PasswordHasher):
    def hash(self, raw_password: RawPassword) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(raw_password.encode(), salt)

    def verify(self, raw_password: RawPassword, password: Password) -> bool:
        return bcrypt.checkpw(
            password=raw_password.encode(),
            hashed_password=password,
        )
