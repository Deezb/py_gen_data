text = """def evaluate(x):
    x = 21
    if x >= 10 and x <= 20:
        x = x + 5
    else:
        x = x * 6
    if x > 25 :
        y = 2 * x + 7
    else:
        y = 3 * x + 2
    return y
"""


text2 = """x = 7
import textfile
def xy():
    pass

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
"""