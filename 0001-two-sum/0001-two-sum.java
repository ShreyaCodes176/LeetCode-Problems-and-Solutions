import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap<Integer,Integer> sum=new HashMap<>();
       for(int i=0;i<nums.length;i++)
       {
        if(sum.containsKey(target-nums[i]))
            {
                int res[]={sum.get(target-nums[i]),i};
                return res;
            }
        else
            sum.put(nums[i],i);
       }
       return new int[]{-1,-1};
}
}
