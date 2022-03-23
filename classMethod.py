class Bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print(f'{name} can fly with {cls.wings} wings.')


bird1 = Bird()
bird1.fly('crow')
