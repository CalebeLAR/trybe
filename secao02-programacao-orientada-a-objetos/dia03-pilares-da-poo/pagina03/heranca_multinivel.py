class C:  # C
    def x(self):  # método de exemplo
        print(1)


class B(C):  # B herda de C
    def x(self):  # método de exemplo
        print(2)
        pass


class A(B):  # A herda de B
    pass


a = A()
a.x()
# 1


class A(B, C):  #
    pass
