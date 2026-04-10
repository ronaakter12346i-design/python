Bangla1 = float(input("plz input your bangla first paper mark "))
Bangla2 = float(input("plz input your bangla second paper mark"))
English1 = float(input("plz inpput your english first paper mark"))
English2 = float(input("plzinput your english secoond paper mark"))
ICT = float(input("plz input your ICT mark"))
Biology1 = float(input("plz input biology1 mark"))
Biology2 = float(input("plz input your boilogy second paper mark"))
Chemistry1 = float(input("plz input your chemistry1 mark"))
Chemistry2 = float(input("plz input your chemistry2 mark"))
Physics1 = float(input("input your physics1 mark"))
Physics2 = float(input("plz input your physics2 paper mark"))
Higher_Math1 = float(input("plz input your higher math1 mark"))
Higher_Math2 = float(input("inout HM2 mark"))
Bangla = Bangla1+Bangla2
English = English1+English2
Biology = Biology1+Biology2
Chemistry = Chemistry1+Chemistry2
Physics = Physics1+Physics2
Higher_Math = Higher_Math1+Higher_Math2
if(Bangla>=160 or Bangla<= 200):
    print("You got in Bangla A+")
elif(Bangla>=140 or Bangla<160):
    print("You got in Bangla A")
elif(Bangla>=120 or Bangla <140):
    print("You got in Bangla A- ")
elif(Bangla >=100 or Bangla<66):
    print("You got in Bangla B")
else:
    print("You are Fail")

if(English>=160 or English <200):

    print("You got in English A+")

elif(English>= 140 or English<160):

    print("You got in English A")

elif(English >=120 or English<140):

    print("You got in English A- ")

elif(English <100 or English>=66):

    print("You got in English B")

else:

    print("You are Fail")
if(ICT>=160 or ICT<=200):
    print("You are got A+ in ICT")
elif(ICT>= 140 or ICT<160):
    print("You got A in ICT")
elif(ICT>=120 or ICT <140):
    print("You got A- in ICT")
elif(ICT<100 or ICT>=66):
    print("You Got B in Bangla")
else:
    print("You are Fail in ICT")
if(Biology>=160 or Biology>=200):
    print("You got A+ in Biology")
elif(Biology>=140 or Biology<160):
    print("You got A in Biology")
elif(Biology>=120 or Biology<140):
    print("You got A- in Biology")
elif(Biology<100 or Biology>=66):
    print("You got B in Biology")
else:
    print("You are Fail in Biology")


if(Chemistry>=160 or Chemistry<=200):
    print("You Got A+ in Chenistry")
elif(Chemistry>=140 or Chemistry<160):
    print("You got A in chemistry")
elif(Chemistry>=120 or Chemistry<140):
    print("You got A-in Chemistry")
elif(Chemistry<100 or Chemistry>=66):
    print("You got B in Chemistry")
else:
    print("You are Fail in Chemistry")

if(Physics>=160 or Physics<=200):
    print("You got A+ in Physics")
elif(Physics>=140 or Physics<140):
    print("You got A in Physics")
elif(Physics>=120 or Physics<140):
    print("You Got in A- in Physics")
elif(Physics>= 100 or Physics<=66):
    print("You got B in Physics")
else:
    print("You are Fail In Physics")

if(Higher_Math>=160 or Higher_Math<=200):
    print("You got A+ in Higher Math")
elif(Higher_Math>=140 or Higher_Math<160):
    print("You got A in Higher Math")
elif(Higher_Math>=120 or Higher_Math<140):
    print("You got A- in Higher Math")
elif(Higher_Math>=100 or Higher_Math<=66):
    print("YOU GOT B in Higher Math")

else:
    print("You are Fail in Higher Math")



