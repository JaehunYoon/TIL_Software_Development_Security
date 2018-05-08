class SimpleTest():
    a = 0
    postfix = "\t DSM"
    def print_with(self, string):
        print(string)
        print(str(self.a) + string + self.postfix)

s1 = SimpleTest()
s2 = SimpleTest()

print(s1.a)
print(s2.a)

s1.a = 10
s2.a = 20

print(s1.a)
print(s2.a)


s1.print_with("h4lo")
s2.print_with("UYBYHGHG")
