This repo contains tasks for Javascript objects, scopes and closures 
Lessons from the project:

class {class name} --> This is used to create a class.

constructor ({arguments}) --> This is used to create a constructor(s) in a class.

this.{constructor argument} --> This is used to initialize an attribute of a class 

const {class name or alias} = require('{executable file housing the class}') --> this is used to import a class

module.exports = {class name} --> This is used to export a class that has been created

class {child class} extends {parent class or alias} --> this is used for inheritance

super({arguments}) --> this is used to call the constructor of the parent class

{list name}.unshift() --> this function is used to place elements at the 0 index of a list, thereby shifting the rest of the elements.

{list name}.map() --> this is used to apply an expression over all elements of a list and possibly assign the new results to a new list

'try' and 'catch' --> they work like the try and except in python. Try attempts to run a code and if an error occurs, the catch block handles the error depending on what the coder wants.

const fs = require('fs').promises --> this imports the 'fs' module and saves it in the object fs. The fs module is responsible for handling operations involving the host machine.

await readFile({file name}) --> reads content of a file and possibly stores them in an object

await writeFile({file name}, {content to write}) --> this is a function that creates a new file and stores a content to it
