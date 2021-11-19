# Copied from clickhouse_sqlalchemy/drivers/http/exceptions.py
class HTTPException(Exception):
    code = None


# Copied from clickhouse_sqlalchemy/drivers/http/exceptions.py
class DatabaseException(Exception):
    def __init__(self, orig):
        self.orig = orig
        super(DatabaseException, self).__init__(orig)

    def __str__(self):
        text = 'Orig exception: {}'.format(self.orig)

        return compat.text_type(text)