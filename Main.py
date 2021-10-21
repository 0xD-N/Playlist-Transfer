import ytclient

client = ytclient.client()

if __name__ == "__main__":
    
    print(client.getPlaylist(input("Enter youtube playlist name: ")))
    
    print("\nFinished")