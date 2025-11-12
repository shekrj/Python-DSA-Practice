class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"                                     # Base case for n = 1
        
        for _ in range(n - 1):                      # Iterate n-1 times to generate the sequence
            temp = ""
            count = 1
            
            for i in range(1, len(s)):              # Loop through s from the second character
                if s[i] == s[i - 1]:                # If current == previous, increment count
                    count += 1
                else:                               # If different, append count and character to temp
                    temp += str(count) + s[i - 1]
                    count = 1                       # Reset count for new character
            
            temp += str(count) + s[-1]              # Append the last counted group
            s = temp                                # Update s for the next iteration
        
        return s                                    # Return final result


class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        prev=self.countAndSay(n-1)
        res=""
        cnt=1
        for i in range(1, len(prev)):
            if prev[i]==prev[i-1]:
                cnt+=1
            else:
                res+=str(cnt)+prev[i-1]
                cnt=1
        res+=str(cnt)+prev[-1]
        return res

