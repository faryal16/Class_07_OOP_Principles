# quiz_data.py

quiz_data = {
    'Functions': [
        {
            'question': 'What is the output of this code: def greet(name): return f"Hello, {name}"\nprint(greet("Ali"))',
            'options': ['a) Hello', 'b) Hello, name', 'c) Hello, Ali', 'd) Error'],
            'answer': 'c) Hello, Ali'
        },
        {
            'question': 'What does the following code do: def add(a, b=5): return a + b\nprint(add(3))',
            'options': ['a) Adds 3 and 5', 'b) Adds a and b', 'c) Error', 'd) Subtracts a and b'],
            'answer': 'a) Adds 3 and 5'
        },
        {
            'question': 'What is the output of this code: def multiply(x, y): return x * y\nprint(multiply(2, 3))',
            'options': ['a) 5', 'b) 6', 'c) Error', 'd) 23'],
            'answer': 'b) 6'
        },
        {
            'question': 'Which of the following is a valid lambda function?',
            'options': ['a) lambda x: x+1', 'b) lambda x, y: return x+y', 'c) def lambda x: x+1', 'd) lambda: x+1'],
            'answer': 'a) lambda x: x+1'
        },
        {
            'question': 'How would you call a function defined as: def func(*args)?',
            'options': ['a) func()', 'b) func(1, 2, 3)', 'c) func(*args)', 'd) func(1, 2, 3, 4)'],
            'answer': 'b) func(1, 2, 3)'
        },
        {
            'question': 'Which function is used to get the number of arguments passed to a function?',
            'options': ['a) len()', 'b) count()', 'c) args()', 'd) len(args)'],
            'answer': 'd) len(args)'
        },
        {
            'question': 'What is the output of this code: def foo(a, b=3, c=4): return a + b + c\nprint(foo(1))',
            'options': ['a) 8', 'b) 7', 'c) 9', 'd) Error'],
            'answer': 'a) 8'
        },
        {
            'question': 'Which of the following is not a valid function declaration?',
            'options': ['a) def foo():', 'b) def foo(a, b=2):', 'c) def foo(*args):', 'd) def foo[]'],
            'answer': 'd) def foo[]'
        },
        {
            'question': 'What is the output of this code: def func(x, y=2): return x + y\nprint(func(3, 4))',
            'options': ['a) 7', 'b) 6', 'c) Error', 'd) None'],
            'answer': 'a) 7'
        },
        {
            'question': 'How do you specify a default argument in Python?',
            'options': ['a) def func(a=1)', 'b) def func(a: int = 1)', 'c) def func(a => 1)', 'd) def func(a, b=1)'],
            'answer': 'a) def func(a=1)'
        }
    ],
    'Loops': [
        {
            'question': 'Which of the following is the correct syntax for a while loop in Python?',
            'options': ['a) for i in range(5):', 'b) while i < 5:', 'c) loop while i < 5:', 'd) while (i < 5)'],
            'answer': 'b) while i < 5:'
        },
        {
            'question': 'How can you break out of a loop in Python?',
            'options': ['a) stop', 'b) end', 'c) break', 'd) exit'],
            'answer': 'c) break'
        },
        {
            'question': 'Which of the following is an infinite loop?',
            'options': ['a) while True:', 'b) while 1:', 'c) for i in range(10):', 'd) both a and b'],
            'answer': 'd) both a and b'
        },
        {
            'question': 'What does the continue statement do in a loop?',
            'options': ['a) Skips the current iteration', 'b) Exits the loop', 'c) Repeats the loop', 'd) Nothing'],
            'answer': 'a) Skips the current iteration'
        },
        {
            'question': 'What is the output of this code: for i in range(3): print(i) break',
            'options': ['a) 0', 'b) 1', 'c) 2', 'd) 0 1 2'],
            'answer': 'a) 0'
        },
        {
            'question': 'What is the output of this code: for i in range(5): print(i) if i == 3: break',
            'options': ['a) 0 1 2 3', 'b) 0 1 2 3 4', 'c) 0 1 2', 'd) Error'],
            'answer': 'a) 0 1 2 3'
        },
        {
            'question': 'How do you iterate through a list in Python?',
            'options': ['a) for each in list:', 'b) for i in list:', 'c) for i=0 to len(list):', 'd) each(list)'],
            'answer': 'b) for i in list:'
        },
        {
            'question': 'What does the following code do: for i in range(2, 10, 2): print(i)',
            'options': ['a) Prints even numbers from 2 to 10', 'b) Prints odd numbers from 2 to 10', 'c) Prints numbers from 2 to 9', 'd) Prints 2 4 6 8'],
            'answer': 'a) Prints even numbers from 2 to 10'
        },
        {
            'question': 'What is the output of the following code: for x in range(4): print(x * 2)',
            'options': ['a) 0 2 4 6', 'b) 1 2 3 4', 'c) 2 4 6 8', 'd) 0 1 2 3'],
            'answer': 'a) 0 2 4 6'
        },
        {
            'question': 'Which of the following will raise an error?',
            'options': ['a) for i in range(3): print(i)', 'b) while True: break', 'c) for i in range(5, 3, -1): print(i)', 'd) for x in range(1, 5, 0): print(x)'],
            'answer': 'd) for x in range(1, 5, 0): print(x)'
        }
    ],
    'OOP': [
        {
            'question': 'What is the correct way to define a class in Python?',
            'options': ['a) class MyClass:', 'b) def MyClass:', 'c) class MyClass()', 'd) class: MyClass'],
            'answer': 'a) class MyClass:'
        },
        {
            'question': 'Which of the following is true about inheritance in Python?',
            'options': ['a) A class can only inherit from one class', 'b) A class can inherit from multiple classes', 'c) A class cannot inherit from another class', 'd) Inheritance is not supported in Python'],
            'answer': 'b) A class can inherit from multiple classes'
        },
        {
            'question': 'Which function is used to initialize an object in a class?',
            'options': ['a) __init__', 'b) __start__', 'c) __begin__', 'd) __create__'],
            'answer': 'a) __init__'
        },
        {
            'question': 'Which of the following is an example of encapsulation in Python?',
            'options': ['a) Accessing private attributes directly', 'b) Using getters and setters to access attributes', 'c) Inheriting methods from other classes', 'd) None of the above'],
            'answer': 'b) Using getters and setters to access attributes'
        },
        {
            'question': 'Which of the following is true about method overriding?',
            'options': ['a) It allows a subclass to modify a method from its parent class', 'b) It creates a new method in the subclass', 'c) It prevents inheritance', 'd) None of the above'],
            'answer': 'a) It allows a subclass to modify a method from its parent class'
        },
        {
            'question': 'What is the purpose of the self parameter in Python methods?',
            'options': ['a) To refer to the instance of the class', 'b) To refer to the method', 'c) To refer to the global variable', 'd) To define the class name'],
            'answer': 'a) To refer to the instance of the class'
        },
        {
            'question': 'What is the correct way to create an object of a class in Python?',
            'options': ['a) object = Class()', 'b) object = new Class()', 'c) object = create Class()', 'd) Class() = object'],
            'answer': 'a) object = Class()'
        },
        {
            'question': 'Which of the following statements about polymorphism is true?',
            'options': ['a) A method behaves differently based on the object', 'b) Polymorphism is not supported in Python', 'c) Polymorphism prevents inheritance', 'd) Polymorphism is the same as encapsulation'],
            'answer': 'a) A method behaves differently based on the object'
        },
        {
            'question': 'What does the super() function do?',
            'options': ['a) Calls the method from the parent class', 'b) Calls the method from the child class', 'c) Creates a new class', 'd) Initializes the object'],
            'answer': 'a) Calls the method from the parent class'
        },
        {
            'question': 'Which of the following is the correct syntax to define a class variable?',
            'options': ['a) self.variable', 'b) class.variable', 'c) variable', 'd) object.variable'],
            'answer': 'b) class.variable'
        }
    ],
    'Lists': [
        {
            'question': 'What is the correct syntax to create a list in Python?',
            'options': ['a) list = ()', 'b) list = []', 'c) list = {}', 'd) list = list()'],
            'answer': 'b) list = []'
        },
        {
            'question': 'Which method is used to add an element to a list?',
            'options': ['a) append()', 'b) add()', 'c) insert()', 'd) extend()'],
            'answer': 'a) append()'
        },
        {
            'question': 'Which of the following is used to access the last item in a list?',
            'options': ['a) list[0]', 'b) list[-1]', 'c) list[1]', 'd) list[2]'],
            'answer': 'b) list[-1]'
        },
        {
            'question': 'Which method is used to remove an item from a list?',
            'options': ['a) remove()', 'b) delete()', 'c) pop()', 'd) All of the above'],
            'answer': 'd) All of the above'
        },
        {
            'question': 'How can you sort a list in ascending order?',
            'options': ['a) list.sort()', 'b) sorted(list)', 'c) list.order()', 'd) sort(list)'],
            'answer': 'a) list.sort()'
        },
        {
            'question': 'How do you slice a list to get a sublist from index 1 to 3?',
            'options': ['a) list[1:3]', 'b) list[1, 3]', 'c) list[1..3]', 'd) list.slice(1, 3)'],
            'answer': 'a) list[1:3]'
        },
        {
            'question': 'What will the following code return: len([1, 2, 3, 4])?',
            'options': ['a) 3', 'b) 4', 'c) Error', 'd) None'],
            'answer': 'b) 4'
        },
        {
            'question': 'How do you concatenate two lists in Python?',
            'options': ['a) list1 + list2', 'b) list1.append(list2)', 'c) list1.insert(list2)', 'd) list1.extend(list2)'],
            'answer': 'a) list1 + list2'
        },
        {
            'question': 'What is the correct way to create a list of lists?',
            'options': ['a) [[1, 2], [3, 4]]', 'b) [1, 2, [3, 4]]', 'c) Both a and b', 'd) list[[1, 2], [3, 4]]'],
            'answer': 'c) Both a and b'
        },
        {
            'question': 'Which method removes all elements from a list?',
            'options': ['a) clear()', 'b) remove()', 'c) reset()', 'd) delete()'],
            'answer': 'a) clear()'
        }
    ],
     
    'Data Types': [
        {
            'question': 'Which of the following is a mutable data type in Python?',
            'options': ['a) tuple', 'b) list', 'c) string', 'd) int'],
            'answer': 'b) list'
        },
        {
            'question': 'What is the output of the following code: a = [1, 2, 3]; a[0] = 4\nprint(a)?',
            'options': ['a) [4, 2, 3]', 'b) [1, 2, 3]', 'c) Error', 'd) None'],
            'answer': 'a) [4, 2, 3]'
        },
        {
            'question': 'Which of the following data types are immutable in Python?',
            'options': ['a) list', 'b) dictionary', 'c) tuple', 'd) set'],
            'answer': 'c) tuple'
        },
        {
            'question': 'What will the following code output: x = 10\nx = "string"\nprint(type(x))?',
            'options': ['a) <class \'int\'>', 'b) <class \'str\'>', 'c) <class \'float\'>', 'd) <class \'bool\'>'],
            'answer': 'b) <class \'str\'>'
        },
        {
            'question': 'Which method is used to add an element at the end of a tuple?',
            'options': ['a) append()', 'b) insert()', 'c) add()', 'd) tuple is immutable'],
            'answer': 'd) tuple is immutable'
        },
        {
            'question': 'Which of the following will raise an error?',
            'options': ['a) x = 1 + 2.0', 'b) x = "Hello" + 1', 'c) x = 2 * 3', 'd) x = [1, 2] + [3, 4]'],
            'answer': 'b) x = "Hello" + 1'
        },
        {
            'question': 'What is the type of the following: isinstance([1, 2, 3], list)?',
            'options': ['a) bool', 'b) list', 'c) int', 'd) None'],
            'answer': 'a) bool'
        },
        {
            'question': 'Which of the following statements about dictionaries is true?',
            'options': ['a) Dictionaries are ordered', 'b) Keys in a dictionary must be unique', 'c) Values in a dictionary must be unique', 'd) Both a and b'],
            'answer': 'd) Both a and b'
        },
        {
            'question': 'What is the default value for an integer variable in Python?',
            'options': ['a) 0', 'b) None', 'c) Error', 'd) False'],
            'answer': 'a) 0'
        },
        {
            'question': 'What is the result of this expression: 5 // 2?',
            'options': ['a) 2', 'b) 2.5', 'c) 1', 'd) 5'],
            'answer': 'a) 2'
        }
    ],
    'Tuples': [
        {
            'question': 'Which of the following is the correct way to define a tuple in Python?',
            'options': ['a) tuple = []', 'b) tuple = ()', 'c) tuple = {}', 'd) tuple = tuple()'],
            'answer': 'b) tuple = ()'
        },
        {
            'question': 'Which of the following operations can you perform on a tuple?',
            'options': ['a) Add elements', 'b) Remove elements', 'c) Concatenate with another tuple', 'd) Modify elements'],
            'answer': 'c) Concatenate with another tuple'
        },
        {
            'question': 'What will the following code output: t = (1, 2, 3)\nt[1] = 4?',
            'options': ['a) (1, 4, 3)', 'b) (1, 2, 4)', 'c) (1, 2, 3, 4)', 'd) Error'],
            'answer': 'd) Error'
        },
        {
            'question': 'Which of the following methods is available for tuples?',
            'options': ['a) append()', 'b) insert()', 'c) pop()', 'd) count()'],
            'answer': 'd) count()'
        },
        {
            'question': 'What is the output of the following code: t = (1, 2, 3)\nlen(t)?',
            'options': ['a) 1', 'b) 2', 'c) 3', 'd) Error'],
            'answer': 'c) 3'
        },
        {
            'question': 'How do you access the second item of a tuple t = (5, 10, 15)?',
            'options': ['a) t[1]', 'b) t(2)', 'c) t{1}', 'd) t[2]'],
            'answer': 'a) t[1]'
        },
        {
            'question': 'What does the following code output: t = (10, 20, 30, 40)\nprint(t[-2])?',
            'options': ['a) 20', 'b) 30', 'c) 40', 'd) 10'],
            'answer': 'b) 30'
        },
        {
            'question': 'What will the following code output: t = (1, 2, 3)\nprint(t * 2)?',
            'options': ['a) (1, 2, 3, 1, 2, 3)', 'b) (1, 1, 2, 2, 3, 3)', 'c) (1, 2, 3)', 'd) Error'],
            'answer': 'a) (1, 2, 3, 1, 2, 3)'
        },
        {
            'question': 'Which of the following is true about tuples?',
            'options': ['a) Tuples are immutable', 'b) Tuples can have duplicate elements', 'c) Tuples can be nested', 'd) All of the above'],
            'answer': 'd) All of the above'
        },
        {
            'question': 'Which of the following methods can be used to convert a tuple to a list?',
            'options': ['a) list()', 'b) tuple()', 'c) set()', 'd) dict()'],
            'answer': 'a) list()'
        }
    ],
     'Sets': [
        {
            'question': 'Which of the following is the correct way to define a set in Python?',
            'options': ['a) set = []', 'b) set = ()', 'c) set = {}', 'd) set = set()'],
            'answer': 'd) set = set()'
        },
        {
            'question': 'What is the output of the following code: s = {1, 2, 3}\ns.add(4)\nprint(s)?',
            'options': ['a) {1, 2, 3}', 'b) {1, 2, 3, 4}', 'c) Error', 'd) {4, 1, 2, 3}'],
            'answer': 'b) {1, 2, 3, 4}'
        },
        {
            'question': 'Which of the following operations can be performed on a set?',
            'options': ['a) Add an element', 'b) Remove an element', 'c) Perform set union', 'd) All of the above'],
            'answer': 'd) All of the above'
        },
        {
            'question': 'Which of the following methods is used to remove an element from a set?',
            'options': ['a) remove()', 'b) discard()', 'c) pop()', 'd) All of the above'],
            'answer': 'd) All of the above'
        },
        {
            'question': 'What will the following code output: s = {1, 2, 3, 4}\ns.remove(2)\nprint(s)?',
            'options': ['a) {1, 3, 4}', 'b) {1, 2, 3, 4}', 'c) Error', 'd) {3, 4}'],
            'answer': 'a) {1, 3, 4}'
        },
        {
            'question': 'Which of the following is true about sets in Python?',
            'options': ['a) Sets are ordered collections', 'b) Sets cannot contain duplicate elements', 'c) Sets are mutable and immutable at the same time', 'd) Sets allow indexing'],
            'answer': 'b) Sets cannot contain duplicate elements'
        },
        {
            'question': 'What is the result of this operation: s = {1, 2, 3} + {4, 5, 6}?',
            'options': ['a) {1, 2, 3, 4, 5, 6}', 'b) Error', 'c) {1, 2, 3, {4, 5, 6}}', 'd) None'],
            'answer': 'b) Error'
        },
        {
            'question': 'Which of the following methods is used to return the intersection of two sets?',
            'options': ['a) intersection()', 'b) union()', 'c) diff()', 'd) append()'],
            'answer': 'a) intersection()'
        },
        {
            'question': 'What is the output of the following code: s1 = {1, 2, 3}; s2 = {3, 4, 5}\ns1 & s2?',
            'options': ['a) {3}', 'b) {1, 2, 3, 4, 5}', 'c) {1, 2}', 'd) Error'],
            'answer': 'a) {3}'
        },
        {
            'question': 'What is the output of the following code: s = {1, 2, 3}\ns.pop()\nprint(s)?',
            'options': ['a) {1, 2}', 'b) {2, 3}', 'c) Error', 'd) {3, 1}'],
            'answer': 'a) {1, 2}'
        }
    ],
      'Dictionaries': [
        {
            'question': 'Which of the following is the correct way to define a dictionary in Python?',
            'options': ['a) dict = []', 'b) dict = {}', 'c) dict = ()', 'd) dict = dict()'],
            'answer': 'b) dict = {}'
        },
        {
            'question': 'Which of the following methods can be used to add a new key-value pair to a dictionary?',
            'options': ['a) append()', 'b) add()', 'c) insert()', 'd) key assignment'],
            'answer': 'd) key assignment'
        },
        {
            'question': 'What is the output of the following code: d = {"a": 1, "b": 2}\nd["c"] = 3\nprint(d)?',
            'options': ['a) {"a": 1, "b": 2, "c": 3}', 'b) {"a": 1, "b": 2}', 'c) Error', 'd) {"a": 1, "b": 2, "c": "3"}'],
            'answer': 'a) {"a": 1, "b": 2, "c": 3}'
        },
        {
            'question': 'Which method is used to get the value for a key in a dictionary?',
            'options': ['a) get()', 'b) fetch()', 'c) getValue()', 'd) value()'],
            'answer': 'a) get()'
        },
        {
            'question': 'What does the following code output: d = {"a": 1, "b": 2}\nprint(d.get("c"))?',
            'options': ['a) None', 'b) Error', 'c) "c"', 'd) "key not found"'],
            'answer': 'a) None'
        },
        {
            'question': 'Which of the following methods is used to remove a key-value pair from a dictionary?',
            'options': ['a) remove()', 'b) del()', 'c) pop()', 'd) All of the above'],
            'answer': 'd) All of the above'
        },
        {
            'question': 'Which of the following is the correct way to iterate over the keys of a dictionary?',
            'options': ['a) for k in dict:', 'b) for k in dict.keys():', 'c) for k in dict.values():', 'd) for k in dict.items():'],
            'answer': 'b) for k in dict.keys():'
        },
        {
            'question': 'What will the following code output: d = {"a": 1, "b": 2}\nd.pop("a")\nprint(d)?',
            'options': ['a) {"b": 2}', 'b) {"a": 1, "b": 2}', 'c) {"b": 2, "a": 1}', 'd) Error'],
            'answer': 'a) {"b": 2}'
        },
        {
            'question': 'Which of the following will raise an error?',
            'options': ['a) d = {"a": 1, "b": 2}; d["c"]', 'b) d = {}; d["a"] = 3', 'c) d = {"a": 1, "b": 2}; d["a"] = 4', 'd) None of the above'],
            'answer': 'd) None of the above'
        }
    ],
      'Error Handling': [
        {
            'question': 'What is the purpose of the `try` block in Python?',
            'options': ['a) To handle exceptions', 'b) To execute code without errors', 'c) To define a function', 'd) To catch exceptions'],
            'answer': 'a) To handle exceptions'
        },
        {
            'question': 'What will the following code output: try:\n   x = 1 / 0\nexcept ZeroDivisionError:\n   print("Error")\nelse:\n   print("No error")',
            'options': ['a) Error', 'b) No error', 'c) Error followed by No error', 'd) SyntaxError'],
            'answer': 'a) Error'
        },
        {
            'question': 'What is the purpose of the `else` block in error handling?',
            'options': ['a) It is executed when no exception occurs', 'b) It is executed when an exception occurs', 'c) It is executed to catch errors', 'd) None of the above'],
            'answer': 'a) It is executed when no exception occurs'
        },
        {
            'question': 'What will the following code output: try:\n   x = 1 / 0\nexcept ZeroDivisionError:\n   print("Cannot divide by zero")\nfinally:\n   print("This will always execute")',
            'options': ['a) Cannot divide by zero', 'b) Cannot divide by zero followed by This will always execute', 'c) Error', 'd) This will always execute'],
            'answer': 'b) Cannot divide by zero followed by This will always execute'
        },
        {
            'question': 'Which of the following exceptions is handled by the `except` block?',
            'options': ['a) SyntaxError', 'b) IndexError', 'c) TypeError', 'd) All of the above'],
            'answer': 'd) All of the above'
        },
        {
            'question': 'What will the following code output: try:\n   print(1)\nexcept TypeError:\n   print(2)\nelse:\n   print(3)',
            'options': ['a) 1', 'b) 2', 'c) 3', 'd) Error'],
            'answer': 'a) 1'
        },
        {
            'question': 'What is the purpose of the `finally` block in error handling?',
            'options': ['a) It is executed regardless of whether an exception occurred or not', 'b) It is executed only when an exception occurs', 'c) It is executed to catch errors', 'd) It is executed to raise exceptions'],
            'answer': 'a) It is executed regardless of whether an exception occurred or not'
        },
        {
            'question': 'What will the following code output: try:\n   x = 1 / "a"\nexcept ValueError:\n   print("Value error")\nexcept TypeError:\n   print("Type error")',
            'options': ['a) Value error', 'b) Type error', 'c) Error', 'd) None'],
            'answer': 'b) Type error'
        },
        {
            'question': 'What is the result of the following code: try:\n   y = 5\nexcept ZeroDivisionError:\n   print("Zero division")\nelse:\n   print("No error")',
            'options': ['a) No error', 'b) Zero division', 'c) Error', 'd) None'],
            'answer': 'a) No error'
        },
        {
            'question': 'Which of the following is used to raise an exception in Python?',
            'options': ['a) raise', 'b) except', 'c) try', 'd) finally'],
            'answer': 'a) raise'
        }
    ]

}
