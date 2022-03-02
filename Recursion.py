# recursive function 

def functionOne(test):
  if (test < 1):
    return;
  else:
    print(test)
    functionOne(test-1)
    print(test)
    return

functionOne(3)