const randomnumbers = Math.floor(Math.random() * 100) +1;
let attempt = 0;
console.log(randomnumbers)

function checkGuess(){
    const guess = parseInt(document.getElementById("guessfield").value)
    attempt++;
    if(isNaN(guess) || guess <1 || guess >100){
        setMessage("Please enter a valid number between 1 and 100")
        return;
    }
    if(guess === randomnumbers){
        setMessage("Congragulations! You won an Iphone")
        document.getElementById("guessfield").disabled = true;
    }else if(guess < randomnumbers){
        setMessage("Too low. Try again")
        return;
    }else{
        setMessage("Too high. Try again")
        return;
    }
}
function setMessage(message){
    document.getElementById("message").textContent = message
}

