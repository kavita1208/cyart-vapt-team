asset = input("Enter Asset (URL/Domain): ").lower().strip()

if "api" in asset:
    category = "API"

elif "admin" in asset:
    category = "Admin Portal"

else:
    category = "Web Application"

print("\nAsset:", asset)
print("Category:", category)
