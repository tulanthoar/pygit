class Student:
  def __init__( self, name, age, grade ):
    self.name = name
    self.age = age
    self.grade = grade
  def dispStudent( self ):
    print( astud.name, astud.age, astud.grade )


astud = Student( 'me', 25, 'grad' )
print( astud.name, astud.age, astud.grade )
astud.dispStudent()
print( hasattr( astud, 'grade' ) )
print( hasattr( astud, 'grad' ) )
setattr( astud, 'grade', 'master' )
astud.dispStudent()
delattr( astud, 'age' )
print( hasattr( astud, 'age' ) )

class Parent:
  counter = 10
  def __init__(self):
    'par init'
  def pFun( self ):
    'par fun call'
  def setC( self, n ):
    Parent.counter = n
  def showC( self ):
    print( Parent.counter )

class Child( Parent ):
  def __init__( self ):
    print( 'child init' )
  def childF( self ):
    print( 'childF called' )
  def showC( self ):
    p = Parent()
    p.showC()
    print( 'overridden' )

apar = Parent()
apar.showC()
achild = Child()
print( achild.counter )
achild.setC( 20 )
print( achild.counter )
print( apar.counter )
achild.showC()
