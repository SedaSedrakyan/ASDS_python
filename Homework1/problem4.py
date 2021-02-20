# Create the dictionary ​market​ with the following values: ​
# {“dairy”: [“yogurt”, “cheese”], “fruits”: [
# ‘banana’, ‘apple’, ‘orange’, ‘lemon’, ‘apple’, ‘banana’, ‘banana’]}​. 
# Add the key ​“candies” ​with a value ​[‘mars’, ‘kinder’, ‘twix’] ​
# to the dictionary ​Market​։ Sort the values at the key ​“fruits”​ 
# in an increasing order and get rid of the duplicate values։ 
# Print the dictionary ​Market ​before and after the changes.

market = {"dairy": ["yogurt", "cheese"], 
          "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
market["candies"] = ["mars", "kinder", "twix"]
market['fruits'].sort()
market['fruits'] = set(market['fruits'])

print("Final look of market is","\n", market)