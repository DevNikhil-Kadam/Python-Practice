def chartostr(arr):
        # code here
        new_s = ""
        for i in range(0,len(arr)):
            new_s = new_s + arr[i]
        
        return new_s

print(chartostr(["N","I","K","H","I","L"]))