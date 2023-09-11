def compose(f,g):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h