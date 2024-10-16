## book_class.py

A script that defines a Book class, utilizing Python magic methods to enhance its functionality. This class models a book with attributes for the title, author, and publication year, and incorporates constructors, destructors, and representation methods to provide a comprehensive representation of a book.

## library_system.py

A script that defines a library system, utilizing inheritance and composition to model different types of books. This system consists of a base class Book and two derived classes, EBook and PrintBook, which inherit from Book, as well as a Library class that manages a collection of books through composition.

## polymorphism_demo.py

A script that demonstrates polymorphism in Python by defining a base class Shape and two derived classes, Rectangle and Circle. The Shape class includes an area() method that raises a NotImplementedError, enforcing derived classes to implement their own area calculations. The Rectangle class overrides the area() method to compute its area using the formula length × width, while the Circle class implements its own area() method to calculate the area using the formula π × radius², utilizing the math module for accurate π representation. This structure highlights method overriding and polymorphic behavior in action.

## class_static_methods_demo.py

A script that demonstrates the use of class methods and static methods in Python, showcasing their differences and practical applications through a Calculator class. This class includes a static method for addition and a class method for multiplication, highlighting when and how to utilize the @staticmethod and @classmethod decorators.