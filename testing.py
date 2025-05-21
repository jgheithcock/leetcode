"""
Testing framework for leetcode problems.

Usage:

Define `tests` in your file.
`tests` is an array of (parameters to pass), expected.

For running unit tests on first regular instance method of class:

    from testing import runTests
    runTests(Solution, tests)

To run on a specific method:

    from testing import runTests
    method = Solution.intToRomanShort
    runTests(method, tests)

For running timing trials on all regular instance methods:

    from testing import timeTests
    timeTests(Solution, tests) # runs 1000 trials by default
    timeTests(Solution, tests, 1_000_000) # 1,000,000 trials

"""

def runTests(obj, tests):
    if type(obj) == type: # passed in Solution.class
        inst = obj()
        methods = methodsFrom(obj)
        method_name, method = methods[0]
    else:
        inst = obj
        method = obj
        method_name = method.__name__
        
    print(f"Running {len(tests)} tests on {method_name}")
    for test, expected in tests:
        result = method(inst, *test)
        if expected == result:
            print(f"{f"{test}"[:20]}...: Success ({expected})\n")
        else:
            print(f"{f"{test}"[:20]}...: -Fail- - got {result} expected {expected}\n")


import timeit
def timeTests(klass, tests, trials=1000):
    inst = klass()
    methods = methodsFrom(klass)
    for method_name, method in methods:
        t = 0
        for test, _ in tests:
            t += timeit.timeit(lambda: method(inst, *test), number=trials)
    
        print(f"{method_name}: {t:0.3f} seconds ({(t * 1000):.0f} ms) for {trials} trials")

from types import FunctionType
def methodsFrom(k):
    return [
        (n, m)
        for n, m in k.__dict__.items()
        if type(m) == FunctionType and not n.startswith("_")
    ]
