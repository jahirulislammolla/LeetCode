class Solution {
    public int[] constructArray(int n, int k) {
        int[] list= new int[n];
        int a=1,j=1+k;
        int t=0;
        while(true && t<n)
        {
            if(t%2==0)
                {
                list[t]=a;
                a++;
                }
            else{
                list[t]=j;
                j--;
            }
            t++;
            if(a>j)
                break;
        }
        j=k+2;
        while(t<n)
        {
            list[t]=j;
            j++;
            t++;
        }
        return list;
    }
}
