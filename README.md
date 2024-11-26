# Autopilot
A tool for automating GUI tasks.

# Install
> pip install -r requirements.txt

# Run
### Autopilot mode
_Autopilot mode_ is the default execution mode. It is used for iterating on the provided _xlsx_ data file and 
executing the actions.

To run the application in _Autopilot mode_:
> python autopilot.py --target wazsi
This will execute the actions stored in _./config/actions_wazsi.txt_

*Note:* the execution can be paused and resumed by pressing 'Pause' and ended by pressing 'Esc'.

### Recording mode
Actions can be recorded using the _Recording mode_. When enabled, the application starts to listen.
Clicks - except for the very first one - and delays between them will be recorded into a generated action file, 
so later can be used for execution. Additionally, a step can be _marked for edition_ in the generated action file 
by pressing 'Pause' the moment when the mark is wished to be present.

To run the application in _Recording mode_:
> python autopilot.py --record wazsi
This will record issued clicks, key presses, scrolls, etc, into _./config/actions_wazsi.txt_.

# Configuration
## Basic configuration
Check the example _configuration.txt_ for details. An _xlsx_ data file and an _action_ configuration
to be provided for the _Autopilot mode_. For running the _Recording mode_ no configuration is required.

## Data source
Data can be provided so that it can be copy-pasted during the execution of _Autopilot mode_. The only supported 
format is _xlsx_. The file is expected to contain a _list_ of data, where every row represents *one* iteration of the 
actions - except the very first, which conventionally must constitute a header row, where every cell can be 
used to reference the column below.

Example data set:

name | title | mail
------------ | ------------- | ------------
Mundo | Dr. | doctor@mundo.com
Baley | Detective | baley@earth.com
Solo Han | merch | chubakka@deathstar.com

_In this example, in the first iteration of Autopilot mode will process the row (Mundo, Dr., doctor@mundo.com)._

# Actions
The _Autopilot mode_ executes the actions for each row in the configured _xslx_ file. Configuring different actions is possible 
via an action configuration file, provided in _configuration.txt_. Additionally to actions, the starting row of the 
_xlsx_ file also can be configured in the very first line of the action file.
Example first line:
> repeat from row 1

_Will iterate from the first data row (excluding headers)_.

Example action file:
> repeat from row 3

> click 100 300 left

> copy name

> paste

> click 500 700 left

Different actions are listed below.

## Click
Clicks to a certain coordinate.

property|value
--- | --- 
reference in action file|"click"
parameter 1 | x coordinate
parameter 2 | y coordinate

Example in action file:
> click 100 300

_Will click to x=100, y=300._

## Wait
Waits a given amound of seconds.

property|value
--- | ---
reference in action file | "wait"
parameter 1 | the amount of time in seconds

Example in action file:
> wait 2

_Will wait for 2 seconds._

## Copy
Copies to the clipboard a property of the row of the _xlsx_ data that is currently under iteration.

property|value
| --- | --- |
reference in action file | "copy"
parameter 1 | the target column of the row to be copied

Example:
> copy title

_Copies the title of the row that is currently being used for action execution._

## Paste
Pastes previously copied data.

property|value
| --- | --- |
reference in action file| "paste"

Example:
> paste

_Pastes the copied data._

## Scroll
Scrolls.

property|value
| --- | --- |
reference in action file| "scroll"

Example:
> scroll 3231 263 0 -1

_Puts the cursor at position (3231, 263) and scrolls vertically down._

## Combo
Issues a hotkey command.

property|value
| --- | --- |
reference in action file| "combo"

Example:
> combo ctrl t

_Issues Ctrl+w and opens up a tab if a chrome window is at focus._

## Esc
Issues a hotkey command.

property|value
| --- | --- |
reference in action file| "esc"

Example:
> esc

_Quits the action execution._
