# Dictionary CLI
 Extremely simple python program to find the definitions of words in the command line

## Requirements
 Because it's so simple, requirements are minimal. All that is needed is Python 3 and the Requests library.
 
 ```
git clone https://github.com/CamJW101/Dictionary-CLI
cd Dictionary-CLI
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install python3-pip python3
pip3 install -r requirements.txt
```

## Usage
 To use the program, you can execute it locally:
 
 ```./dictionary.py [word to define]```
 
 ## Installation
 Or, you can install it and add it to your path to run from anywhere by following these commands.
 
 ```
mkdir -p ~/bin
cp dictionary.py ~/bin/dictionary
chmod +x ~/bin/dictionary
export PATH=$PATH":$HOME/bin"
 ```
