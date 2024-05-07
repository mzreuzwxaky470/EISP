
function f_gold(nums, k) {
    let s = [0].concat(nums.map((sum => v => sum += v)(0)));
    let ans = 0;
    for (let i = 1; i < nums.length + 1; i++) {
        if (nums[i - 1] >= k) continue;
        let left = 1;
        let right = i;
        while (left < right) {
            let mid = Math.floor((left + right + 1) / 2);
            if ((s[i] - s[i - mid]) * mid < k) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        ans += left;
    }
    return ans;
}

