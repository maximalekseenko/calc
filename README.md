# **Calculator, based on custon engine**

## **That the is this**
This is a simple calculator, based on my [engine](https://github.com/maximalekseenko/pygame-based-engine).

It withholds next features:
- [Numpad](#numpad) with 20 unique buttons for you to press on.
- [Display](#display) that shows your current input or result of your calculations.
- [Interface](#interface), that is prepaired for the most extreme screen sizes.
- [Easy way](#memory) for continueous calculatations.

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
Input is the second major part of the [interface](#interface). located at the lower two third of the screen. It contans matrix of buttons. Used for translating your request manualy by operating with your mouse. It is valueable to notice ability to input by [keyboard](#keyboad-input).

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
> Button with ANS is not impemented.

> ### **Button with nothing**
> Single rectangular button that spells '` `' (space symbol). 
>
> By pressing this button, '` `' symbol will be added to the [display](#display).
>
> Button with nothing is not implemented.


---

## **Structure**
Explanation of basic terms can be found [here](https://github.com/maximalekseenko/pygame-based-engine/blob/master/README.md).

> <h3 align="center"> Theatre - theatre </h3>
>
> ---
>
> Defalut **theatre** will be used, as i dont need to save anything globaly.

> <h3 align="center"> Act - Main </h3>
>
> ---
>
> As this is just a calculator, no other **act**s meems to be requaired.
>
> This will contain two **scene**s: one for input; one for output.

> <h3 id="scene_keypad", align="center"> Scene - Keypad </h3>
>
> ---
>
> Input **scene**. Contains buttons with numbers, operations and specal actions(e.g. erace)

> <h3 align="center"> Scene - Screen </h3>
>
> ---
>
> Output **scene**. Contains a row of text to show current input or a final result.

> <h3 align="center"> Element - Button </h3>
>
> ---
>
> **Element** for button in [Keypad **scene**](#scene_keypad). Will have highlight logic.