# 1 Two Sum
# gasim doua numere din lista care adunate dau target

def two_sum(nums, target):

    # dictionar pentru a retine numerele deja vazute
    seen = {}

    # parcurgem lista cu index si valoare
    for i, num in enumerate(nums):

        # calculam numarul complementar
        complement = target - num

        # verificam daca acel numar exista deja
        if complement in seen:

            # daca exista returnam indexurile
            return [seen[complement], i]

        # salvam numarul curent in dictionar
        seen[num] = i


print(two_sum([2,7,11,15], 9))


# 2 Palindrome Number
# verificam daca un numar citit invers este acelasi

def is_palindrome(x):

    # transformam numarul in string
    text = str(x)

    # verificam daca este egal cu inversul lui
    return text == text[::-1]


print(is_palindrome(121))
print(is_palindrome(123))


# 3 Maximum Subarray
# gasim suma maxima dintr-un subarray

def max_sub_array(nums):

    # initializam valorile
    max_current = nums[0]
    max_global = nums[0]

    # parcurgem lista incepand de la al doilea element
    for num in nums[1:]:

        # alegem valoarea maxima intre elementul curent
        # sau suma elementului curent cu suma anterioara
        max_current = max(num, max_current + num)

        # actualizam maximul global
        if max_current > max_global:
            max_global = max_current

    return max_global


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))


# 4 Binary Search
# cautam un element intr-o lista sortata

def binary_search(nums, target):

    # stabilim limitele cautarii
    left = 0
    right = len(nums) - 1

    # continuam cat timp intervalul este valid
    while left <= right:

        # calculam pozitia de mijloc
        mid = (left + right) // 2

        # verificam daca elementul este gasit
        if nums[mid] == target:
            return mid

        # daca elementul este mai mare cautam in dreapta
        elif nums[mid] < target:
            left = mid + 1

        # daca elementul este mai mic cautam in stanga
        else:
            right = mid - 1

    # daca nu este gasit
    return -1


print(binary_search([1,2,3,4,5,6], 4))



