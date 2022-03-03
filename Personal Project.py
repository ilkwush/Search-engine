# 2021/9/28
import re

stock_dic = {}
f = open("stock_data_v2", encoding="utf8")
headers = f.readline().strip().split(",")

# Explanation:
# Read data from a file into a dictionary into an utf 8 format

# 2021/9/29 -- 2021/10/21
for line in f:
    line = line.strip().split(",")
    stock_dic[line[0]] = line

# Explanation:
# Read each line of stock's information without space and comma between each stock's data

# 2021/10/30 -- 2021/11/21
f.close()
for i, j in stock_dic.items():
    print(i, j)

while True:
    cmd = input("Please type the stock information you want：").strip()
    if not cmd:
        continue

    for s_id, s_data in stock_dic.items():
        s_name = s_data[1]
        if cmd in s_name:
            print(s_data)
    # Allow filtering information according to the columns of 'current price', 'change rate' and 'turnover rate'
    # If the current price is >50, print all stocks whose prices are greater than 50
    # Print all stocks that change rate less than 50

    # Ensure program robustness in advance avoid program crushing

    # Check if this formula is valid (regular expression)
    cmd_parser = re.split("[<>]", cmd)
    if len(cmd_parser) != 2:

        continue

# 2021/11/30 -- 2022/1/1
    filter_column, filter_val = cmd_parser
    # Check the column name legal or not
    if filter_column not in ["current price", "change rate", "turnover rate"]:
        continue
    # Validity of values
    try:
        filter_val = float(filter_val)
    except ValueError:
        continue

    # Select index from column name
    column_index = headers.index(filter_column)
    for s_id, s_data in stock_dic.items():
        if ">" in cmd:
            if float(s_data[column_index].strip("%")) > filter_val:
                print(s_data)
        else:
            if float(s_data[column_index].strip("%")) < filter_val:
                print(s_data)

## Student evaluation
# Objective I: 6
# Objective II: 7
# Objective III: 7
# Objective IV: 8

# "1 - 2 Not there yet
# I	The code does not compile and is inefficient when it's running in an expert's perspective
# II The code is hard to understand and take more than 15 minutes to read by an expert
# III The search engine has not extra functions, but only has typing the stock's name to get information
# IV 30 to 50 errors or over 50 errors in running the code.

# "3 - 4 Almost there
# I	The code compiles, but the code is poorly written and confusing to read and doesn't do what it is intended to do in an expert's perspective.
# II The code is still hard to understand and take more than 10 minutes to read by an expert
# III The search engine has limited extra functions, it has by typing the stock's name and change rate to get information
# IV 20 to 30 errors or less than 20 errors in running the code.

# "5 - 6
# Got it(meets)
# I	The code compiles successfully and does what is intended to do,  but it runs inefficiently and contains unnecessary processing in an expert's perspective.
# II The code is getting easy to understand and take more than 5 minutes to read by an expert
# III The search engine has extra basic functions, it has by typing the stock's name, change rate and current price to get information.
# IV 10 to 20 errors or less than 10 errors in running the code.

# "7 - 8
# Wow(succeeds)
# I	Code compiles successfully. The code does what it is intended to do, and is clearly written, also comments are included in the code to explain what it does. Variable and methods are named to indicate what function they perform.  Also it runs efficiently and contains no unnecessary processing in an expert's perspective.
# II The code is easy to understand and take less than 5 minutes to read by an expert
# III The search engine has extra advanced functions, it has by typing the stock's name, change rate, current price and turnover rate to get information.
# IV 1 or 4 errors or completely 0 errors in running the code.
