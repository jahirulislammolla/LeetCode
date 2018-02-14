class Solution {
    public int pivotIndex(int[] nums) {
        int d=0,f=0;
        for(int i: nums) 
            d+=i;
        for(int j=0; j<nums.length; j++)
        {   //System.out.println(f);
            if(d-f-nums[j]==f)
               {
                return j;
               }  
         f+=nums[j]; 
        }
        return -1;
    }
}
