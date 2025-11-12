#Brute-Force
class StockSpanner:

    def __init__(self):
        self.arr=[]
        
        

    def next(self, price: int) -> int:
        self.arr.append(price)
        span=1
        for i in range(len(self.arr)-2, -1, -1):
            if self.arr[i]<=price:
                span+=1
            else:
                break
        return span

#Optimal
class StockSpanner:

    def __init__(self):
        self.st=[]
        
        

    def next(self, price: int) -> int:
        span=1
        while self.st and self.st[-1][0]<=price:
            span+=self.st.pop()[1]
        self.st.append((price, span))
        return span
 ##
class StockSpanner:

    def __init__(self):
        self.st=[]
        self.prices=[]
        

    def next(self, price: int) -> int:
        i=len(self.prices)
        self.prices.append(price)
        while self.st and self.prices[self.st[-1]]<=price:
            self.st.pop()
        if not self.st:
            span=i+1
        else:
            span=i-self.st[-1]
        self.st.append(i)
        return span