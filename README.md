# mrMonosCli

It's an public package published on PyPi: https://pypi.org/project/mrMonosCli/

## How to install 

On Windows use command:

`pip install mrMonosCli`

It will download lastest package version.

On Linux/MacOS use:

`$ pip3 install mrMonosCli`

## Docs

It is a very simple package.
It has only one build-in function you can (and should) use.

`add_func_to_reg()`

This function make yourself defined function available to call from CLI.

Arguments in order:
- command (str) => It will be available point to your function 
- function (func) => It is yourself defined function what code is executing on command ***It have to be without parentheses*** 
- description (str) => This will be showing on help command 
- **optional** Arguments (bool) => It informs about arguments existing (***Do not include "self" arg***)
- **optional** Number of arguments (int) => It informs about number of arguments (***Do not include "self" arg***)

It also have two parameters of main class:

`prompt` and `intro`

`Promtp` is showing on start of every line where you type command (default: CMD>)

`Intro` is showing when you start program (default: Welcome in CMD!)


## Example

      from mcli import main
      class MyCMD(main.CMD):
          def greet(self,name):
              print(f"Hello {name}!")
          def __init__(self):
              super().__init__()
              self.add_func_to_reg("greet",self.greet,"Shows greeting",True,1)
      MyCMD().main_loop()

Start it. 
### Output
      Welcome in CMD!
      CMD>
      
Type `greet John`.

### Output
      Welcome in CMD!
      CMD>greet John
      Hello John!
      
Then type `greet John|greet Steve`.
### Output
      CMD>greet John|greet Steve
      Hello John!
      Hello Steve!
You can also type `help greet`.
### Output
      CMD>help greet
      Shows greeting
      CMD>
# Version book:
- ## 0.1.0
  Package has been released.
- ## 0.1.1
  Some bugs have been fixed.
- ## 0.1.2 (Current)
  Some bugs have been fixed.
- ## 0.2.0 (In work)
