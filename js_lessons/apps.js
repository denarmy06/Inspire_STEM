// Data types:

/*   // Multiline comment in java script
1.String
2.Integers/Numbers
3.Booleans
4.Arrays
5.Object
*/

let name = "Mike";
let height = 50


//Onclick events
//Element selector in javascript
function submit(){
    var input = document.getElementById("inputfield").value;
    var input = parseInt(input);   //Data type conversion
    var input = input + 1
    //console.log(input)
}


let adult = true; //Boolean data type
let fruit = ['kiwi', 'pineapple', 'apple', 30, false] //Array
let person = {
    Firstname: 'Ada',
    Lastname: 'Lovelace',
    age: 18,
    address: {
        country: 'Sudan',
        city: 'Khartoum',
        street: 'Bani bani',
    },
    children: ['Kelly', 'Mary']
}

function saveitem(){
    var input = document.getElementById("inputfield").value
    localStorage.setItem('inputfield', item);
    showWelcomeMessage(input)
}

function showWelcomeMessage(input){
    var messageElement = document.getElementById("showMessage")
    messageElement.textContent = "We have saved your input as "+ input;
}

var storedItem = localStorage.getItem("inputfield");
if(storedItem){
    showWelcomeMessage(saveitem)
}


//console.log(person.children[1])
//console.log(typeof(person))


//console.log(typeof(fruit))
//console.log(typeof(height))




