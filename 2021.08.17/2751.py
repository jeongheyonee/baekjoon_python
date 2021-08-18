# 로그 선형 정렬
# n = int(input())
#
# l = []
#
# for _ in range(n):
#     l.append(int(input()))
#
# sort 함수 이용 - 원본 변경
# l.sort()
#
# sorted 이용 - 원본 변형 X
# l = sorted(l)

# 병합정렬: 리스트를 반으로 나누어 정렬되지 않은 리스트를 만듦
# 특징: 안정적, 대규모 데이터에 대해 속도가 빠름
# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])
#
#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr
#
# l = merge_sort(l)

# 힙정렬: 완전 이진 트리의 일종
# max heap 트리로 배열의 순서를 바꿔줘서 오름차순으로 정렬
def heapSort(unsorted):
    n = len(unsorted)
    # 최대 힙을 구하는 반복문
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    # 오름 차순으로 정렬하는 부분
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]  # 자리를 바꿔줌으로서 젤 큰 값을 맨 뒤로 보내주게 된다
        heapify(unsorted, 0, i)  # 맨 뒤로 보낸 값 빼고 다시 max heap으로 바꿔준다

    return unsorted


# 리스트를 max heap으로 바꾸는 함수
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1  # 트리에서 왼쪽 노드는 기존 인덱스에 2를 곱하고 더하기 1을 한 것이고,
    right_index = 2 * index + 2  # 오른쪽 노드는 기존 인덱스에 2를 곱하고 더하기 2를 한 것이다

    # 만약 왼쪽 인덱스가 힙 사이즈보다 작고, 트리 왼쪽 값이 트리에서 가장 큰 값보다 크다면 왼쪽 인덱스를 largest로 바꾼다
    # left_index가 2*index+1이여서 리스트의 범위를 벗어나는 경우가 있기 때문에 확인 해야 한다
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    # 오른쪽도 마찬가지로 해준다
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    # largest가 기존에 예상했던 index가 아니라면 largest와 index의 자리를 바꿔준다, 즉 트리의 노드를 바꿔주는 것
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


m = int(input())
arr = []
for i in range(m):
    arr.append(int(input()))
arr = heapSort(arr)
for i in range(m):
    print(arr[i])


# for i in l:
#     print(i)