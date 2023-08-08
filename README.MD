# Pythonisms

>1.Decorators:

Decorators in Python are a way to modify or extend the behavior of functions or methods without changing their core code. They use the @decorator_name syntax and usually take a function as an input, returning a modified version of that function. This allows you to add functionality like logging, timing, or authentication to functions while keeping their original structure intact.

>2.Dunder Methods (__len__):

Dunder methods, also known as magic or special methods, are pre-defined method names in Python classes that allow you to customize how objects behave in various situations. For example, the __len__ dunder method is used to define the behavior of the len() function when called on an object. By implementing these methods, you can make your custom classes work seamlessly with built-in Python functions and operators.

> 3.Generators:

Generators are a way to create iterators in Python using a special kind of function. Instead of returning a value and stopping, generators yield a value each time they're called, maintaining their internal state. This allows you to generate and iterate over large sequences of values without needing to store them all in memory, making generators efficient for processing large datasets or infinite sequences.