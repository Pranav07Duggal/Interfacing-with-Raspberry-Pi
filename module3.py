import http.client

# Establish HTTPS connection to www.uci.edu
conn = http.client.HTTPSConnection("www.uci.edu")

# Send a GET request for the root page
conn.request("GET", "/")

# Get the response
response = conn.getresponse()

# Read and decode the contents of the page
webpage_content = response.read().decode('utf-8')

# Print the webpage content
print(webpage_content)

# Close the connection
conn.close()
