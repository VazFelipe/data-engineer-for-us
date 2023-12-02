# print(int(user_answer.split(':')[0]) + (60/int(user_answer.split(':')[1])))
# print(converted)

def main():
    user_answer = input('What time is it? ')
    time = convert(user_answer)
    if  7 <= time <= 8:
        print('breakfast time')
    if 12 <= time <= 13:
        print('lunch time')
    if 18 <= time <= 19:
        print('dinner time')

def convert(time):
    converted = int(time.split(':')[0]) + float('{:.2f}'.format((int(time.split(':')[1])/60)))
    return converted

if __name__ == "__main__":
    main()