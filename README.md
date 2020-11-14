# Hebrew Gibberish to UTF-8 Converter
Convert Hebrew gibberish to UTF-8
For example, will convert `ùìåí çðåê` to `שלום חנוך`

## Quick Explanation
Encoding issues have plagued Hebrew filenames for years.<br/>
A quick Python line can convert to the all useful UTF-8:
```python
bytes(gibberish_hebrew_string, "iso-8859-1").decode("windows-1255")
```
The rest of the script simply iterates over files and subdirectories and converts the names recursively.

## Usage:
    > python gib2u.py TARGET
target can be a file or a folder
