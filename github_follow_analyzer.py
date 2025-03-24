import requests
import sys

def get_github_followers(username):
    """Returns the followers of the specified GitHub user."""
    followers = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/followers?per_page=100&page={page}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error: Couldn't get followers. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return []
        
        data = response.json()
        if not data:  # If page is empty, we've reached the end
            break
            
        followers.extend([user["login"] for user in data])
        page += 1
    
    return followers

def get_github_following(username):
    """Returns the users that the specified GitHub user is following."""
    following = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/following?per_page=100&page={page}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error: Couldn't get following. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return []
        
        data = response.json()
        if not data:  # If page is empty, we've reached the end
            break
            
        following.extend([user["login"] for user in data])
        page += 1
    
    return following

def analyze_follows(username):
    """
    Analyzes the followers and following of the specified user
    and lists users without mutual follow relationship.
    """
    print(f"Analyzing follow relationships for GitHub user '{username}'...")
    
    # Get followers and following
    followers = get_github_followers(username)
    following = get_github_following(username)
    
    if not followers and not following:
        print("Couldn't retrieve follower or following information.")
        return
    
    # Find users without mutual follow
    not_following_back = [user for user in following if user not in followers]
    not_followed_back = [user for user in followers if user not in following]
    
    # Print results
    print("\n--- SUMMARY ---")
    print(f"Total followers: {len(followers)}")
    print(f"Total following: {len(following)}")
    print(f"Mutual follows: {len(following) - len(not_following_back)}")
    
    print("\n--- USERS NOT FOLLOWING YOU BACK ---")
    if not_following_back:
        for user in not_following_back:
            print(f"- {user}")
    else:
        print("Everyone you follow is following you back!")
    
    print("\n--- USERS YOU DON'T FOLLOW BACK ---")
    if not_followed_back:
        for user in not_followed_back:
            print(f"- {user}")
    else:
        print("You follow all your followers!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_follow_analysis.py <github_username>")
        sys.exit(1)
    
    username = sys.argv[1]
    analyze_follows(username)