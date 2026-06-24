import numpy as np
arr=np.array([
    [
        [1,2],
        [2,4]

    ],
    [
        [5,6],
        [7,8]
    ]
])
print(arr[1,1,1])
print(arr[:,1,:])
print(arr[1,:,:])