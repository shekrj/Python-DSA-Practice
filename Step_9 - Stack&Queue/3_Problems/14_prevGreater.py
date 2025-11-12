def pge(arr):
    st=[]
    res=[-1]*len(arr)
    for i in range(len(arr)):
        while st and st[-1]<=arr[i]:
            st.pop()
        if st:
            res[i]=st[-1]
        st.append(arr[i])
    return res