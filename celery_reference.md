# myapp/tasks.py
from celery import shared_task
@shared_task("my_function")  #The @shared_task decorator lets you create tasks that can be used by any app(s).
@shared_task(name="my_function")
def my_function(a=123, b=None, c=True):
    ...
```
## Running Celery Tasks
```python
from myapp.tasks import my_function
```
*Typical*
```python
my_function(a=456, b="Sweet", c=False)
```
*Celery Shortcut*
```python
my_function.delay(a=456, b="Sweet", c=False)
```