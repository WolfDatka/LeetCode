/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let nums_len = nums.len();

        let mut i = 0;
        while i < nums_len {
            let mut j = 0;
            while j < nums_len {
                if j != i && nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }

                j += 1;
            }
            i += 1;
        }

        vec![0, 0]
    }
}
// @lc code=end
