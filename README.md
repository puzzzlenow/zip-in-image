# zip-in-image
Stores compressed file as pure image format.  
It simply works! Tried many similar ways but all failed. So I make my own for attaching zip files in email.  

*Recently my geemail account prompted this error after uploaded file.*
`
Blocked for security reasons!
`
 

## Usage
You may simply right-click on a file to encode/decode file in Windows "SendTo" menu  
Or  
Run the python script source code as below.  
```console
$ python encoder.py [filename]
...
$ python decoder.py [filename that is encoded with .png extension]
...
```

## Example
```console
$ python encoder.py sample-input.tar.gz
Encoding..sample-input.tar.gz
-------------------------------
imported file : sample-input.tar.gz
generated file : sample-input.tar.gz.png
---- FIN ----------------------
```

```console
$ python decoder.py sample-input.tar.gz.png
Decoding..sample-input.tar.gz.png
-------------------------------
decoding img file : sample-input.tar.gz.png
exported file : 20230926-172924.733754-sample-input.tar.gz
---- FIN ----------------------
```

Encoded output png file may look like this:  
![Image](https://raw.githubusercontent.com/puzzzlenow/zip-in-image/main/sample-input.tar.gz.png?token=GHSAT0AAAAAACIDMZK5QME6UBR3D7HW7QUIZITDKZQ)


## Q&A
* Question : I got an error ModuleNotFoundError: No module named 'PIL'
* Answer : You need to install the library. Run this command.
```console
pip install Pillow
```
See more: https://pypi.org/project/Pillow/
