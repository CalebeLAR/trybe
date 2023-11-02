import typing


def connection_url(self: typing.Any) -> None:
    a = f"{self.dialect}://{self.user}:"
    b = f"{self.password}@{self.host}:"
    c = f"{self.port}/{self.database}"
    self.connections_url = a + b + c


class DataBase:
    """Creates a Database instance

    Parameters
    ----------
    dialect : str
    user : str
    host : str
    password : str
    database : str
    port : str | int, optional, by default None

    >>> db = DataBase('dialect', 'user', 'host', 'pass', 'db', 30.20)
    Traceback (most recent call last):
    ...
    ValueError: `port` must have a numeric value
    >>> db = DataBase('mysql', 'user', 'host', 'pass', 'db')
    >>> print(db.connections_url)
    mysql://user:pass@host:3306/db
    >>> db = DataBase('mysql', 'user', 'host', 'pass', 'db',3308)
    >>> print(db.connections_url)
    mysql://user:pass@host:3308/db
    >>> db = DataBase('postgresql', 'user', 'host', 'pass', 'db')
    >>> print(db.connections_url)
    postgresql://user:pass@host:4000/db
    >>> db = DataBase('postgresql', 'user', 'host', 'pass', 'db', 1222)
    >>> print(db.connections_url)
    postgresql://user:pass@host:1222/db
    >>> db = DataBase('another_db', 'user', 'host', 'pass', 'db')
    Traceback (most recent call last):
    ...
    ValueError: invalid default `port` for unrecognized `dialect`
    >>> db = DataBase('another_db', 'user', 'host', 'pass', 'db', 2345)
    >>> print(db.connections_url)
    another_db://user:pass@host:2345/db
    """

    def __new__(cls: typing.Any, *args: typing.Any) -> typing.Any:
        return object.__new__(cls)

    def __init__(
        self,
        dialect: str,
        user: str,
        host: str,
        password: str,
        database: str,
        port: int | str = "",
    ) -> None:
        self.dialect = dialect
        self.user = user
        self.host = host
        self.password = password
        self.database = database

        is_str = isinstance(port, str)
        is_int = isinstance(port, int)

        if not is_str and not is_int and port != "":
            raise ValueError("`port` must have a numeric value")

        is_mysql = self.dialect == "mysql"
        is_postegresql = self.dialect == "postgresql"

        if not is_mysql and not is_postegresql and port == "":
            raise ValueError(
                "invalid default `port` for unrecognized `dialect`"
            )

        if is_mysql and port == "":
            self.port = 3306
        if is_postegresql and port == "":
            self.port = 4000
        if port != "":
            self.port = int(port)

        connection_url(self)

        # pylance type checking mode
