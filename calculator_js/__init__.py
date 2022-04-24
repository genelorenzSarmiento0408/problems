import check50

@check50.check()
def exists():
    """Calculator.js exists"""
    check50.exists("calculator.js")

@check50.check(exists)
def add2and2():
    """Add: 2+3 is equal to 5"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("+")
    calculator.stdin("2")
    calculator.stdin("3")
    calculator.stdout("5")

@check50.check(exists)
def add_decimals():
    """Add: Can add decimals"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("+")
    calculator.stdin("2.1")
    calculator.stdin("2.2")
    calculator.stdout("4.3")


@check50.check(exists)
def add_large_num():
    """Add: Can add large numbers"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("+")
    calculator.stdin("56484446464898")
    calculator.stdin("6564984644")
    calculator.stdout("56491011449542")

@check50.check(exists)
def sub2and2():
    """Subtract: 3-2 is equal to 1"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("-")
    calculator.stdin("3")
    calculator.stdin("2")
    calculator.stdout("1")

@check50.check(exists)
def sub_decimals():
    """Subtract: Can subtract decimals"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("-")
    calculator.stdin("2.2")
    calculator.stdin("2.1")
    calculator.stdout("[0?].1", regex=True)


@check50.check(exists)
def sub_large_num():
    """Subract: Can subtract large numbers"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("-")
    calculator.stdin("56484446464898")
    calculator.stdin("6564984644")
    calculator.stdout("56477881480254")

@check50.check(exists)
def mult6and6():
    """Multipy: 6 and 6 is equal to 36"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("*")
    calculator.stdin("6")
    calculator.stdin("6")
    calculator.stdout("36")

@check50.check(exists)
def mult_large_num():
    """Multipy: Can multiply large numbers"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("*")
    calculator.stdin("6565430")
    calculator.stdin("2561651")
    calculator.stdout("16818340324930")

@check50.check(exists)
def divide_whole():
    """Divide: 6 and 6 is equal to 1"""
    calculator = check50.run("node calculator.js")
    calculator.stdin("/")
    calculator.stdin("6")
    calculator.stdin("6")
    calculator.stdout("1")