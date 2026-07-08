#creating a first tuple
#unline list, we use () - parenthesis
coordinates = (28.14587, 30.458756)
print('coordinates', coordinates)
print('type(coordinates)', type(coordinates))

#trying to modify the coordinate
# coordinates[0] = None #ERROR: tuple does not support assignment operation-----immutable datatype

#creating an empty tuple
empty = ()
print('type(empty): ', type(empty))

#creating single element tuple
single=(3,)
print('type(sinle): ', type(single))

#Concept: Tuple Packing/Unpacking
setError = 'errEmail', 'errUsername', 'errPassword' #packing
print('setError (packing): ', setError)

#Unpacking Operation
errOne, errTwo, errThree = setError
print(f'errOne: {errOne}, errTwo: {errTwo}, errThree: {errThree}')

#Perform indexing (positive/negative)
print(f"setError[0] = {setError[0]}")
print(f"setError[2] = {setError[2]}")
print(f"setError[-2] = {setError[-2]}")

#Perform slicing in tuple
print(f"setError[0:2] = {setError[0:2]}")
print(f"setError[::] = {setError[::]}")