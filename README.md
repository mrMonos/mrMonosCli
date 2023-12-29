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

This function make function available to call from CLI.

Arguments in order:
- command (str) => It will be available point to function 
- function (func) => It is function what code execute on command ***It have to be without parentheses*** 
- description (str) => This will be showing on help command 
- **optional** Arguments (bool) => It informs about arguments existing 
- **optional** Number of arguments (int) => It informs about number of arguments 

It also have two parameters of class:

`prompt` and `intro`

`Promtp` is showing on start of every line where you type command (default: CMD>)

`Intro` is showing when you start program (default: Welcome in CMD!)


## Example

      from main import CMD
      class MyCMD(CMD):
        def greet(self,name):
          print(f"Hello {name}!")
        def __init__(self):
            super().__init__()
            self.add_func_to_reg("greet",self.greet,"Shows greeting",True,1)

Start it. Type `greet John`.

### Output
      Welcome in CMD!
      CMD>greet John
      Hello John!
      CMD>help greet
      Shows greeting
      CMD>
