def partial_apply(func, arg1):
    def partial_func(arg2):
        return func(arg1, arg2)
    return partial_func