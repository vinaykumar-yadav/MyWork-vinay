import sys  # For simplicity, we'll read config file from 1st CLI param sys.argv[1]
import json, logging, msal, requests

{
    "authority": "https://login.microsoftonline.com/organizations",
    "client_id": "fd2bfb66-5b4c-492e-8f39-44699600bca8",
    "scope": ["User.ReadBasic.All"],
    "username": "v-vinayyadav@microsoft.com",  
    "endpoint": "https://graph.microsoft.com/v1.0/users"
}

result = None
# Create a preferably long-lived app instance which maintains a token cache.
app = msal.PublicClientApplication(
    client_id="fd2bfb66-5b4c-492e-8f39-44699600bca8", 
    authority="https://login.microsoftonline.com/organizations",
    )
accounts = app.get_accounts(username="v-vinayyadav@microsoft.com")
if accounts:
    print("Account(s) already signed in:")
    for a in accounts:
        print(a["username"])   
        result = app.acquire_token_silent(config["scope"], account=chosen)
if not result:
    logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
    print("A local browser window will be open for you to sign in. CTRL+C to cancel.")
    result = app.acquire_token_interactive(
        ["User.ReadBasic.All"],
        login_hint="v-vinayyadav@microsoft.com",  # You can use this parameter to pre-fill
            # the username (or email address) field of the sign-in page for the user,
            # if you know the username ahead of time.
            # Often, apps use this parameter during reauthentication,
            # after already extracting the username from an earlier sign-in
            # by using the preferred_username claim from returned id_token_claims.
        )        
if "access_token" in result:
    print(result['access_token'])
    print("Graph API call result: %s ...")
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))  # You may need this when reporting a bug        