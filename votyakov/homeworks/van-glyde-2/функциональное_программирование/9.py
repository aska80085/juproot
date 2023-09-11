def compose_functions(functions):
    def composed_function(arg):
        if len(functions) == 0:
            return arg
        return compose_functions(functions[1:])(functions[0](arg))
    return composed_function