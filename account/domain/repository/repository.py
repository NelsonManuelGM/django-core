"""Module to define actions on the database repository"""


class IUserRepository:
    """Abstract class for repository methods"""
    class Meta:
        abstract = True

    def create(self):
        """create abstract method"""
        pass

    def update(self):
        """update abstract method"""
        pass

    def delete(self):
        """delete abstract method"""
        pass

    def select(self):
        """select abstract method"""
        pass
