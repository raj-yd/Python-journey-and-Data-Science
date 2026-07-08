#lambdaExpression.py

'''

Sometimes, you need a tiny, throwaway function, used once, never again.
In that case, we can use lambda expression with very small definition of a function.
Syntax:

lambda parameters : expression

'''
#Normal Definiton
#def square(x):
# return x**2

#Lambda: Alternative approach
square = lambda x : x**2
#here, square is the name of lambda expression
print(f'Lambda Expression Result: {square(5)}, {square(10)}')

multiply=lambda x,y : x*y
print(multiply(2,3))