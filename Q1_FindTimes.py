def count_occurences(limit_minutes: int) -> int:
    """
    count number of arithmetic numbers from 12:00 till the time specified in
    limit_minutes
    """
    count = 0
    hours = [12] + list(range(1,12))
    for hour in hours:
        for min in range(60):
            digits = [
                hour // 10,
                hour % 10,
                min // 10,
                min % 10
            ]

            diff1 = digits[1] - digits[0]
            diff2 = digits[2] - digits[1]
            diff3 = digits[3] - digits[2]

            if digits[0] == 1:
                if diff1 == diff2 and diff2 == diff3:
                    count += 1
            else:
                if diff2 == diff3:
                    count += 1

            if (hour % 12) * 60 + min >= limit_minutes:
                return count
    return count

def find_favorite_times(minutes: int) -> int:
    minInDozen = 12 * 60
    # left over minutes after a full clock cycle (12 hours)
    leftOver = count_occurences(minutes % minInDozen)
    # number of arithmetic numbers in a clock cycle mult by the number of cycles
    loopCount = count_occurences(minInDozen) * (minutes // minInDozen)

    return leftOver + loopCount


if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the number if minutes observed: "))
        except ValueError:
            print("Sorry, you must input a integer.")
            continue
        else:
            break
    arithmetic_nums = find_favorite_times((num))
    print(f"Number of arithmetic numbers observed: {arithmetic_nums}")
    
# Example:
# --------
# Input:
# 123456
# Output:
# 5321