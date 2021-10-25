# PyDI
Dependency injection lib for python


# How to use

To define the classes that should be injected and stored as bean use decorator `@component`

    @component
    class A:  # A instance will be created and stored in context
        pass


    @component
    class B:
        a: A  # In this case an instance of A will be chosen from context and injected in B


    @component
    class C:
        b: B

        def __init__(self, a: A):  # And here an instance of A will also be chosen from context
            self.b = B()           # and injected in B, but created manually
            self.b.a = a
            
 
Then build the dependency grap using command `build_dependency_graph`
 
After that you can get ready components with `get_component_from_context` function
 
    print(get_component_from_context(C))  # This will print <__main__.C object at 0x0...>
