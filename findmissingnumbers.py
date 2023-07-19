"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #6 - WHERE ARE MY NUMBERS!? (findmissingnumbers.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: The Grand Prix was about to begin. The track was set, 
the cars were revved up, and the anticipation filled the air. 
As the race officials prepared for the event, they encountered a
problem that needed to be solved. The challenge was to analyze a list 
of numbers that represented checkpoints along the race track. 

These numbers were supposed to be in a specific sequence, but it 
seemed that some were missing. The officials needed to identify those
missing numbers before the race could commence.
Given a list of numbers that are in sequence, find the numbers missing in 
the sequence and output those numbers. You may assume the following:

1. The number sequence will NOT contain negatives.
2. The number sequence will NOT always start with the 
lowest value of the sequence and the last number in the sequence will
NOT always be the highest value in the sequence.
3. The numbers missing will always be in between the lowest value
and the highest values.
4. It matters not if numbers repeat or if they are scrambled, 
your duty is to find the numbers missing in betwixt the lowest and the highest
denary values. There may be floats.
5. If list is empty, output “Invalid input”
6. If list has only one number, output “None missing”

Test Cases: 
Input: [1, 2, 3, 5, 6]  Output: [4]

Input: [3, 4, 2, 1, 6, 7, 5, 9, 10] Output:[8]

Input: [3, 3, 3, 3, 4, 7] Output: [5, 6]

"""
def removeDuplicates(arr, n):
 
    # Return, if array is empty or contains
    # a single element
    if n == 0 or n == 1:
        return n
 
    temp = list(range(n))
 
    # Start traversing elements
    j = 0
    for i in range(0, n-1):
 
        # If current element is not equal to next
        # then store that current element
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1
 
    # Store the last element as whether it is unique
    # or repeated, it isn't stored previously
    temp[j] = arr[n-1]
    j += 1
    arr=[]
    # Modify original array
    for i in range(0, j):
        arr.append(temp[i])
    return arr


class Solution:
    def findMissingNumbers(self, numbers):
      if len(numbers) == 0:
        print("Invalid input")
        return None
      if len(numbers) == 1:
        print("None missing")
      maxnum=0
      minnum=1000000000
      missingnums=[]
      for num in numbers:
        maxnum=max(maxnum, num)
        minnum=min(minnum, num)
      for i in range(int(minnum), int(maxnum+1)):
        if not (i in numbers):
          missingnums.append(i)
      return missingnums
          

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = float(array[x])

    tc1 = Solution()
    ans = tc1.findMissingNumbers(array)
    print(ans)

if __name__ == "__main__":
    main()
    
#listOfNumbers = [0, 3, 3, 3, 4, 7, 3]  # STEP 1: get the in input
#print(findMissingNumbers(listOfNumbers)) # Step 2: Call a function to handle the input