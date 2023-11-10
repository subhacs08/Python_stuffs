class Student:

    def __init__(self, name: str, batchId: int, universityName: str):
        self.name = name
        self.batchId = batchId
        self.universityName = universityName

    def updateBatchId(self, newBatchId:int):
        self.batchId = newBatchId

class Studentchild(Student):

    def __init__(self):
        super().__init__("John", 1, "MIT")
        print("We are inside Child class constructor ...")
        print(self.name)  # Just to check if name is John as we assigned just above


def mainpublicmembers():
        student1 = Student(name="James", batchId=3, universityName="MIT")
        print(student1.name)
        print("Before changing Batch Id")
        print(student1.batchId)
        student1.updateBatchId(newBatchId=4)
        print("After changing Batch Id")
        print(student1.batchId)
        student2 = Studentchild()
        print(student2.name)
        print(student2.batchId)
        print(student2.universityName)
