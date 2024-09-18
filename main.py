import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to get {url}")
            return []
    
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = []
        for i in range(20):
            results.append(soup.find("li", value=i+1))
            
        puzzles = [item.text.strip() for item in results]
        
        questions = []
        answers = []
        for puzzle in puzzles:
            q = puzzle.split('Solution')[0]
            for i in range(len(q)-1):
                if(q[i].islower() and q[i+1].isupper()):
                    q = q[:i+1] + ": " + q[i+1:]
            questions.append(q)
            answers.append(puzzle.split('Solution')[1])
            
        return [questions, answers]
    
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
        print(ques[i%20])
        x = input("Your Answer: ")
        if x.lower() == 'end':
            break
        else:
            print("Answer" + ans[i%20])
            i+=1
            
            
        
if __name__ == "__main__":
    main()