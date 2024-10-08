import requests as requests
from bs4 import BeautifulSoup

allCommenters = []
def ellipsis_parser(text):
    try:
        # Split the string by whitespaces
        parts = text.split()

        # Extract the last number, which represents the total number of comments and return it as an integer datatype
        total_comments = int(parts[-2])

        #print(f"Total number of comments: {total_comments}")

        return total_comments
    except (ValueError, IndexError) as e:
        print(f"Error parsing the total number of comments: {e}")
        return None

def load_page(page, perPage, url):
    try:
        # Get a request to grab html content, print the status code to see if successful or fail, then store
        if page == 0:
            req = requests.get(url)
        else:
            req = requests.get(f"{url}?ctp={page}")
        #print(req)

        # Find the comment section
        soup = BeautifulSoup(req.content, "html.parser")

        # Narrow the html content to the list of comments by the class tag
        storage_comments = soup.find(class_="commentthread_comments")

        # Find the text that tells how many comments are being shown
        totalComments = soup.find(class_="forum_paging_summary ellipsis")

        # Parse the text to grab the total number of comments
        totalPages = ((ellipsis_parser(totalComments.text)) // perPage) + 1
        #print("the total number of pages would be ", totalPages)
        print("loaded page number ", page)

        # Function to get the comments
        gather_comments(storage_comments)

        return totalPages, storage_comments
    except requests.exceptions.RequestException as e:
        print("unsuccessful gathering of html content - ", e)
        return None, None

def gather_comments(storage_comments):
    # Find the comments group
    commenters = storage_comments.find_all_next('bdi')

    # Grab the names of each commenter
    for commenters in commenters:
        commenter_name = commenters.text
        allCommenters.append(commenter_name)

def check_true_comments():
    global allCommenters
    duplicates = []
    comment_number = 0

    # Grab the url from the user, if user accidentally links a page that is not the default page, return to default page 0
    while True:
        url = input("Enter the URL: ")
        if "?ctp=" in url:
            url = url.split("?ctp=")[0]

        # Load the first page to get all necessary data, including the total number of pages
        total_pages, comments = load_page(0, 15, url)

        # check if the url loads a page, if not, ask for another html link
        if total_pages is not None:
            break
        else:
            print("Invalid html link, please try again")

    # When comments are more than the total showing of comments per page. then loop through all pages
    if total_pages > 0:
        for page in range(2, total_pages + 1):
            load_page(page, 15, url)

    print(f"This giveaway's total number of comments is {len(allCommenters)}")

    # Specifically check duplicates and know their placement in the order table
    for i, user in enumerate(allCommenters):
        duplicate_counter = 0
        for j, comments in enumerate(allCommenters):
            comment_number += 1
            if i != j and user == comments:
                duplicate_counter += 1
                if (j+1) not in duplicates and duplicate_counter > 0:
                    duplicates.append(j+1)

    # Tell the user which comment numbers are found to be multiple comments from a specific user
    print("duplicate comments were found at:")
    for comment in duplicates:
        print(f"comment number.{comment} by {allCommenters[comment-1]}")

    # Grab the total unique comments without the duplicates
    unique_commenters = list(set(allCommenters))
    allCommenters = unique_commenters
    print(f"after checking for duplicate user comments, the unique total number of comments is {len(allCommenters)} for the raffle wheel")

    allCommenters.clear()

while True:
    check_true_comments()
