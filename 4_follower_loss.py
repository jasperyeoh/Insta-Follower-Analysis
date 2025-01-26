# Function to read usernames from a text file and return a set
def read_usernames_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file.readlines())

# Paths to the extracted usernames files
followers_1_file_path = 'extracted_followers_usernames_24_nov.txt'  
followers_2_file_path = 'extracted_followers_usernames_6_jan.txt'

# Read the usernames from both files
followers = read_usernames_from_file(followers_1_file_path)
following = read_usernames_from_file(followers_2_file_path)

# Find users you follow but who do not follow you back
not_following_back = followers - following

# Sort the usernames in alphabetical order
sorted_not_following_back = sorted(not_following_back)

# Output the list of users who don't follow you back
if sorted_not_following_back:
    print("Users you follow but who don't follow you back:")
    # for username in sorted_not_following_back:
      #  print(username)
else:
    print("Everyone you follow follows you back!")

# Optionally, save the sorted list to a file
with open('follower_loss_1.txt', 'w') as output_file:
    if sorted_not_following_back:
        output_file.write('\n'.join(sorted_not_following_back))
        print("time difference saved to follower_Loss_1.txt")
    else:
        output_file.write("Everyone you follow follows you back!")
        print("No one to save in follower_loss.txt")