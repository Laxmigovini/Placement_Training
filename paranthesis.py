def paranthesis(n,s='',l=0,r=0):
    if len(s)==2*n:
        print(s)
        return
    if l < n:
        paranthesis(n,s+'(',l+1,r)
    if l > r:
        paranthesis(n,s+')',l,r+1)
paranthesis(3)
'''
def parathesis(n,s=''):
    if len(s) == n:
        print(s)
        return
    parathesis(n,s+'(')
    parathesis(n,s+')')
parathesis(3)
#output
(((
(()
()(
())
)((
)()
))(
)))

'''