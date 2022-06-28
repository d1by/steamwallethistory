add=0
spend=0
endloc=0
endloc2=0
i=0
j=0
#source
with open('wallet.txt', 'r') as source:
    content = source.read()
    
    #money spent via steam wallet
    endval = content.count("""-align: right'>-""")
    endval = endval/2
    while i<endval:
        loc = content.find("""-align: right'>-""", endloc)
        endloc = content.find("</td>", loc)
        src = content[loc+20:endloc]
        spend = spend + float(src)
        endloc = endloc + 500
        i=i+1

    #money received via steam wallet
    endval2 = content.count("""-align: right'>+""")
    endval2 = endval2/2
    while j<endval2:
        loc2 = content.find("""-align: right'>-""", endloc2)
        endloc2 = content.find("</td>", loc2)
        src2 = content[loc+20:endloc]
        add = add + float(src)
        endloc2 = endloc2 + 500
        j=j+1

print("----------------------------")
print("Steam Wallet History")
print("----------------------------")
print("\nTotal money spent: ", round(spend,2), "in ", int(endval), " transactions")
print("\nTotal money received: ", round(add, 2), "in ", int(endval2), " transactions")
print("\n--------------------------")
print("\nLIMITATIONS: ")
print("\n1)External funds are ignored. ")
print("Only purchases via the Steam Wallet are considered.")
print("To locate external funds, navigate here: ")
print("https://help.steampowered.com/en/")
print("Alternatively, follow these instructions: ")
print("Steam > Help (top bar) > Steam Support > My Account > Data Related to Your Steam Account > External Funds Used")
print("\n2)No currency conversion is involved.")

while True:
    k = input("\n\nExit? (Y/N)\n")
    if(k=="Y" or k=='y'):
        break;
