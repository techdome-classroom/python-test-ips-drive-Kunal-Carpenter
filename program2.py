def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass

function smp(nums) {
    let n = nums.length;
    
    // Step 1: Replace negative numbers and numbers greater than n with 0
    for (let i = 0; i < n; i++) {
        if (nums[i] <= 0 || nums[i] > n) {
            nums[i] = 0;
        }
    }
    
    // Step 2: Mark indices corresponding to positive numbers as negative
    for (let i = 0; i < n; i++) {
        let index = Math.abs(nums[i]) - 1;
        if (index < n && nums[index] > 0) {
            nums[index] = -Math.abs(nums[index]);
        }
    }
    
    // Step 3: Find the first positive number's index
    for (let i = 0; i < n; i++) {
        if (nums[i] >= 0) {
            return i + 1; // Return the smallest positive integer missing
        }
    }
    
    // Step 4: If all numbers are present, return n+1
    return n + 1;
}

module.exports = smp;

