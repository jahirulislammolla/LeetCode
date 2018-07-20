/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
   var max=0;
   var x=[];
    var i=0;
    var j=height.length-1;
   while(i<j)
       {
           p=height[i];
           q=height[j];
           s=i+1;
           l=j;
           u=j-1;
           v=i+1;
           while(s<=l || v<u)
               {   if ((s-i)*p<max && (l-i)*p<max)
                        {s=1; l=0;}
                   if ((j-v)*q<max && (j-u)*q<max)
                       {
                           v=1;
                           u=0;
                       }
                   if (s<=l)max=Math.max(max,(s-i)*Math.min(height[s],p),(l-i)*Math.min(height[l],p));
                   if (v<=u) max=Math.max(max,(j-v)*Math.min(height[v],q),(j-u)*Math.min(height[u],q));
                   s+=1;
                   l-=1;
                   v+=1;
                   u-=1;
               }
           i++;
           j--;
       }
    
    return max;
    
};
