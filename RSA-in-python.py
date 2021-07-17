def mod_inverse(x,y):
	def eea(a,b):
		if b==0:return (1,0)
		(q,r) = (a//b,a%b)
		(s,t) = eea(b,r)
		return (t, s-(q*t) )

	inv = eea(x,y)[0]
	if inv < 1: inv += y 
	return inv
def fact(n):
    fact = []
    i = 2
    while i<=n:
        if n%i==0:
            fact.append(i)
            n//= i
        else:
            i+=1
    return fact
while True:
        P=76245601
        Q=99192971
        print(f"P= {P}")
        print(f"Q= {Q}")
        MOD=P*Q
        T = (P-1)*(Q-1)
        print("MOD=",MOD)
        print("T=",T)
        E = 65537
        print("E=",E)
        D=mod_inverse(E,T)
        print("D=",D)
        def encrypt_pub(me):
            en = pow(me,E, MOD)
            return en
        def encrypt_priv(me):
            dn = pow(me,D,MOD)
            return dn
        message = str(input("Enter the message to be encrypted: "))
        print("Original Message is: ", message)
        cipher=""
        c=0
        numform = ""
        for i in message:
                i = ord(i)
                c+=1
                if len(str(i)) <=2:
                        numform+=str("0"+str(i))
                else:
                        numform+=str(i)
                if c == 2:
                        numform+=" "
                        c=0
        print(numform, "numform")
        for i in numform.split():
                i=int(i)
                i = encrypt_pub(i)
                cipher+=str(i)+" "
        print(cipher, "cipher")
        message=""
        for i in cipher.split():
                message+=str(encrypt_priv(int(i)))+" "
        print(message)
        print("*"*20)
