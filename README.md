-----------------
V  OUT OF DATE  V
-----------------

Methoding and Logic of editing default order parameters without editing everything.

Method 1 - "Lots 'o Work":

  Data is sent to ordering module, defaults are defined in module. The data that is missing is replaced with default.
  
  Advantages:
  
  - Separates user from defaults, keeps the "gold standard" for default parameters tightly under our control
  - Less for the user to write as they only send the parameters that need to be changed (also less chance of them f***ing something up)

  Disadvantages:
  
  - Requires that I know how to edit presets inside modules from the outside...
  - ...or teaching python modules to accept the lack of information as information

Method 2 - "Easy...I think":

  Similar to Method 1 except defaults are stored outside of the order module. The user still just changes or writes the parameters they want changed and sends it to the order module allong with the default.
  
  Advantages:
  
  - Easy to do
  - Good set-up for later more complex interfaces
  - Makes it easier to add new presets as they can be handled outside of the control of both the user and the order module

  Disadvantages:
  
  - User may be tempted (depending on set-up) to edit the defaults. This could be problematic.
  - Possibility for both Logic and Runtime errors as the order module has to decide between the default and the new parameters that the user has set out

Method 3 - "Bad idea":

  Data is rewriten in full by the user the end result is sent to the order module. As long as it is in the same format the order module should just accept it without knowing any better.
  
  Advantages:
  
  - Easy to implement, from what I understand it is the system we currently have
  - Thanks to "control+c" and "control+v" it should be easy for users to edit default values if they were given a template to work from in the accepted code

  Disadvantages:
  
  - Too easy for the user to make a mistake, sifting through >50 lines of parameters and expecting no-one to make a mistake: not happening
  - Could seem too daunting for most users to bother, in other words: could scare them away

Method 4 - "Thinking outside the Program":

  The ordering module has a sub-module for editing the parameters of the order. This means that when they pick a template, say for example a postcard, they then edit where the text on the back should be, if there should be text on the front, size and possition of the photographs, ect.
  
  Advantages:
  
  - Full control over original templates can be controlled externally
  - Great support for a "do it yourself" or "what you see is what you get" interface for a less tech savy user

  Disadvantages:
  
  - Might not work too well for the tech savy app developer (who doesn't affraid of anything) who doesn't want their consumers to edit the designs of their prints
  - May have difficulties adding new parameters to exsisting templates as the program would then become out of date
