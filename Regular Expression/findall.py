import  re
email_address = "Please contact us at: supp_ort@datacamp.com, xyz@datacamp.com"

#'addresses' is a list that stores all the possible match

addresses = re.findall(r'[\w]+@[\w.]*', email_address)
print(addresses)
for address in addresses:
    print(address)