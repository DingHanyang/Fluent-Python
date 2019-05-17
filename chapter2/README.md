# Chapter2

1. 解释一下 ```__iadd__``` 和```__add__```的区别
   += 背后的特殊方法是  ```__iadd__```（用于“就地加法”）。但是如果一个类没有实现这个方 法的话，Python 会退一步调用 ```__add__```。

   ```python
   >>> a+=b
   ```

   如果 a 实现了  ```__iadd__``` 方法，就会调用这个方法。同时对可变序列（例如 list、bytearray 和 array.array）来说，a 会就地改动，就像调用了 a.extend(b) 一样。但是如果 a 没有实现  ```__iadd__```的话，a += b 这个表达式的效果就变得跟 a = a + b 一样了：首先计算 a + b，得到一个新的对象，然后赋值给 a。也就是说，在这个表 达式中，变量名会不会被关联到新的对象，完全取决于这个类型有没有实现  ```__iadd__``` 这 个方法。

2. 一个谜题

   ```python
   >>> t = (1, 2, [30, 40])
   >>> t[2] += [50, 60] 
   Traceback (most recent call last):  
   	File "<stdin>", line 1, in <module> 
   TypeError: 'tuple' object does not support item assignment 
   >>> t (1, 2, [30, 40, 50, 60])
   ```

   - 不要把可变对象放在元组里面。
   - 增量赋值不是一个原子操作。我们刚才也看到了，它虽然抛出了异常，但还是完成了 操作
   - 查看 Python 的字节码并不难，而且它对我们了解代码背后的运行机制很有帮助

3. ```sorted()```和```sort()``` 的区别
4. python内置排序方法（timesort）的工作原理





