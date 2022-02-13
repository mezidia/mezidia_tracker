from passlib.context import CryptContext


class Hash:
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def bcrypt(cls, password: str) -> str:
        """
        Method for bcrypting the password
        :param password: user password
        :return: hashed password
        """
        hashed_password = cls.pwd_context.hash(password)
        return hashed_password

    @classmethod
    def verify(cls, hashed_password: str, plain_password: str) -> bool:
        """
        Method to verify user password and hashed password
        :param hashed_password: hashed password from database
        :param plain_password: user password
        :return: result of verifying
        """
        return cls.pwd_context.verify(plain_password, hashed_password)
