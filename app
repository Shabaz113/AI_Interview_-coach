from interview_coach import InterviewCoach

def main():
    coach = InterviewCoach()

    print("=== AI Interview Coach ===")
    role = input("Enter target role: ")

    coach.start_session(role)

if __name__ == "__main__":
    main()
