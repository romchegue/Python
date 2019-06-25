# File classtools.py
"There are different utilities for working with classes"

class AttrDisplay:
    """
    Implements a hereditary method of overloading an output operation
    that displays the class names of instances and all attributes
    as name = value pairs that exist in instances (excluding attributes
    inherited from classes). I can work with any instances.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def gatherAllAttrs(self):
        attrs = []
        for key, value in self.__class__.__dict__.items():
            if 'function ' + self.__class__.__name__ in str(value):
                attrs.append('%s=%s' % (key, value))
        return ', '.join(attrs)
    def __str__(self):
        return '[%s: %s; [All attrs: %s]]' % (self.__class__.__name__, self.gatherAttrs(), self.gatherAllAttrs())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X) # Will output all attributes of an instance
    print(Y) # Will output a name of the closest class in an inheritance tree
