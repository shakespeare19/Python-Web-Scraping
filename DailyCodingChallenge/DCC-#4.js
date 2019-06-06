// Question:
// Good morning! Here's your coding interview problem for today.
// This problem was asked by Stripe.
// Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
// For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
// You can modify the input array in-place.


// array list 
var arr = [8,4,99,3,7,2,1,-1,9,5];
var sort = arr.sort();
var j = 1;
console.log(sort);

for (i=0;i<arr.length;i++){
  if(arr[i]<=0){

  }
  else{
    if (arr[i] != j){
      console.log(j);
        break;
    }
    j++;
  }
}
  





