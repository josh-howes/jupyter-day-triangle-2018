""" Simple example of a REPL

A simple program that takes user inputs, executes them,
and returns the result.  This is about as simple a read-eval-print-loop (REPL)
can get. Made for educational purposes only.
"""
if __name__ == '__main__':
    while True:
        code = input(">>> ")
        result = exec(code)
