fn main() {
    
}

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
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
