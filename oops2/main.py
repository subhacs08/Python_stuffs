from publicMembers import mainpublicmembers
from protectedMembers import mainprotectedmembers
from privateMembers import mainprivatemembers
from gettersetter import maingettersetter
from referencetoself import mainreferencetoself
from reftoself import mainreftoself
from super import mainsuper
from constructors import mainconstructor
from destructor import maindestructor

if __name__ == '__main__':
    print("Demonstrating Public members....")
    mainpublicmembers()
    print("\nDemonstrating  Protected members ...")
    mainprotectedmembers()
    print("\nDemonstrating Private members ...")
    mainprivatemembers()
    print("\nDemonstrating Getter Setter Method ...")
    maingettersetter()
    print("\nDemonstrating reference to Self ...")
    mainreferencetoself()
    print("\nDemonstrating reference to Self ...")
    mainreftoself()
    print("\nDemonstrating Super Class ...")
    mainsuper()
    print("\nDemonstrating Constructor ...")
    mainconstructor()
    print("\nDemonstrating Destructor ...")
    maindestructor()


"""
public members : Access to everything in python
protected members : Access to everything in python
private members : can only be accessed by the same class methods internally (indirectly)
"""

