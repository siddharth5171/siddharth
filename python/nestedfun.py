def outer_function(outer):
    def inner_function(inner):
        return outer + inner
    inner_result = inner_function(5)
    print(inner_result)  # Output: 15
outer_function(10)