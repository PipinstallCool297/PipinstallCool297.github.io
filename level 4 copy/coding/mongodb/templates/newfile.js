const value1 = prompt('Give me a numerical value.');
const value2 = prompt('Give me another numerical value.');
const value3 = prompt('Give me one more numerical value.');
if (value1>value2 and value1>value3) {
    console.log(value1)
}
else if (value2>value1 and value2>value3) {
    console.log(value2)
} else {
    console.log(value3)
}