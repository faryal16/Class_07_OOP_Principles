from models import QuizManager, UserProgress
from quiz_data import quiz_data
from termcolor import colored

def main():
    # Welcome message and asking for username
    print(colored("\t\t\n📘 Welcome to StudySync - Python Exam Prep 📘\n", 'cyan'))
    username = input("✍  Please enter your name: ")

    print(f"\nHello \033[1;3;35m{username}!\033[0m Let's get started with your Python exam preparation! 💪")

    user_progress = UserProgress()
    quiz_manager = QuizManager(quiz_data)

    while True:
        print("\nChoose an option:")
        print("1. Take quiz by topic")
        print("2. View my scores")
        print("3. Review incorrect answers")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            print("\nSelect a topic: 📚")
            topics = list(quiz_data.keys())
            for i, topic in enumerate(topics, 1):
                print(f"{i}. {topic}")
            topic_choice = int(input("\nEnter topic number: ")) - 1
            selected_topic = topics[topic_choice]
            quiz_manager.start_quiz(selected_topic)
            user_progress.update_score(selected_topic, quiz_manager.score, quiz_manager.total_questions)
        
        elif choice == '2':
            user_progress.view_score()

        elif choice == '3':
            print("\nFeature not implemented yet.")

        elif choice == '4':
            # Congratulatory message
            print(colored(f"\n🎉 Congrats {username}! You've completed your study session! 🎉", 'green'))
            print("\nExiting... Goodbye! 👋")
            break

        else:
            print("\n❌ Invalid choice, please try again. ❌")

if __name__ == "__main__":
    main()
