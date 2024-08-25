<h1 align="center">filename-cleaner</h1>

## About

Tired of filenames cluttered with unnecessary info like website names or audio quality tags? I wrote this script to clean them up.

## Features

-   Removes substrings in the filename.

-   Processes multiple files.

## Installation

-   You need Python installed.

1.  Clone the repository.
    <br/>` git clone https://github.com/Seryjnyy/python-tools.git`

2.  Navigate to the project directory.
    <br/> `cd filename-cleaner`

## Usage

### Basic usage

1.  Add files you want changing to the folder with the script.

    -   Or add the script to the folder with the files.

        -   Note: I didn't want to accidentally mess up files by getting the path wrong, so it's done this way.

2.  In the terminal, enter `py "substring" "substring2" -ext "extension"`

    -   A substring can be any string you want removing.
    -   -ext is for declaring the extension type of the files.

3.  Please use `py ./main.py -h` for further help.

## Example

```
py ./main.py "-320kbps-" "-128kbps-" "Example.com" "SiteName.com" -ext "mp3"

# Before:
01-Artist-Title-320kbps-Example.com.mp3
02-Artist-Title-128kbps-SiteName.com.mp3

# After:
01-Artist-Title.mp3
02-Artist-Title.mp3
```

## TODO

-   [ ] Custom path support for choosing files outside the folder.
