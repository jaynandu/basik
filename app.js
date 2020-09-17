var happy = "oui";
console.log(happy);

// ? Arithmetic

// * The main thing to do with numbers is arithmetic. Arithmetic operations such as addition or multiplication take two number values and produce a new number from them. Here is what they look like in JavaScript:

console.log(100 + 4 * 11);
// La reponse c'est 144

// ? The + and * symbols are called operators. The first stands for addition, and the second stands for multiplication. Putting an operator between two values will apply it to those values and produce a new value.

texto = [
  "Down on the sea \n",
  " Lie on the ocean \n",
  " Float on the ocean \n",
];

console.log(texto);

// ? Strings cannot be divided, multiplied, or subtracted, but the + operator can be used on them. It does not add, but it concatenates - it glues two strings together. The following line will produce the string "concatenate":
console.log("con" + "cat" + "e" + "nate");

// ! String values have several associated functions (methods) that can be used to perform other operations on them.

// * Not all operators are symbols. Some are written as words. One example is the typeof operator, which produces a string value naming the type of the value you give it. The other operators that use two values are called unary operators. The minus operator can be used both as a binary operator and as a unary operator.

console.log(typeof 6.7);
console.log(typeof "x");
console.log(-(10 - 2));

// ? COMPARISON

// * The > and < signs are the traditional symbols for "is greater than" and "is less than", respectively. They are binary operators. Applying them results in a  Boolean value that indicates whether they hold true in this case.  Strings can be compared in the same way.

console.log(3 > 2);
// false
console.log(2 < 2);
// false
console.log("Aardvark" < "Zoroaster");
// true

// ! Explantion logic

// Other similar operators are >= (greater than or equal to), <= (less than or equal to), == (equal to), and != (not equal to).

// console.log("Itchy" != "Scratchy") // → true console.log("Apple" == "Orange") // → false

// There is only one value in JavaScript that is not equal to itself, and that is NaN (“not a number”).

// console.log(NaN == NaN) // → false

// NaN is supposed to denote the result of a nonsensical computation, and as such, it isn’t equal to the result of any other nonsensical computations.

// Logical operators

// There are also some operations that can be applied to Boolean values themselves. JavaScript supports three logical operators: and, or, and not. These can be used to “reason” about Booleans.

// The && operator represents logical and. It is a binary operator, and its result is true only if both the values given to it are true.

// console.log(true && false) // → false console.log(true && true) // → true

// The || operator denotes logical or. It produces true if either of the values given to it is true.

// console.log(false || true) // → true console.log(false || false) // → false

// Not is written as an exclamation mark (!). It is a unary operator that flips the value given to it—!true produces false, and !false gives true.

// When mixing these Boolean operators with arithmetic and other operators, it is not always obvious when parentheses are needed. In practice, you can usually get by with knowing that of the operators we have seen so far, || has the lowest precedence, then comes &&, then the comparison operators (>, ==, and so on), and then the rest. This order has been chosen such that, in typical expressions like the following one, as few parentheses as possible are necessary:

// 1 + 1 == 2 && 10 * 10 > 50

// The last logical operator I will discuss is not unary, not binary, but ternary, operating on three values. It is written with a question mark and a colon, like this:

// console.log(true ? 1 : 2); // → 1 console.log(false ? 1 : 2); // → 2

// This one is called the conditional operator (or sometimes just the ternary operator since it is the only such operator in the language). The value on the left of the question mark “picks” which of the other two values will come out. When it is true, it chooses the middle value, and when it is false, it chooses the value on the right.

// Empty values

// There are two special values, written null and undefined, that are used to denote the absence of a meaningful value. They are themselves values, but they carry no information.

// Many operations in the language that don’t produce a meaningful value (you’ll see some later) yield undefined simply because they have to yield some value.

// The difference in meaning between undefined and null is an accident of JavaScript’s design, and it doesn’t matter most of the time. In cases where you actually have to concern yourself with these values, I recommend treating them as mostly interchangeable.

// Automatic type conversion

// In the Introduction, I mentioned that JavaScript goes out of its way to accept almost any program you give it, even programs that do odd things. This is nicely demonstrated by the following expressions:

// console.log(8 * null) // → 0 console.log("5" - 1) // → 4 console.log("5" + 1) // → 51 console.log("five" * 2) // → NaN console.log(false == 0) // → true

// When an operator is applied to the “wrong” type of value, JavaScript will quietly convert that value to the type it needs, using a set of rules that often aren’t what you want or expect. This is called type coercion. The null in the first expression becomes 0, and the "5" in the second expression becomes 5 (from string to number). Yet in the third expression, + tries string concatenation before numeric addition, so the 1 is converted to "1" (from number to string).

// When something that doesn’t map to a number in an obvious way (such as "five" or undefined) is converted to a number, you get the value NaN. Further arithmetic operations on NaN keep producing NaN, so if you find yourself getting one of those in an unexpected place, look for accidental type conversions.

// When comparing values of the same type using ==, the outcome is easy to predict: you should get true when both values are the same, except in the case of NaN. But when the types differ, JavaScript uses a complicated and confusing set of rules to determine what to do. In most cases, it just tries to convert one of the values to the other value’s type. However, when null or undefined occurs on either side of the operator, it produces true only if both sides are one of null or undefined.

// console.log(null == undefined); // → true console.log(null == 0); // → false

// That behavior is often useful. When you want to test whether a value has a real value instead of null or undefined, you can compare it to null with the == (or !=) operator.

// But what if you want to test whether something refers to the precise value false? Expressions like 0 == false and "" == false are also true because of automatic type conversion. When you do not want any type conversions to happen, there are two additional operators: === and !==. The first tests whether a value is precisely equal to the other, and the second tests whether it is not precisely equal. So "" === false is false as expected.

// I recommend using the three-character comparison operators defensively to prevent unexpected type conversions from tripping you up. But when you’re certain the types on both sides will be the same, there is no problem with using the shorter operators.

// Short-circuiting of logical operators

// The logical operators && and || handle values of different types in a peculiar way. They will convert the value on their left side to Boolean type in order to decide what to do, but depending on the operator and the result of that conversion, they will return either the original left-hand value or the right-hand value.

// The || operator, for example, will return the value to its left when that can be converted to true and will return the value on its right otherwise. This has the expected effect when the values are Boolean and does something analogous for values of other types.

// console.log(null || "user") // → user console.log("Agnes" || "user") // → Agnes

// We can use this functionality as a way to fall back on a default value. If you have a value that might be empty, you can put || after it with a replacement value. If the initial value can be converted to false, you’ll get the replacement instead. The rules for converting strings and numbers to Boolean values state that 0, NaN, and the empty string ("") count as false, while all the other values count as true. So 0 || -1 produces -1, and "" || "!?" yields "!?".

// The && operator works similarly but the other way around. When the value to its left is something that converts to false, it returns that value, and otherwise it returns the value on its right.

// Another important property of these two operators is that the part to their right is evaluated only when necessary. In the case of true || X, no matter what X is—even if it’s a piece of program that does something terrible—the result will be true, and X is never evaluated. The same goes for false && X, which is false and will ignore X. This is called short-circuit evaluation.

// The conditional operator works in a similar way. Of the second and third values, only the one that is selected is evaluated.

// ! Summary
/* We looked at four types of JavaScript values: numbers, strings, Booleans, and undefined values.  

Such values are created by typing in their name (true, null) or value (13, “abc”). You can combine and transform values with operators. We saw binary operators for arithmetic (+,-, *, /, and %), string concatenation(+), comparison(==, != , !==, < , >, <=, >=), and logic (&&, ||), as well as several unary operators (- to negate a number, ! to negate logically, and typeof to find a value's type) and a ternary operator(?:) to pick one of two values based on a third value. */

// ? PROGRAM STRUCTURE
// To catch and hold values, JavaScript provides a thing called a binding, or variable:
// let caught = 5 * 5;
// That's a second kind of statement. The special (keyword) let indicates that this sentence is going to define a binding. It is followed by the name of the binding and, if we want to immediately give it a value, by an = operator and an expression.

// After a binding has been defined, its name can be as an expression.The value of such an expression is the value the binding currently holds. Here's an example:

let ten = 10;
console.log(ten * ten);

// When a binding points at a value, that does not mean it is tied to that value forever. The operator can be used at any time on existing bindings to disconnect them from their current vale and have them point to a new one.

let mood = "light";
console.log(mood);
// I change the value on the second expressions.
mood = "dark";
console.log(mood);

// A single let statement may define multiple bindings. The definitions must be separated by commas.

let one = 1,
  two = 2;
console.log(one + two);

// var (short for "variable") is the way bindings were declared in pre-2015 Javascript.
// ! The word const stands for constant. It defines a constantbinding, which points at the same value for as long as lit lives. This is useful for bindings that give a name to a value so that you can easily refer to it later.
// * The environment
//  * The collection of bindings and their values that exist at a given time is called the environment. When a program starts up, this environment is not empty. It always contains bindings that are part of the language standard, and most of the time, it also has bindings that provide ways to interact with the surounding system.

// ? FUNCTIONS

// A lot of the values provided in the default environment have the type function. A function is a piece of program wrapped program wrapped in a value. Such values can be applied in order to run the wrapped program.

/* prompt("Enter passcode"); */

// Executing a function is called invoking,calling, or applying it. You can call a function value. Usually you'll directly use the name of the binding that holds the function.

console.log(Math.max(2, 4));

console.log(Math.min(2, 4) + 100);

if (1 + 1 == 2) console.log("It's true");

// You often won't just have code that executes when a condition holds true, but also code that handles the other case. You can use the else keyword, together with if, to create two separate, alternative execution paths.

// ! Looping control flow allow us to go back to some point in the program where we were before and repeat it with our currrent program state.

for (let number = 0; number <= 12; number = number + 2) {
  console.log(number);
}

// The standard Javascript functions, and most Javascript functions, and most Javascript programmers, follow the bottom style - they capitalize every word except the first.

for (let line = "#"; line.length < 8; line += "#") console.log(line);

for (let n = 1; n <= 100; n++) {
  let output = "";
  if (n % 3 == 0) output += "Fizz";
  if (n % 5 == 0) output += "Buzz";
  console.log(output || n);
}

