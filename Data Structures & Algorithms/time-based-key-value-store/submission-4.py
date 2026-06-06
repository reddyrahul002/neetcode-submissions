class TimeMap:

    def __init__(self):
        self.present={}
        self.timestamp_prev=0
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.present.setdefault(key,[]).append((value,timestamp))
        self.timestamp_prev=timestamp


    def get(self, key: str, timestamp: int) -> str:

        if key not in self.present or timestamp < self.present[key][0][1] :
            return ''
        else:
            l,r=0,len(self.present[key])-1
            last_value=0
            while l<=r:
                mid=(l+r)//2
                if self.present[key][mid][1]==timestamp:
                    return self.present[key][mid][0]
                
                if self.present[key][mid][1]<timestamp:
                    l=mid+1
                    last_value=self.present[key][mid][0]
                else :
                    r=mid-1
            return last_value

                

                



            
        

        
