def DecimalToOctal(num):
  if(num>7):
    DecimalToOctal(num//8)
  print(num%8,end="")
 
DecimalToOctal(96)