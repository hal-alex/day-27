# def add(*args):
#     return sum(args)
#
# print(add(1,2,3,4))

def calculate(**kwargs):
    print(kwargs)
    sum = kwargs["add"] + kwargs["multiply"]
    print(sum)

calculate(add=3, multiply=5)