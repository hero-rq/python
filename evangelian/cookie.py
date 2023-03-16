class Foo():

    def __enter__(self):
        print("I mean...")
        return self

    def __cookie__(self):
        print("okay?")

    def __exit__(self, type, value, traceback):
        print("...and go away.")

      
with Foo() as foo:
  foo.__cookie__()
  print("nice to meet you")
