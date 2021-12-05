class Root:
    def __init__(self, x = 0, y = 0):
        self.x=x
        self.y=y

rt = Root()

print(rt.__dict__)
print(rt.x, rt.y)
rt = Root(1, 1)
print(rt.__dict__)

