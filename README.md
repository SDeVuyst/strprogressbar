<p align="center"><img src="https://socialify.git.ci/SDeVuyst/strprogressbar/image?description=1&font=Bitter&language=1&name=1&owner=1&pattern=Plus&theme=Dark" alt="project-image"></p>

<p align="center">
<a href='https://github.com/SDeVuyst/strprogressbar/issues'><img src="https://img.shields.io/github/issues/SDeVuyst/strprogressbar.svg"></a>
<a href="https://github.com/SDeVuyst/strprogressbar/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="shields"></a>
</p>

<h1>🚀 Usage</h1>

**_ProgressBar_** has quite a few parameters:
| Parameter name | Mandatory | Type | Description |
| --- | --- | --- | --- |
| `value` | **yes** | int | Current value of the progress bar
| `total` | **yes** | int | Max value of the progress bar
| `string_length` | **yes** | int | Length of the bar
| `unfilled_char` | no | str | char that displays the unfilled portion of the bar. Defaults to "▬".
| `progress_char` | no | str | char that displays the filled portion of the bar. Defaults to "🔘".
| `fill_bar` | no | bool | If the left side of the bar should also be filled. Defaults to False.

<h2>Examples: </h2>


```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 25 characters
# we are in step 67/85
p = ProgressBar(67, 85, 25)
print(p)

>>> "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔘▬▬▬▬▬"
```
```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 20 characters
# we are in step 3/5, change the default characters
# fill in the progress that we already made
p = ProgressBar(3, 5, 20, "░", "▓", True)
print(p)

>>> "▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░"
```
```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 30 characters
# we are in step 8/15, change the default characters
# fill in the progress that we already made with 2 chars
p = ProgressBar(8, 15, 30, "░", "▒▓", True)
print(p)

>>> "▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓░░░░░░░░░░░░░░"
```

<h2>What if we want to show our progress in numbers or in percentage?</h2>

**_ProgressBar_** has 4 default functions to add or remove this feature.

- [add_percentage()](#add_percentage())
- [remove_percentage()](#remove_percentage())
- [add_counter()](#add_counter())
- [remove_counter()](#remove_counter())

Note that adding percentage or counter does not alter the size of the progress bar. eg. If you set `string_length` to 20 and added a percentage indicator, the progress bar will still be 20 chars long, but with the total string will be longer with the percentage sign. 

<h3>add_percentage()</h3>
<h4>Parameters</h4>

| Parameter name | Mandatory | Type | Description |
| --- | --- | --- | --- |
| `decimals` | no | int | The amount of decimals to display. Defaults to 0.
| `left` | no | bool | If the percentage should be displayed to the left of the progress bar. Defaults to False/right side.
| `seperator` | no | str | The seperator between the progress bar and the percentage number. Defaults to " ".

<h4>Example</h4>

```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 25 characters
# we are in step 30/64 and display this on the right side with 2 decimals
p = ProgressBar(30, 64, 25).add_percentage(2, False)
print(p)

>>> "▬▬▬▬▬▬▬▬▬▬▬🔘▬▬▬▬▬▬▬▬▬▬▬▬▬ 46.88%"
    |__________________________|
            25 characters
```

<h3>remove_percentage()</h3>
<h4>Parameters</h4>

*This function has no parameters.*

<h4>Example</h4>

```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 25 characters
# we are in step 30/64 and display this on the right side with 0 decimals
p = ProgressBar(30, 64, 25).add_percentage(0, False, ' @ ')
print(p)
# remove the percentage
print(p.remove_percentage())

>>> "▬▬▬▬▬▬▬▬▬▬▬🔘▬▬▬▬▬▬▬▬▬▬▬▬▬ @ 47%"
>>> "▬▬▬▬▬▬▬▬▬▬▬🔘▬▬▬▬▬▬▬▬▬▬▬▬▬"
```

<h3>add_counter()</h3>
<h4>Parameters</h4>

| Parameter name | Mandatory | Type | Description |
| --- | --- | --- | --- |
| `left` | no | bool | If the percentage should be displayed to the left of the progress bar. Defaults to False/right side.
| `seperator` | no | str |The seperator between the progress bar and the percentage number. Defaults to " "

<h4>Example</h4>

```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 25 characters
# we are in step 67/85 and display this on the left side
p = ProgressBar(67, 85, 25).add_counter(True, " - ")
print(p)

>>> "67/85 - ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔘▬▬▬▬▬"
```
We can also add both a counter and a percentage indicator:
```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 25 characters
# we are in step 67/85 and display this on the left side
# add a percentage indicator on the right side
p = ProgressBar(67, 85, 25).add_counter(True, " - ").add_percentage(1, False, " - ")
print(p)

>>> "67/85 - ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🔘▬▬▬▬▬ - 78.8%"
```

<h3>remove_counter()</h3>
<h4>Parameters</h4>

*This function has no parameters.*

<h4>Example</h4>

```python
from strprogressbar import ProgressBar
# create a progressbar with a width of 25 characters
# we are in step 18/64 and display this on the right side with 0 decimals
p = ProgressBar(18, 64, 25, "░", "▓", True).add_counter(False).add_percentage()
print(p)
# remove the percentage
print(p.remove_counter())

>>> "▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░ 28% 18/64"

>>> "▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░ 28%"
```
  
<br>
<h1>🛠️ Installation Steps:</h1>

<p>1. Installing</p>

```
pip install strprogressbar
```
<br>
<h1>🛡️ License:</h1>

This project is licensed under the GNU General Public License v3.0