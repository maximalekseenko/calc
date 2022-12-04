# **Calculator, based on custon engine**

---

## **That the is this**
This project is a proof-of-concept of my [engine project](https://github.com/maximalekseenko/pygame-based-engine) by creating a simple calculator.

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