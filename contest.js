// Please implement the serializer and deserializer for char array below.
// For char arrays, we follow the JSON standard according to http://www.json.org/
// Therefore, a single character A is represented as "A" (wrapped in double quotes instead of single quotes).
// A char array containing 3 elements "A", "B", "C" is represented in string as ["A","B","C"].
// For the purpose of this problem, you must not use JSON parser library or eval method. 
// Standard library provided by the language (not including JSON library) is allowed.

function characterArrayToString(charArray) {
  var charString = [];
  
  for(var i = 0; i < charArray.length; i++) {
    charString.push(charArray[i]);
  }

  var res = charString.join("");

  return res;
}

// Bonus point if your deserializer is able to deal with whitespaces between elements.
// For example: param = "[  \"a\",  \"b\", \"c\"  ]"
function stringToCharacterArray(param) {
  throw "Not implemented yet.";
}

// Note: These tests are basic and passing them does not mean your code is correct.
// Feel free to write additional tests and test serializer and deserializer individually.
function test() {
  var testcases = [
      "[]",
      "[\"a\",\"b\",\"c\"]",
      "[\"T\",\"e\",\"!\",\"'\"]",
      "[\"'\",\"\\\"\",\"c\"]",
      "[\"\\n\",\"\\t\",\"'\",\"\\\"\",\"\\\\\"]"
  ];

  for (var index = 0; index < testcases.length; index++) {
      var testcase = testcases[index];
      try {
          if (characterArrayToString(stringToCharacterArray(testcase)) != testcase) {
              console.log("TESTCASE FAILED : " + testcase + "\n");
          } else {
              console.log("TESTCASE PASSED \n");
          }
      } catch(err) {
          console.log(err)
          break;
      }
  }
}


(function main() {
  test();
}());
