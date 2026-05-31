maheshbabu_fans={"sriram","eshwar","yeshwanth","rakesh","ashwanth"}
prabhas_fans={"sriram","yeshwanth","rakesh","harsha"}
both=maheshbabu_fans & prabhas_fans

print("BOTH","=",both)
only_babufans=maheshbabu_fans-prabhas_fans
print("babbu" ,"=" ,only_babufans)
All_fans=maheshbabu_fans|prabhas_fans
print("TFI" ,"=",All_fans)