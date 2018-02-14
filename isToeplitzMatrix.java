class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int l1=matrix.length;
        int l2=matrix[0].length;
        int a=0,b=l1-1,x=0,p=0,q=0;
        while(a<l2)
        {
            if(b>0)
            {   x=matrix[b][a];
                p=a;
                q=b;
                while(p+1<l2 && q+1<l1)
                {
                    if(matrix[q+1][p+1]!=x)
                        return false;
                    p++;
                    q++;
                }
                b--;
            }
            else{
                x=matrix[b][a];
                p=a;
                q=b;
                while(p+1<l2 && q+1<l1)
                {
                    if(matrix[q+1][p+1]!=x)
                        return false;
                    p++;
                    q++;
                }
                a++;
            }
        }
        return true;
    }
}
