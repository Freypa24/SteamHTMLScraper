Developed on October 8, 2024
By Lance Gabriel Trias

Overview:
  Our community are doing a giveaway program inside steam discussion page.
  The giveaway procedure takes a total number of comments and then randomly selects a number, whichever the system picks, that is going to be the winner.
  However, the problem arises when there are multiple comments from various users. We strictly implement only 1 entry per user to ensure fairness and order. But there would be times users fail to follow instructions.
  There is also the "per number" issue if there are too many comments in one page, emphasizing the need of automation in reading all pages for comments until the final comment has been reached.

Program:
  This program takes a url input from the user, the html content(Steam discussion Page), and finds the comment section. It then reads each individual comments and users to check if there are multiple comments from any user.
  If so, we fix the list by finding the placement in the comment section of each multiple comments and counts the true total number of comments. 
  It showcases the total number of unfiltered comments, tells the user which comment is multiple and by whom, the order of commenting users, and the total number of filtered comments(for the giveaway procedure)
  Another feature is the ability for the program to read all corresponding pages for comments, without the need for the user to grab the html link of each page number until the final comment.
