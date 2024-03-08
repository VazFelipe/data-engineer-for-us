//4 + 5 = 9
//4 - 5 = -1
//4 x 5 = 20
//4 / 5 = 0.8

operations = ['+', '-', '*', '/']

function math_operations(num1, num2){
  for (let i = 0;i < 4; i++){
    var calculus = eval(num1.toString() + operations[i] + num2.toString())
    var message = `${num1} ${operations[i]} ${num2} = ${calculus}`
    console.log(message)
  }
}

math_operations(4,5)