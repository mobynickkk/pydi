# PyDI
Dependency injection lib for python


# How to use

To define the classes that should be injected and stored as bean use decorator `@component`

    @component
    class A:  # A instance will be created and stored in
        pass


    @component
    class B:
        a: A  # In this case an instance of A will be chosen from context and injected in B


    @component
    class C:
        b: B

        def __init__(self, a: A):  # And here an instance of A will also be chosen from context and injected in B, but created manually
            self.b = B() 
            self.b.a = a
            
 
 Then build the dependency grap using command `build_dependency_graph`
 
