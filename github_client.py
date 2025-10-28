import os
from github import Github, Auth

def authenticate_github():
    """
    Authenticates with GitHub using a Personal Access Token
    stored in an environment variable.
    """
    token = os.environ.get('GH_TOKEN')
    
    if not token:
        print("Error: GH_TOKEN environment variable not set.")
        print("Please set it before running the script.")
        return None
    
    # Debug: Check token format (don't print the full token!)
    token = token.strip()  # Remove any whitespace
    print(f"Token found. Length: {len(token)}")
    print(f"Token prefix: {token[:4]}...")
    print(f"Token suffix: ...{token[-4:]}")
    
    # Check if token starts with expected prefixes
    valid_prefixes = ['ghp_', 'github_pat_', 'gho_', 'ghu_', 'ghs_', 'ghr_']
    if not any(token.startswith(prefix) for prefix in valid_prefixes):
        print(f"⚠️ Warning: Token doesn't start with a recognized prefix")
        print(f"Expected prefixes: {', '.join(valid_prefixes)}")
    
    print("Attempting authentication...")
    
    try:
        # Use the modern authentication method
        auth = Auth.Token(token)
        g = Github(auth=auth)
        
        # Test authentication
        user = g.get_user()
        print(f"✓ Successfully authenticated as: {user.login}")
        return g
        
    except Exception as e:
        print(f"✗ Error during authentication: {e}")
        print("\nTroubleshooting steps:")
        print("1. Verify your token is valid and not expired")
        print("2. Regenerate your token at: https://github.com/settings/tokens")
        print("3. Make sure the token has the required scopes (repo, user)")
        print("4. Check for extra spaces or quotes in your token")
        return None

# --- Main part of the script ---
if __name__ == "__main__":
    github_api = authenticate_github()
    
    if github_api:
        print("\n✓ Authentication successful!")
    else:
        print("\n✗ Authentication failed.")