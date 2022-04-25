import check50
import check50.c

@check50.check()
def exists():
    """The program and text-pointer.c exists"""
    check50.exists("text-pointer.c")
    check50.exists("text-pointer")

@check50.check(exists)
def compiles():
    """text-pointer.c compiles"""
    check50.c.compile("text-pointer.c", lcs50=True)

@check50.check(compiles)
def valgrind_check():
    """No memory errors"""
    check50.c.valgrind("./text-pointer").stdin("Hello world").exit(0)

@check50.check(compiles)
def text_pointer():
    """Prints the text and its pointer"""
    test = check50.run("./text-pointer")
    test.stdin("Hello world")
    test.stdout("The text is Hello world and the pointer is 0x\w{0,32}", regex=True).exit(0)

@check50.check(compiles)
def number_pointer():
    """Can check and print number and its pointers"""
    test = check50.run("./text-pointer")
    test.stdin("84")
    test.stdout("The text is 84 and the pointer is 0x\w{0,32}", regex=True).exit(0)