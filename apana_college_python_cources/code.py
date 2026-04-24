import urllib.request

def fetch_and_write(url: str, output_file: str) -> None:
    """Fetch data from a URL and write it to a file."""
    print(f"Fetching data from: {url}")
    
    with urllib.request.urlopen(url) as response:
        data = response.read()
    
    with open(output_file, "wb") as f:
        f.write(data)
    
    print(f"Data written to: {output_file}")
    print(f"Bytes written: {len(data)}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    output_file = "output.txt"
    fetch_and_write(url, output_file)