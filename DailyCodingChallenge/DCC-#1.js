// This problem was recently asked by Google.
// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

var input=[1,2,3,8,14];

for (i=0;i<input.length;i++){
    for (j=i+1;j<input.length;j++){
    var sum = input[i]+input[j];
        if (sum === 17){
            console.log(' '+input[i]+' '+input[j]);
        }
    }
}
