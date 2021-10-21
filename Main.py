import ytclient

client = ytclient.client()

if __name__ == "__main__":
    
    print(type(client.getPlaylist("test")))
    
    print("\nFinished")