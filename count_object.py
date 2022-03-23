class ObjCount:
    """taking count as static variable coz for counting all object created we can have one class level variable """
    count = 0

    def __init__(self):
        ObjCount.count += 1

    """We can change the static variable by class method"""

    @classmethod
    def getNumberOfObjects(cls):
        print('Number of objects created till now: ', cls.count)


ObjCount.getNumberOfObjects()
obj = ObjCount()
obj1 = ObjCount()
obj3 = ObjCount()
print(obj1.count)
ObjCount.getNumberOfObjects()
