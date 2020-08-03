Sig = "101000011010111100001111010101001101110001011111111001100011110111101001010100101010110111010001100"
KnownPlain = "le mot de passe est"
KnownPlain = KnownPlain.upper()



LnSig = len(Sig)

Letters = []
LettersCnt = []
BitLetters = []
Counter = ""
MxCounter = ""
for ltr in KnownPlain :

     if not ltr in Letters:
          Letters.append(ltr)
          LettersCnt.append(KnownPlain.count(ltr))
          Counter += "4"
          MxCounter += "9"



print("\nSignal :",Sig)
print("\nKnown Plain Text : ",KnownPlain)

print("\n Solution :")

print(""" 
L     E      M     O     T       D     E      P     A   S    S    E      E  S    T       C    A   C    A   H     U     E  T   E
10100 00 110 10111 1000  011 110 10101 00 110 11100 010 1111 1111 00 110 00 1111 011 110 1001 010 1001 010 10110 11101 00 011 00
     """)



print("\n -Starting Huffman Attack-")

Counter = int(Counter)
MxCounter = int(MxCounter)
     

while Counter <= MxCounter:
      print("BruteForcing : " + str(Counter) + " / " +str(MxCounter) ,end= "\r")
      ArrayCounter = [int(i) for i in str(Counter)]
      ArrayCounter = list(reversed(ArrayCounter))
      start = 0
      BitLetters = []
      for end in ArrayCounter:
               if end == 1:
                    end = end + 1
               strtend = start + end
               if strtend > LnSig:
                         strtend = strtend - (strtend - LnSig)
               sample = Sig[start:strtend]
               BitLetters.append(sample)
               start = start + len(sample)
      
      check = []
      stop = 0
      for bit,ltr in zip(BitLetters,KnownPlain):
          if stop != 1:
               test = bit+":"+ltr
               for item in check:
                    if ltr in item:
                         bit2check =item.split(":")[0]
                         if bit2check != bit:
                              stop = 1
                    bit2check2 =item.split(":")[0]
                    ltr2check = item.split(":")[1]
                    if stop != 1 and bit == bit2check2 and ltr != ltr2check:
                         stop = 1
               check.append(test)

      if stop != 1:
         table = ""
         for bit,ltr in zip(BitLetters,KnownPlain):
             table += ltr.upper()
             for i in range(0,len(bit)):
                  table += " "
         tobit = " ".join(BitLetters)
         print(table)
         print(tobit)
 
     
      Counter = Counter + 1
