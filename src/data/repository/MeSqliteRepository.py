from src.data.model.Me import Me


class MeSqliteRepository:

    def __init__(self, session):
        self.session_func = session
        self.session = self.session_func()

    def __enter__(self):
        return self

    def __exit__(self, _type, value, traceback):
        self.session_func.remove()

    def read(self):
        """
        Find the record for me.
        :return: Me
        """
        me = self.session.query(Me).first()
        if me is None:
            me = Me()
            self.session.add(me)
            self.session.flush()
        return me

    def save(self, me: Me):
        """
        Save me!
        :param me: to save
        :return: Me
        """
        if me.id != 1:
            raise ValueError('Your id should always be "1". Use the "read" method to retrieve a Me object.')

        self.session.add(me)
        self.session.flush()
        return me
