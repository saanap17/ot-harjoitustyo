class Level:
    """Class that specifies all possible levels."""

    def check_level(self, experience):
        """Returns level and points required for the next level."""
        if experience < 50:
            return ('Beginner', 50)
        elif experience < 100:
            return ('Novice', 100)
        elif experience < 200:
            return ('Experienced', 200)
        else:
            return ('Master', 0)
