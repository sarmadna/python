def main():
    class Employee:
        def __init__(self, first, last):
            self.first = first
            self.last = last
            self.email = self.first + '.' + self.last + '@company.com'
        def full_name(self):
            return "Your name is: {} {}".format(self.first, self.last)
if __name__ == "__main__":
    main()