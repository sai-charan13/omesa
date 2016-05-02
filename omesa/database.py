"""Blitzdb database declarations."""

from blitzdb import Document
from blitzdb import FileBackend


class Configuration(Document):
    """Blitzdb configuration placeholder."""

    pass


class Vectorizer(Document):
    """Blitzdb vectorizer placeholder."""

    pass


class Classifier(Document):
    """Blitzdb classifier placeholder."""

    pass


class Results(Document):
    """Blitzdb results placeholder."""

    pass


class Table(Document):
    """Blitzdb table placeholder."""

    pass


class Database(object):
    """Blitzdb database."""

    def __init__(self):
        """Load backend."""
        # TODO: I'm sure the path here can be done neater
        self.db = FileBackend(__file__.split('/database.py')[0] + "/db")

    def save(self, doc):
        """Save document do db."""
        self.db.save(doc)
        self.db.commit()

    def fetch(self, doc, q):
        """Filter and return first entry."""
        try:
            return self.db.filter(doc, q)[0]
        except IndexError:
            print("File does not exist.")

    def getall(self, doc):
        """Returns all entries in db."""
        return [d for d in self.db.filter(doc, {})]