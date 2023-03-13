# Dependencies
Software dependencies or system requirements needed to build and run the Docker container.

### NUMPY
NUMPY is a Python library for dealing with mathematics
#### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install NUMPY.
```
pip install numpy
```

# Build instructions
Instructions on how to build the Docker container from the compressed tarball.

+ Extract files from compressed tarball file "Rebekka.tar.gz"

+ Open folder named "Rebekka" in Visual Code Studio

+ Run the command below to build the docker file
```
% docker build -t fibonacci-term .
```
# Run instructions
Instructions on how to run docker file

+ Run the command below to run the docker file
```
% docker run --rm fibonacci-term 2
```
+ The output should be 
```
7
```
+ Change the number at the end of the run command to change the amount of digits
