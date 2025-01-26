# Function to read usernames from a text file and return a set
def read_usernames_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file.readlines())

# Paths to the extracted usernames files
followers_file_path = 'extracted_followers_usernames.txt' # output of 1_filtering.py
following_file_path = 'extracted_following_usernames.txt' # output of 1_filtering.py

# Read the usernames from both files
followers = read_usernames_from_file(followers_file_path)
following = read_usernames_from_file(following_file_path)

# Find users you follow but who do not follow you back
not_following_back = following - followers

# Sort the usernames in alphabetical order
sorted_not_following_back = sorted(not_following_back)

# Output the list of users who don't follow you back
if sorted_not_following_back:
    print("Users you follow but who don't follow you back:")
    # for username in sorted_not_following_back:
        # print(username)
else:
    print("Everyone you follow follows you back!")

# Optionally, save the sorted list to a file
with open('not_following_back.txt', 'w') as output_file:
    if sorted_not_following_back:
        output_file.write('\n'.join(sorted_not_following_back))
        print("List of users not following back saved to not_following_back.txt")
    else:
        output_file.write("Everyone you follow follows you back!")
        print("No one to save in not_following_back.txt")