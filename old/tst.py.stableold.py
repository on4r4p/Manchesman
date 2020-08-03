import random,time

finalres = []

def epuration(Strt,btslst):
     global finalres

     tmpsaved = []
     new = []
     lastln = 666
     while len(tmpsaved) != lastln:
          lastln= len(tmpsaved)
          if len(tmpsaved) >  0 :
                    Strt = tmpsaved
                    tmpsaved = []
          for sample in Strt:
                 smp = sample.replace(" ","")
                 for nextsample in BitLetters:
                    nxt = nextsample.replace(" ","")
                    if sig[len(smp):len(smp)+len(nxt)] == nxt:
                         newsample = sample+nextsample
                         nsmp = smp+nxt
                         if len(nsmp)<= len(sig):
                              if not nsmp in tmpsaved:
                                   tmpsaved.append(nsmp)
                                   onething = sample
                                   onething += " "
                                   onething += nextsample
                                   new.append(onething)
                                   finalres.append(onething)
#                         print("Newrealstart : ",newsample)
     return(new)

sig = "101110011011101111001111110101100011010100011010010001100001011111101001011100101110001010100111100"
KnownPlain = "LE MOT DE PASSE EST "
Letters = []
BitLetters = []
SigStarts = []
print(sig)
print(KnownPlain)

for i in KnownPlain:
  if not i in Letters:
     Letters.append(i)

start = 0
end = 1
   
while start <= len(sig):
      if len(sig[start:end]) >1 and len(sig[start:end]) < 10:
        if start >0:
          BitLetters.append(sig[start:end])
        else:
          SigStarts.append(sig[start:end]) 
          #print(sig[start:end])
      end = end + 1

      if end >= len(sig):
               end = 1
               start = start +1
               #print(start)

print(len(BitLetters))

#set = set(BitLetters)
#final = list(set)
#BitLetters = final

soluce = epuration(SigStarts,BitLetters)
print("Len soluce :",len(soluce))
while len(soluce[0].split(" ")) <= len(Letters):
     soluce = epuration(soluce,BitLetters)
     print("Len soluce :",len(soluce))

time.sleep(2)

for res in finalres:
     r = res.replace(" ","")
     if r[0:len(r)] == sig[0:len(r)]:
          print("==")
          print("Original : ",sig)
          print()
          print("Match : ",res)
     try:
          if len(res.split(" ")) >= len(Letters):
               print("==!==")
               print("Right split :")
               print(res)
     except:
          pass

#     unik = ltr+sample+ltr
#     if not unik in saved:
#          saved.append(unik)
#          for pos,ltr in zip(table,Letters):
#               result = result.replace(ltr,BitLetters[pos])
#               break
# if len(result) <= len(sig) and sig[0:15] == result[0:15]:                           
#          print("Solution : ",result)                   

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
