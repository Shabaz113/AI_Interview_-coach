from question_bank import questions
from feedback import generate_feedback


class InterviewCoach:

    def start_session(self, role):

        q_list = questions.get(role, questions["General"])

        for question in q_list:

            print("\nQuestion:")
            print(question)

            answer = input("\nYour Answer: ")

            strengths, improvements = generate_feedback(answer)

            print("\n--- Feedback ---")

            print("\nWhat Worked:")
            for s in strengths:
                print("-", s)

            print("\nWhat To Improve:")
            for i in improvements:
                print("-", i)

            print("\n----------------")
