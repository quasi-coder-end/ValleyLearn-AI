import json
import os
import glob

# Load JKBOSE syllabus data
def load_data():
    data_dir = "data/class_10_light.json/data"
    qa_list = []
    try:
        json_files = glob.glob(os.path.join(data_dir, '**', '*.json'), recursive=True)
        for file_path in json_files:
            with open(file_path, "r") as file:
                data = json.load(file)
                qa_list.extend(data["qa"])
        print(f"Loaded {len(qa_list)} Q&A items from {len(json_files)} files.")
        return {"qa": qa_list}
    except FileNotFoundError:
        print("Error: Data directory not found.")
        print("Make sure the data/ folder exists.")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON in data files.")
        exit()

# Match question using keywords
def find_answer(question, qa_list):
    question_lower = question.lower()
    matches = []
    max_score = 0

    for item in qa_list:
        score = sum(1 for k in item["keywords"] if k.lower() in question_lower)
        if score > max_score:
            max_score = score
            matches = [item]
        elif score == max_score:
            matches.append(item)

    return matches if max_score > 0 else []

def main():
    print("=" * 40)
    print("Valley Learn AI")
    print("Class 10 Physics – Light (JKBOSE)")
    print("=" * 40)

    data = load_data()
    qa_list = data["qa"]

    while True:
        question = input("\nAsk your question (or type 'exit'): ")

        if question.lower() == "exit":
            print("Exiting Valley Learn AI.")
            break

        matches = find_answer(question, qa_list)

        if not matches:
            print("\nThis question is not covered in the JKBOSE Class 10 syllabus.")
        elif len(matches) == 1:
            answer = matches[0]["answer"]
            print("\nAnswer:")
            if isinstance(answer, dict):
                for key, value in answer.items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print(answer)
        else:
            print("\nMultiple possible answers found. Please choose one:")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {', '.join(match['keywords'])}")
            while True:
                try:
                    choice = int(input("Enter the number of your choice: "))
                    if 1 <= choice <= len(matches):
                        answer = matches[choice-1]["answer"]
                        print("\nAnswer:")
                        if isinstance(answer, dict):
                            for key, value in answer.items():
                                print(f"{key.capitalize()}: {value}")
                        else:
                            print(answer)
                        break
                    else:
                        print(f"Invalid choice. Please enter a number between 1 and {len(matches)}")
                except ValueError:
                    print("Please enter a valid number.")

if __name__ == "__main__":
    main()
