# 100 Prisoners Problem

The 100 prisoners problem is a mathematical problem in probability theory and combinatorics.

## Description

The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 boxes. The director randomly puts one prisoner's number in each closed box. The prisoners enter the room, one after another. Each prisoner may open and look into 50 boxes in any order. The boxes are closed again afterwards. If, during this search, every prisoner finds his number in one of the boxes, all prisoners are pardoned. If just one prisoner does not find his number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the boxes. What is the prisoners' best strategy?

## Strategies

### No Collusion

Each prisoner randomly chooses 5 boxes.

### Box Hopper

1. Each prisoner first opens the drawer with his own number.
2. If this drawer contains his number he is done and was successful.
3. Otherwise, the drawer contains the number of another prisoner and he next opens the drawer with this number.
4. The prisoner repeats steps 2 and 3 until he finds his own number or has opened half the drawers.

## Program

In the program, first you may pick a strategy for opening the boxes, and then the program runs multiple simulations of the game and records the wins, losses and win rate. You can set the number of games simulated and total number of prisoners in the main method.

You may also uncomment the print statements to see the boxes that each prisoner chooses.