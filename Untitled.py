Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> ================================ RESTART ================================
>>> 
file read
>>> print desc

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print desc
NameError: name 'desc' is not defined
>>> ================================ RESTART ================================
>>> 
file read
[u'daddy af \U0001f629\U0001f32e', u'drugs']
>>> ================================ RESTART ================================
>>> 
file read
[u'daddy af \U0001f629\U0001f32e', u'drugs']

Traceback (most recent call last):
  File "/Users/jennywong/fun/venmo_analysis.py", line 18, in <module>
    readVenmo()
  File "/Users/jennywong/fun/venmo_analysis.py", line 15, in readVenmo
    if desc.contains('\U0001f629'):
AttributeError: 'list' object has no attribute 'contains'
>>> ================================ RESTART ================================
>>> 
file read
[u'daddy af \U0001f629\U0001f32e', u'drugs']

Traceback (most recent call last):
  File "/Users/jennywong/fun/venmo_analysis.py", line 19, in <module>
    readVenmo()
  File "/Users/jennywong/fun/venmo_analysis.py", line 16, in readVenmo
    if d.contains('\U0001f629'):
AttributeError: 'unicode' object has no attribute 'contains'
>>> u= unicode('daddy af \U0001f629\U0001f32e', 'utf-8')
