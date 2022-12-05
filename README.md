# **Calculator, based on custon engine**

## **That the is this**
Core idea of this project is to practice in project development.

This project is an application, that immitates calculator.

Base of this application is [pygame based engine](https://github.com/maximalekseenko/pygame-based-engine).

---

# Installation
For running thip program you will need:
 - [python 3.10+](http://python.org)
 - [pygame 2.1+](http://pygame.org)
 - [git](https://git-scm.com) or [zip with this project](https://github.com/maximalekseenko/calc)

Run this program by simply running '`run.py`' with your [python interpritator](http://python.org).

---

# **Interface**
Interface is easily seperated on two parts:
- [Output](#output) - Located at top of the screen and used for witnessing your input or program output.
- [Input](#input) - Located at bottom of the screen and used to manipulate with this program.

---

## **Output**
One of two major parts of [interface](#interface) (the other one is [input](#input)). It occupies the top third of the screen and used for witnessing what you have inputed or what was outputed as a result of your operations.

Output consists of single element:
- [display](#display) - line of symbols, that can be found at right side of the output.

> ### Display
> Single line of symbols that represents current input or output.
>
> Display touches the right side of the screen, but can go out of the left.
> 
> If Display is not present, it is becouse it is empty.
>
> Display is located at right side of the [output](#output). 

---

## **Input**
Input is the second major part of the [interface](#interface). located at the lower two third of the screen. It contans matrix of buttons. Used for translating your request manualy by operating with your mouse. It is valueable to notice ability to input by [keyboard](#keyboard-input).

**Input** consists of 20 buttons that are located in [numpad](#numpad).

> ### **Numpad**
> 5x4 numpad with buttons.
>
> Used for manupulating with this program.
> 
> #### Numpad layout:
> |                            |                            |                               |                               |
> |----------------------------|----------------------------|-------------------------------|-------------------------------|
> | [AC](#button-with-ac)      | [BS](#button-with-bs)      | [%](#buttons-with-operations) | [/](#buttons-with-operations) |
> | [7](#buttons-with-numbers) | [8](#buttons-with-numbers) | [9](#buttons-with-numbers)    | [*](#buttons-with-operations) |
> | [4](#buttons-with-numbers) | [5](#buttons-with-numbers) | [6](#buttons-with-numbers)    | [-](#buttons-with-operations) |
> | [1](#buttons-with-numbers) | [2](#buttons-with-numbers) | [3](#buttons-with-numbers)    | [+](#buttons-with-operations) |
> | [OFF](#button-with-off)    | [0](#buttons-with-numbers) | [.](#button-with-a-dot)       | [=](#button-with-equal)       |

> ### **Buttons with numbers**
> Ten rectangular buttons that spells a number (e.g. '`0`', '`1`', '`2`', ect.).
>
> By pressing one of this buttons, corresponding number will be added to the left of [display](#display).
>
> Buttons with numbers are located in [numpad](#numpad-layout)

> ### **Button with a dot**
> Single rectangular button that spells '`.`'. 
>
> By pressing this button, `.` symbol will be added to the left of [display](#display). Used to manipulate with fractional numbers.
>
> Button with a dot is located in [numpad](#numpad-layout).

> ### **Buttons with operations**
> Five rectangular button that spells one of the baisic operations (e.g. '`%`', '`/`', '`+`'). 
>
> By pressing any of such buttons, corresponding operaion will be added to the [display](#display).
>
> Legacy of this buttons:
> - '`%`' - modulo.
> - '`/`' - division (tip: type twice to get an integer division).
> - '`*`' - multyplication.
> - '`-`' - subtraction.
> - '`+`' - addition

> ### **Button with equal**
> Single rectangular button that spells '`=`'. 
>
> By pressing this button, line of symbols in the [display](#display) will be replaced with a result of previously inputed operations(s).
>
> Button with a dot is located in [numpad](#numpad-layout).

> ### **Button with AC**
> Single rectangular button that spells '`AC`'. 
>
> By pressing this button, whole line of symbols in [display](#display) will be erased.
>
> Button with AC is located in [numpad](#numpad-layout).

> ### **Button with BS**
> Single rectangular button that spells '`BS`'. 
>
> By pressing this button, last symbol in [display](#display) will be removed.
>
> Button with BS is located in [numpad](#numpad-layout).
>
> Buttons with operations is located in [numpad](#numpad-layout).

> ### **Button with OFF**
> Single rectangular button that spells '`OFF`'. 
>
> By pressing this button, application will be quited.
>
> Button with OFF is located in [numpad](#numpad-layout).

> ### **Button with ANS**
> Single rectangular button that spells '`ANS`'. 
>
> By pressing this button, last calculation result will be added to the [display](#display). If no calculations were made yet, '`0`' will be added instead.
>
> Button with ANS is not impemented on the [numpad](#numpad-layout). Can be used throught [keyboard](#keyboard-input).

> ### **Button with nothing**
> Single rectangular button that spells '` `' (space symbol). 
>
> By pressing this button, '` `' symbol will be added to the [display](#display).
>
> Button with nothing is not impemented on the [numpad](#numpad-layout). Can be used throught [keyboard](#keyboard-input).

---

# **Inner structure**
This project posesses nest structure:
- [engine](#engine) - core of the project.
- [font.ttf](#fontttf) - font.
- [readme.md](#readmemd) - documentation.
- [theatre.py](#theatrepy) - heart of the application.
- [act_main.py](#act_mainpy) - python file with main act.
- [scene_output.py](#scene_outputpy) - python file with [output](#output).
- [scene_input.py](#scene_inputpy) - python file with [input](#input).
- [element_button.py](#element_buttonpy) - buttons.
- [run.py](#runpy) - python file for running this application.

> ### **engine**
> Folder with engine, this project made on.
>
> Source code can be found [here](https://github.com/maximalekseenko/pygame-based-engine).

> ### **font.ttf**
> File, that contains seven segment font.
>
> Used by [display](#display) and [numpad](#numpad).
>
> Source code can be found [here](https://www.dafont.com/seven-segment.font).
>
> Readed by [theatre](#theatrepy) upon initilization.

> ### **readme.md**
> File with documentation for this project.
>
> Used for understanding how to use this application and how it works.
>
> Beginig can be found [here](#calculator-based-on-custon-engine).

> ### **theatre.py**
> Heart of the project.
>
> Contains extended thearte and it's initialization.
>
> Extended theatre has two new variables:
> - `.font` - font, for this programm. Within initialization, reads it from [fontttf](#fontttf).
> - `.colors` - list of colors for program.

> ### **act_main.py**
> This act represents program in open state.
>
> This act withholds next vatiables:
> - `.is_preview` - [is currently shows a result](#clear-the-result).
> - `.line` - [display](#display);
> - `.memory` - [menory](#memory)
>
> This act has two scenes:
> - `.scene_output` - instance of [output scene](#scene_outputpy)
> - `.scene_input` - instance of [input scene](#scene_inputpy)
>
> Initialized and added to the [theatre](#theatrepy) in the [run.py](#runpy)

> ### **scene_output.py**
> Scene for upper part of the screen.
>
> Is implementation of [output](#output).
>
> Used in [main act](#act_mainpy).

> ### **scene_input.py**
> Scene for lower part of the screen.
>
> Is implementation of [input](#input).
> 
> withhold matrix of [buttons](#element_buttonpy) '`.buttons`' as implementation of [numpad](#numpad).
>
> Used in [main act](#act_mainpy).

> ### **element_button.py**
> Buttons.
>
> Is implementation of buttons in [numpad](#numpad-layout).
>
> Matrix of such located in [input scene](#scene_inputpy).

> ### **run.py**
> This is file for running the program
>
> Upon execution initilizes the [theatre](#theatrepy) by `theatre.Begin()`.


---

# **Features**
> ### **Keyboard input**
> Aside of manual input, this program has an ability to input by keyboard.
>
> | Key                                              | Button                                             |
> |--------------------------------------------------|----------------------------------------------------|
> | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` | [buttons with numbers](#buttons-with-numbers)      |
> | `.`                                              | [button with a dot](#button-with-a-dot)            |
> | `%`, `/`, `*`, `-`, `+`                          | [button with operations](#buttons-with-operations) |
> | `=`, `enter`                                     | [button with equal](#button-with-equal)            |
> | `delete`                                         | [button with AC](#button-with-ac)                  |
> | `backspace`                                      | [button with BS](#button-with-bs)                  |
> | `escape`                                         | [button with OFF](#button-with-off)                |
> | `a`                                              | [button with ANS](#button-with-ans)                |
> | `space`                                          | [button with nothing](#button-with-nothing)        |

> ### **Memory**
> After calculation this program saves final result to memory, wich can be accessed by [ANS button](#button-with-ans)

> ### Clear the result
> When calcutaion is [done](#button-with-equal), [display](#display) will preview the result. There is no need of editing the tesult by user, as there is [memory feature](#memory). Upon [adding](#buttons-with-numbers) any new symbol to the display, previewed result eraces at first.

# What this code is protected against
- Pressing [=](#button-with-equal) with incorrect line in [display](#display).
- Pressing [AC](#button-with-ac) when line in display is empty.
- Division by zero.
- Modulo by zero.
- Scaling window to small.
- Scaling window to big.
- Typing two [numbers](#buttons-with-numbers) at the same time.

# Testing log
| № | User action | Expected result | Real result | Comments |
|-|-|-|-|-|
| 1 | Hitting [4](#buttons-with-numbers), when `163+62` in [display](#display) | display shows `163+624` | display shows `163+624` | - |
| 2 | Hitting [=](#button-with-equal), when `163+62` in display | display shows `225` | display shows `225` | - |
| 3 | Hitting [AC](#button-with-ac), when `163+62` in display | display shows ` ` | display shows ` ` | - |
| 4 | Hitting [OFF](#button-with-off), when `163+62` in display | Programm quites | Programm quites | - |
| 5 | Hitting =, when `163+` in display | display shows `&` | Infinity or zero | Division by zero |
| 6 | Hitting wall with your device, when `163+62` in display | display shows ` ` | display shows `163+62` | Technical problems |