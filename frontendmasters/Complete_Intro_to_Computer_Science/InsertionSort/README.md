### Insertion Sort

At insertion sort we take our first element of our array as sorted which means everything after the first element is unsorted.
This means that we start our comparison with the element on index one. 

This works somehow like bubble sort just reversed. We take our element on index one and check if the element is lager than on index zero. If our element on index 1 is not larger we move it to the right, and we have a new first element and a new second element since they both switched. 

In the next step we do the same but with the element on index two we check if the element on index two is larger than the element on index one. If our element on index 2 is lager then on index 1 we do nothing since they are on the correct position, so we go with the next one. 

| 3 | 2 | 5 | 4 | 1 |
|---|---|---|---|---|
1. Is arr[1] larger than arr[0]?  No, switch the places

| 2 | 3 | 5 | 4 | 1 |
|---|---|---|---|---|
1. Is arr[2] larger than arr[1]? Yes, do nothing

| 2 | 3 | 5 | 4 | 1 |
|---|---|---|---|---|
1. Is arr[3] larger than arr[2]? No, switch places
2. Is arr[2] (swapped) larger than arr[1]? Yes, do nothing

| 2 | 3 | 4 | 5 | 1 |
|---|---|---|---|---|
1. Is arr[4] larger than arr[3]? No, switch places
2. Is arr[3] (swapped) larger than arr[2]? No, switch places
3. Is arr[2] (swapped) larger than arr[1]? No switch places
4. Is arr[1] (swapped) larger than arr[0]? No switch places

End of list, list is sorted

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
