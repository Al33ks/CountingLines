# About:
This script is a simple command-line tool that counts the number of lines in the specified files. It is written in Python and can be run from the terminal with the python command.

To use the script, pass the names of the files you want to count the lines of as command-line arguments. The script will open each file, read it line by line, and keep a count of the number of lines. When it has finished reading all of the files, it will print the total count of lines to the console.
# Walkthrough
This line imports the sys module, which provides access to functions and variables used or maintained by the interpreter.
<pre>
<code>import sys </code></pre>

This defines a function called count_lines that takes a list of filenames as an argument. The function sets a count to 0 and then iterates through each filename in the list. It opens each file and reads it line by line, incrementing the count by 1 for each line. Finally, the function returns the total count of lines.
<pre><code>
def count_lines(filenames):
  count = 0
  for filename in filenames:
    with open(filename) as f:
      for line in f:
        count += 1
  return count
</code></pre>
This line sets the variable filenames to a list of the command-line arguments passed to the script, except for the first one (which is the name of the script itself).
<pre><code>filenames = sys.argv[1:]</code></pre>
This calls the count_lines function with the filenames list and prints the returned result to the console.
<pre>
<code>print(count_lines(filenames))</code>
</pre>

# How to run this program?
<pre><code>python line_counter.py file1.txt file2.txt</code>
</pre>

# Example
For example, if file1.txt contains the following text:
<pre>
Hello, world!
This is a test.
</pre>
And file2.txt contains the following text:
<pre>
This is another test.
</pre>
Results:<br>
<img src="https://media.discordapp.net/attachments/930566500643905556/1059863387875573860/image.png"/>
# Notes
<li>This script requires Python 3 to run.</li>
<li>The script assumes that the specified files exist and can be read.</li>
<li>The script does not handle any exceptions that may occur while reading the files.</li>
