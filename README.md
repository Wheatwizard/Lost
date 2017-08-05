# Lost

Lost is a 2 dimensional language in which the start location and direction are
entirely random

# Memory

The memory is stored in a stack and a scope.  Both are stacks padded with zeros at the bottom.
At the end of execution the contents of the stack are printed.

Unlike most 2D languages the ip may start in any location moving in any direction.

# Commands

## Mirrors

- `\` Swaps the x and y directions

- `/` Swaps the x and y directions and multiplies them by -1

- `|` Multiplies the horizontal direction by -1

## Directions

- `>` Tells the ip to move east

- `<` Tells the ip to move west

- `v` Tells the ip to move south

- `^` Tells the ip to move north

## Doors

- `[` Reflects the ip if it is moving east; becomes `]` if the ip is moving horizontally

- `]` Reflects the ip if it is moving west; becomes `[` if the ip is moving horizontally

## Jumps

- `!` Skips the next operation

- `?` Pops off the top of the stack and jumps if not zero

## Stack manipulation

- `:` Duplicates the top of the stack

- `$` Swaps the top two items of the stack

- `(` Pops from the stack and pushes to the scope

- `)` Pops from the scope and pushes to the stack

## Literals

- `0`-`9` pushes n to the top of the stack

- `"` Starts and ends a string literal.  During a string literal commands are not run and instead their character values are pushed to the stack.

## Operations

- `+` Adds the top two numbers

- `*` Multiplies the top two numbers

- `-` Multiplies the top by -1

## Control

- `%` Turns the safety off

- `#` Turns the safety on

- `@` Ends execution if the safety is off (starts on)
