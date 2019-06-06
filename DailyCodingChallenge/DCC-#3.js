// Good morning! Here's your coding interview problem for today.

// This problem was asked by Uber.
// Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
// For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
// Follow-up: what if you can't use division?


var arr = [3,2,1];
var temp = 1;
var kali = 1;
var newarr = [];

for(i=0;i<arr.length;i++){
  kali = 1;
  for (j=0;j<arr.length;j++){
    if (i != j) {
    kali *= arr[j];      
    }
  }
  newarr[i] = kali; 
}
console.log(newarr);


// set temp variable = 1,
// compare array position.
// Multiple the different element in the array
// Create new array 