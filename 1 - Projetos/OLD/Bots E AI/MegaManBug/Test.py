Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============================== RESTART: C:\Users\marlo\OneDrive\Documentos\GitHub\Scripts-Marlon-Backup\Projetos\MegaManBug\Test.py ==============================
test
1

=============================== RESTART: C:\Users\marlo\OneDrive\Documentos\GitHub\Scripts-Marlon-Backup\Projetos\MegaManBug\Test.py ==============================
test
'12+32'
test2
'this=this'

=============================== RESTART: C:\Users\marlo\OneDrive\Documentos\GitHub\Scripts-Marlon-Backup\Projetos\MegaManBug\Test.py ==============================
Traceback (most recent call last):
  File "C:\Users\marlo\OneDrive\Documentos\GitHub\Scripts-Marlon-Backup\Projetos\MegaManBug\Test.py", line 9, in <module>
    test2=this=this
NameError: name 'this' is not defined
import json
json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
from io import StringIO
io = StringIO()
json.dump(['streaming API'],io)
io.getvalue()
'["streaming API"]'
