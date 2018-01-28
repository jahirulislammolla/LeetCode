class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=list(str(x))
            x= int("-"+"".join(x[1:][::-1]))
        else:
            x=(int("".join(list(str(x))[::-1])))
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff
        if(x<0):
            val=x&neg_limit
            if(val==neg_limit):
                return x
            else:
                return 0
        elif(x==0):
            return x
        else:
            val = x&pos_limit
            if(val==x):
                return x
            else:
                return 0
