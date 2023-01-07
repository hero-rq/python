def merge_sort(arr):
    # 배열의 길이가 1보다 크면 수행
    if len(arr) > 1:
        # 중간 지점을 구함
        mid = len(arr) // 2
        # 왼쪽 부분 배열
        left = arr[:mid]
        # 오른쪽 부분 배열
        right = arr[mid:]

        # 재귀 호출을 통해 왼쪽, 오른쪽 부분 배열을 정렬
        merge_sort(left)
        merge_sort(right)

        # 병합 작업 시작
        i = j = k = 0
        while i < len(left) and j < len(right):
            # 왼쪽 부분 배열의 첫 번째 값과 오른쪽 부분 배열의 첫 번째 값을 비교하여
            # 작은 값을 새로운 배열에 삽입
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # 왼쪽 부분 배열에 남은 값이 있으면 삽입
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # 오른쪽 부분 배열에 남은 값이 있으면 삽입
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# 정렬할 배열
arr = [5, 2, 1, 3, 4]
# 정렬 수행
merge_sort(arr)
# 정렬된 결과 출력
print(arr)
