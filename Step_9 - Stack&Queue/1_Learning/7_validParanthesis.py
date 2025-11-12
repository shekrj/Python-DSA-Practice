def func(s):
    st=[]
    for i in s:
        if (i=="(") or (i=="{") or (i=="["):
            st.append(i)
        else:
            if len(st)==0:
                return False
            else:
                el=st[-1]
                st.pop()
                if (el=='(' and i==')') or (el=="{" and i=="}") or (el=="[" and i=="]"):
                    continue
                else:
                    return False
    return len(st)==0