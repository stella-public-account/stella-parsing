
# Practical Coding Exercise - Automation Developer  
 
Thank you for applying to join the Stella team! This test is designed to give us an idea on your programming skills, the way you approach development, application testing and your attention to detail. 

## Instructions  
 
Complete the exercise given below then archive your completed exercise in a zip, tar.bz2 or tar.gz format and submit by email to Emapta for inclusion with your other details. 

Questions must be submitted via Emapta and will be responded to as soon as possible. 

## The Exercise 
 
The goal of the exercise is to develop a python module to run a command on a remote server and parse the output using TextFSM or any library of your choice. 

### Environment:

* Code must be written for Python version 3.8.10 using PEP8 standards and formatting.
* Feel free to use any editor of your choice.

### Setup:

* Clone this git repository: https://gitlab.reivernet.com/recruitment/stella-parsing.git
* Install the requirements in `requirements.txt` using `pip`

### Script must be able to do following tasks:

1. Run this command on the remote server and capture the output: `top -bn1`
2. Parse the captured output using TextFSM or similar python library.
3. Display the complete parsed output. Hint: use list or dictionaries.
4. Display the PIDs of top 3 longest running processes.

### Notes:

* Commit changes regularly with meaningful commit messages during your development.
* Ensure the `.git` directory is included in your archive file for submission. 
* Update the README.md file in the base directory of the project to explains how to run the module.
* Use comments as you would in a production codebase maintained by a wider team. 

