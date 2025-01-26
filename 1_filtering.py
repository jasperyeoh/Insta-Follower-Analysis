from bs4 import BeautifulSoup

# Function to extract Instagram usernames from the HTML file
def extract_usernames(file_path):
    usernames = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        # Find all <a> tags with href containing 'instagram.com'
        for a in soup.find_all('a', href=True):
            href = a['href']
            if 'instagram.com' in href:
                # Extract the username from the Instagram URL
                username = href.split('instagram.com/')[-1].strip('/')
                if username and username not in usernames:
                    usernames.append(username)
    return usernames

# Paths to your followers and following HTML files
followers_file_path = 'followers_1.html'  # downloaded from instagram
following_file_path = 'following.html'   # downloaded from instagram

# Extract usernames from both files
followers_usernames = extract_usernames(followers_file_path)
following_usernames = extract_usernames(following_file_path)

# Sort usernames in alphabetical order
followers_usernames = sorted(followers_usernames)
following_usernames = sorted(following_usernames)

# Print extracted usernames for followers
print("Extracted and sorted followers usernames:")
# for username in followers_usernames:
    # print(username)

# Print extracted usernames for following
print("\nExtracted and sorted following usernames:")
# for username in following_usernames:
    # print(username)

# Save the extracted usernames to separate text files
with open('extracted_followers_usernames.txt', 'w') as followers_file:
    followers_file.write('\n'.join(followers_usernames))
    print("Sorted followers usernames saved to extracted_followers_usernames.txt")

with open('extracted_following_usernames.txt', 'w') as following_file:
    following_file.write('\n'.join(following_usernames))
    print("Sorted following usernames saved to extracted_following_usernames.txt")