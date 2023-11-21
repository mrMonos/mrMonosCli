# CMD-3.0

It's an public package published on PyPi: https://pypi.org/project/CMD-3.0/

# How to install 

On Windows use command:

>pip install CMD-3.0

It will download lastest package version.

On Linux/MacOS use:

>$ pip3 install CMD-3.0

# Docs

It is a very simple package.
It has only one build-in function you can (and should) use.

add_func_to_reg()

This function make function available to call from CLI.

Arguments in order:
- command (alias) => It will be available point to function **str**
- function => It will be function what code execute. ***It have to be without parentheses*** **func**
- description => This will be showing on help command **str**
- **optional** Arguments => Inform about arguments existing **bool**
- **optional** Number of arguments => Inform about arguments amount **int**

# Example

>from main import CMD
>class MyCMD(CMD):
>  def greet(self,name):
>    print(f"Hello {name}")
>  def __init__(self):
>      super().__init__()
>      self.add_func_to_reg("greet",self.greet,"Shows greeting",True,1)
      
