def arithmetic_arranger(problems):
    arranged_problems = ""
    
    for problem in problems:
        words = problem.split()
        print(f"{words[0]}")
        print(words[1], words[2])
        print("----")

    return arranged_problems
