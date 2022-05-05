[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7796553&assignment_repo_type=AssignmentRepo)
# PY4E_12.1
Assignment
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

For the purposes of this assignment http://data.pr4e.org/intro-short.txt

Modify the socket1.py program to retrieve the above URL and print out the headers and data.  Regarding the displaying of the headers information, most popular packages for HTTP requests will return the headers as a dictionary (key-value format), however, the socket package does not. For the purposes of this assignment, you will also need to leverage your understanding of Python dictionaries in order to create a new dictionary with the correct header key-value pairs you get from the HTTP response and then display those values. This will allow you to become familiar with the typical data format when parsing header information.

Make sure to change the code to retrieve the above URL - the values are different for each URL.

Enter the header values in each of the fields below and press "Submit".

HINT: When trying to parse the header data, you can use a function like splitLines() to split the data into a list so that you can access the individual pieces of data more easily. You can also use whatever other functions make sense for parsing string data as well.
