print({True: f"{(s:=str(input()))} is a Palindrome", False: f"{s} is not a Palindrome"}[s.lower() == s.lower()[::-1]])