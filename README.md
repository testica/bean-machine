# Bean Machine Simulator

Simulation of Bean Machine built in pyhton.
## Requisites
* Python v 2.7.x

## Usage
* You have to specify number of levels with flag `-l` (required)
* You have to specify number of balls with flag `-b` (required)
* If you want get the result in percentage, use flag `-p` (optional).

## Example

20 levels and 500 balls are thrown

`python bean_machine.py -l 20 -b 500`

output: `[0, 0, 0, 1, 1, 11, 9, 44, 46, 82, 79, 90, 56, 52, 21, 4, 4, 0, 0, 0, 0]`
(output may be different)

-------------------------------------------------------
10 levels and 800 balls are thrown

`python bean_machine.py -l 10 -b 800 -p`

output: `['0.25%', '0.88%', '3.62%', '10.13%', '20.13%', '24.88%', '22.25%', '14.12%', '2.63%', '1.0%', '0.13%']`
(output may be different)
