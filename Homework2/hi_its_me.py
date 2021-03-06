
def dec_for_its_me(str):
    def wrapped():
        return str() + ",it's me!"
    return wrapped
def dec_for_us(fn):
    def wrapped():       
        return "<u> " + fn() + " </u>"
    return wrapped
@dec_for_us
@dec_for_its_me
def hi():
    return "Hi"

print(hi())