from datetime import datetime

# A simple "database" (dictionary) storing the last time users were active
user_last_online = {
        "Alice": "2026-06-25 14:30:00",
        "Bob": "2026-06-25 15:45:12"
}

def update_online_time(username):
    """Updates the user's last online time to the current time."""
   
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save it to our database
    user_last_online[username] = current_time
    print(f"Updated: {username} was just online at {current_time}.")

def check_online_time(username):
    """Checks the last time a user was recorded as online."""
    if username in user_last_online:
        last_seen = user_last_online[username]
        print(f"[{username}] was last seen online at: {last_seen}")
    else:
        print(f"Error: We don't have any record for [{username}].")

# --- Let's test the code ---

# 1. Check a user who is already in the system
check_online_time("Alice")

# 2. Add a new user who just logged in
update_online_time("Charlie")

# 3. Check the new user's time
check_online_time("Charlie")