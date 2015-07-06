/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
 
/**
 *  runtime: 40ms
 *  error : 2   does not consider deeply about same points.
 * 
 * 
 */ 
bool cmp(Point& p1, Point& p2){
    if(p1.x==p2.x)
        return p1.y<p2.y;
    return p1.x<p2.x;
}
class Solution {
public:
    int maxPoints(vector<Point>& points)  {
        int size = points.size();
        if(size<3) return size;
        sort(points.begin(),points.end(),cmp);
        int Max= 0;
        for(int i=0; i<size-1; i++){
            int repeat = 0;
            while(i<size-1&&points[i].x==points[i+1].x&&points[i].y==points[i+1].y){
                repeat++;
                i++;
            }
            for(int j=i+1; j<size; j++){
                int cnt=2;
                int p=j+1;
                if(points[i].x==points[j].x){
                   while(p<size) {
                       if(points[j].x==points[p].x)
                            cnt++;
                        p++;
                   }
                }
                else if(points[i].y==points[j].y){
                   while(p<size) {
                       if(points[j].y==points[p].y)
                            cnt++;
                        p++;
                   }
                }
                else{
                    for(;p<size;p++){
                        if(points[j].x==points[p].x&&points[j].y==points[p].y){
                            cnt++;
                            continue;
                        }
                        if(points[j].x==points[p].x||points[j].y==points[p].y)
                            continue;
                        if((points[j].y-points[i].y)*(points[p].x-points[j].x)==
                            (points[p].y-points[j].y)*(points[j].x-points[i].x))
                            cnt++;
                    }
                }
                Max=max(Max,cnt+repeat);
            }
            Max = max(Max,repeat+1);
        }
        return Max;
    }
};
