# closure
def out_func(n_out):
    def in_func():
        return n_out ** 2
    return in_func

x = out_func(2)
print(type(x))
print(x)
print(x())





# def out_func(n_out):
#     def in_func(n_in):
#         return n_in ** 2
#     return in_func(n_out)
#
# print(out_func(2))
