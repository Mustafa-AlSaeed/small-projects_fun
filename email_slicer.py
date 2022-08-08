email = input("please input your email").strip() #the strip function removves any unwanted spaces in this tring

username = email[:email.index('@')] #in my scenario this like writing email[:where at is located 13 for example]
domain = email[email.index('@')+1:]

print(f"your username is {username} & domain is {domain}"
      )

