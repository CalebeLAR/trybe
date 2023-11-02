class C:  # C
    def x(self):  # método de exemplo
        print(1)


class B(C):  # B herda de C
    def x(self):  # método de exemplo
        print(2)
        pass


class A(B, C):  #
    pass


a = A()
a.x()
# 1
