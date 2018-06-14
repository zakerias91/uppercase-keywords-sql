# Uppercase keywords in a SQL file
This package uppercases keywords in a SQL file.

## Keywords.txt
Words that appear in keywords.txt will be converted to uppercase in the SQL file. For example: ```select,from,where``` in keywords.txt will convert:

```
select * from test where testid = 1
```

to

```
SELECT * FROM test WHERE testid = 1
```

Please note that a comma is used as the delimiter.

## Instructions
Please ensure Python is installed on your machine. Python does not come prepackaged with Windows.

Save the uppercase_keywords.py file in a directory alongside the SQL file you wish to uppercase. Then open a PowerShell or Command Prompt window in this location.

To run the script enter:

```
python uppercase_keywords.py yoursqlfile.sql
```
This will create an .UPPERCASE file in your directory with the original SQL filename.
