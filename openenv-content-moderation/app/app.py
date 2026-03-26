from env.environment import ModerationEnvironment

def main():
    env = ModerationEnvironment()
    result = env.step("Test input")
    print(result)

if __name__ == "__main__":
    main()
