st = input("Enter an expression:")
if st.count('1') % 3 == 0 or st.count('0') % 3 == 0:
    print("Accepted")
else:
    print("Rejected")
