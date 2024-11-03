/*
 * @lc app=leetcode id=9 lang=rust
 *
 * [9] Palindrome Number
 */

// @lc code=start
impl Solution {
    fn is_palindrome(num: i32) -> bool {
        if num < 0 {
            return false;
        }
        if num < 10 {
            return true;
        }

        let mut original = num;
        let mut reversed = 0;

        while original > 0 {
            reversed = (reversed * 10) + (original % 10);
            original /= 10;
        }

        num == reversed
    }
}
// @lc code=end

