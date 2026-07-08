import numpy as np
import time

size=1000000

list=list(range(size))
start=time.time()
result=[ x*2 for x in list]
print(f"List time : {time.time() - start:.4f}")  #method-2 #print("%.4f" % (time.time()-start))
# List time : 0.0939    

#numpy: another approach
start=time.time()
numpy_array=np.arange(size)
numpy_result=numpy_array*2
print(f"Numpy Array Time : {time.time()-start:.4f}")
# Numpy Array Time : 0.0104