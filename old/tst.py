import random,time

sig = "101110011011101111001111110101100011010100011010010001100001011111101001011100101110001010100111100"
KnownPlain = "LE MOT DE PASSE EST "

stat = ""
Letters = []
LettersCnt = []

for i in KnownPlain:
  if not i in Letters:
     Letters.append(i)
     LettersCnt.append(KnownPlain.count(i))

for i,j in zip(Letters,LettersCnt):

     stat += i + " cnt:" + str(j) + " , "



print()
print(sig)
print(KnownPlain)
print()
print(stat)
print()
cnt = 0
start = 0
final = []
   
#for cnt in range(0,len(sig)-len(Letters)) :
while 1 == 1:
      #print(ltr):
      BitLetters = []
      end = random.randint(1,10)
      charleft = len(sig)
      start = 0 + cnt
      stop = 0
      while charleft != 0:
          sample = sig[start:start+end]
          charleft = (len(sig) - len(sample))-start

           
          for chk in BitLetters:
               if sample == chk: 
                    stop = 1
                    end = end +1
          if stop != 1:  
               
               BitLetters.append(sample)
               end = random.randint(1,10)
               start = start + len(sample)
          else:
               stop = 0
         
      #print(" ".join(tmp))

      soluce = ""
      binsol = ""

      bincheck = KnownPlain
      saved = []
      for bits,ltr in zip(BitLetters,KnownPlain):
                    
                 soluce += "'" + ltr + "'= " + bits + " "
                 binsol += bits
                 unik = ltr+bits+ltr
                 bincheck = bincheck.replace(ltr,bits)
                 saved.append(unik)
      
      if len(bincheck) <= len(sig):
           lnSig = len(sig[0:len(bincheck)])
           if len(bincheck) == lnSig:
               #print(bincheck)
              if bincheck == sig[0:lnSig] :
               #score = int(len(sig)/2) 
               #if bincheck[0:score] == sig[0:score]:
                    print("==\n")
                    print(soluce)
                    print(" ".join(BitLetters))
                    print("Sig :",sig[0:lnSig])
                    print("Bin :",bincheck)
                    print("\n==")

print("""
     
 
P 10100
U 10101
E 00
L 10111
D 10110
  110
O 11100
M 11101
C 1001
T 1111
H 1000
S 010
A 011

     """)

#print(len(saved))
