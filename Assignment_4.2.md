
1.Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving
average of the given sequence is defined as follows:
The moving average sequence has n-k+1 elements as shown below.


```python
from collections import deque
import itertools

def moving_average(iterable, n=3):
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable) 
    # create an iterable object from input argument
    d = deque(itertools.islice(it, n-1))  
    # create deque object by slicing iterable
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

# example on how to use it
for i in  moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]):
    print(i)

```

    5.0
    4.666666666666667
    5.666666666666667
    6.666666666666667
    9.666666666666666
    28.666666666666668
    49.333333333333336
    72.66666666666667
    84.0
    93.33333333333333
    116.33333333333333
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
