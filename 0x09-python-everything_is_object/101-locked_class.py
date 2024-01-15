class LockedClass:
    __slots__ = ["first_name"]  # Restrict allowed attributes

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)  # Allow setting 'first_name'
