/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;

    let res = new Array(n);
    let prefix = 1;
    let postfix = 1;
    
    for (let i = 0; i < nums.length; i++){
        res[i] = prefix;
        prefix *= nums[i];
    }
    for (let i = nums.length-1; i >-1; i --){
        res[i] *= postfix;
        postfix *= nums[i];
    }    
    return res;
    
};