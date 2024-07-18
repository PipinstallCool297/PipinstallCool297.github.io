// function info (myname,age,city) {
//     console.log(myname, "aged", age, "years in", city)
// }
// myname = prompt("What is your name?")
// age = prompt("How old are you?")
// city = prompt("Where do you live?")
// info(myname,age,city)

// function mean (one, two, three, four) {
//     console.log("The mean of all four numbers is ",(one+two+three+four)/4)
// }
// one = Number(prompt("Give me a number."))
// two = Number(prompt("Give me another number."))
// three = Number(prompt("Give me another number."))
// four = Number(prompt("Give me another number."))
// mean(one, two, three, four)

// function reverse (word) {
//     letters = word.length
//     myword=[]
//     for (let i = 0; i <= letters; i+=1) {
//         letter = word[i]
//         myword.push(letter)
//         console.log(letter) }
//     myworc.reverse()
//     console.log(mywrod.join(''))
// }
// word = prompt("Give me a word.")
// reverse(word)

// function alphabetical (word) {
//     letters = word.length
//     myword=[]
//     for (let i = 0; i <= letters; i+=1) {
//         letter = word[i]
//         myword.push(letter)
//         console.log(letter) }
//     myword.sort()
//     console.log(myword.join(''))
// }
// word = prompt("Give me a word.")
// alphabetical(word)

// function asterik (rows, collums) {
//     collums_list=[]
//     for (let j = 1; j <=collums; j+=1) {
//         collums_list.push('*')
//     }
//     for (let i = 1; i <=rows; i+=1) {
//         console.log(collums_list.join(''))
//     }
// }
// rows = Number(prompt("How many rows would you like?"))
// collums = Number(prompt("How many collums would you like?"))
// asterik(rows,collums)

// friends = {
//     'Chloe': 'Sandwich',
//     'Jenny': 'Pasta',
//     'Taylor': 'Toast',
//     'Claire': 'Mac and Cheese',
//     'Jane': 'Ice-Cream'
// };
// for (friend in friends) {
//     console.log(friend)
//     console.log(friends[friend])
// }

// items = {
//     'Strawberries': '$5',
//     'Olive Oil': '$7',
//     'Potatoes': '$3',
//     'Bread': '$4',
//     'Bellpepper': '$2'
// };
// console.log('The available items are:');
// for (item in items) {
//     console.log(item)
// };
// want = prompt("Which item would you like?");
// if (want in items) {
//     console.log("The price of that would be",items[want])
// }
// else {
//     console.log("It looks like that item isn't available right now. Please try somewhere else!")
// }

// function square (length) {
//     area = length*length;
//     console.log("The area is",area);
// };
// function rectangle (length,width) {
//     area = length*width;
//     console.log("The area is",area);
// };
// function triangle (base,height) {
//     area=base*height/2;
//     console.log("The area is",area);
// };
// formulas = {
//     squareformula: square,
//     rectformula: rectangle,
//     triformula: triangle
// };

// one = {
//     'email': 'chloed@gmail.com',
//     'password': 'chloed!',
//     'first': 'Chloe',
//     'last': 'Dorrez'
// };
// two = {
//     'email': 'taylorc@gmail.com',
//     'password': 'taylorc!',
//     'first': 'Taylor',
//     'last': 'Cross'
// };
// three = {
//     'email': 'jennyj@gmail.com',
//     'password': 'jennyj!',
//     'first': 'Jennifer',
//     'last': 'Jackson'
// };
// four = {
//     'email': 'claireq@gmail.com',
//     'password': 'claireq!',
//     'first': 'Claire',
//     'last': 'Quinsy'
// };
// users=[one,two,three,four];
// emailone = ''
// passwordone = ''
// email=prompt("What is your email?")
// password=prompt("What is your password?")
// console.log(email,password)
// for (let i = 0; i < users.length; i+=1) {
//     if (email === users[i]['email']) {
//         if (password === users[i]['password']) {
//             console.log("Login succesful")
//             console.log("Hello,",users[i]['first'],'',users[i]['last'])
//             passwordone=''
//             emailone=''
//             break;
//         }
//         else {
//             passwordone = 'incorrect'
//         }
//     }
//     else {
//         emailone = 'incorrect'
//     }
// }
// if (passwordone === 'incorrect') {
//     console.log('Incorrect password')
// }
// if (emailone === 'incorrect') {
//     console.log ('Incorrect information')
// }

// myBirthday = new Date(2012,1,19)
// today = new Date()
// difference = today-myBirthday
// hours = difference/60000/60
// console.log("It's been",hours/24,"days since you were born.")

console.log(getDate(19))