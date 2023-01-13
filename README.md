# Cmput404
Question 1：https://github.com/ZhiyuanYu133

Question 2：2.28.1

Question 3：2.28.2

Question 4：
Under a virtual environment, separate directory on the system were created where it will install its own versions of Python ( with any packages installed as well). This allows people to have different versions of Python installed on one machine without interfering with each other.
But in a non-virtual environment, since we are using the global Python installation and its packages, that any changes you make to the packages will affect all projects that use that global installation.

Question 5：
301 Moved Permanently;
https://www.google.com 

Question 6:
For “curl http://www.google.com/teapot”, the status code is 301 Moved Permanently, It is the one returned by "curl -i http://google.com/teapot” However, the command “curl -iL http://google.com/teapot” return both 301 Moved Permanently and 418 I'm a Teapot.
When we "curl http://www.google.com/teapot", the server will respond with an HTTP status code of 418 I'm a teapot.

Question 7:
The“curl -i https://webdocs.cs.ualberta.ca/~hindle1/1.py ” will return the script file content, but “curl -i -X POST -d "X=Y" https://webdocs.cs.ualberta.ca/~hindle1/1.py” will not return the script file content, it will return the response from the script which is handling the POST request.


Question8: https://raw.githubusercontent.com/ZhiyuanYu133/Cmput404/main/print.py
