import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        #open the website
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to get {url}")
            return []
    
        #run beautifulsoup on the site
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #append the 20 puzzles from the site into results
        results = []
        for i in range(20):
            results.append(soup.find("li", value=i+1))
            
        puzzles = [item.text.strip() for item in results]
        
        #separate the puzzle into questions and answers
        questions = []
        answers = []
        for puzzle in puzzles:
            q = puzzle.split('Solution')[0]
            for i in range(len(q)-1):
                #clean the data by adding punctuation
                if(q[i].islower() and q[i+1].isupper()):
                    q = q[:i+1] + ": " + q[i+1:]
            questions.append(q)
            answers.append(puzzle.split('Solution')[1])
            
        return [questions, answers]
    #error handle any potential exceptions
    except Exception as e:
        print(f"An error has occured: {e}")
        
def main():
    site = "https://www.geeksforgeeks.org/top-20-puzzles-commonly-asked-during-sde-interviews/?ref=outind"
    qa = scrape_website(site)
    ques = qa[0]
    ans = qa[1]
    i = 0
    print("Answer the puzzle, enter END to stop")
    while(True):
        #cycle through each question and ask for an answer
        print(ques[i%20])
        x = input("Your Answer: ")
        
        #check if user wants to stop, else, provide a link to the answer and increment the counter
        if x.lower() == 'end':
            break
        else:
            print("Answer" + ans[i%20])
            i+=1
            
            
        
if __name__ == "__main__":
    main()