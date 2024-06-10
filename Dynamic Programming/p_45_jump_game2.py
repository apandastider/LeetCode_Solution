'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



'''

## first attempt --- failed on some testcases

from collections import deque 
class Solution:
    def jump(self, nums: List[int]) -> int:

        curr_pos_ind = deque([0])

        curr_pos_list = deque([nums[0]])

        self.counter = 0

        def dfs(curr_pose_ind, curr_pos_list):
            print(curr_pos_ind, curr_pos_list)
            print(self.counter)
            if curr_pos_ind[-1] == len(nums)-1:
                # print("CC")
                return 1
            else:
                # print("FF")

                self.counter += 1

                pos = curr_pos_ind.popleft()
                val = curr_pos_list.popleft()

                for i in range(val):
                    curr_pos_ind.append(i+pos+1)
                    curr_pos_list.append(nums[i+pos+1])
                    if curr_pos_ind[-1] == len(nums) - 1:
                        break
                dfs(curr_pos_ind, curr_pos_list)
                # self.counter -= 1

        dfs(curr_pos_ind, curr_pos_list)

        return self.counter    

### 2nd attempt ---- fell into runtime error :( 

from collections import deque 
class Solution:
    def jump(self, nums: List[int]) -> int:

        curr_pos_ind = deque([0])

        curr_pos_list = deque([nums[0]])

        jump_count = deque([0])

        self.counter = 0

        def dfs(curr_pose_ind, curr_pos_list):
            # print(curr_pos_ind, curr_pos_list)
            # print(self.counter)
            if curr_pos_ind[-1] == len(nums)-1:
                # print("CC")
                return 1
            else:
                # print("FF")
                curr_jump = jump_count.popleft()
                self.counter = curr_jump + 1

                pos = curr_pos_ind.popleft()
                val = curr_pos_list.popleft()

                for i in range(val):
                    curr_pos_ind.append(i+pos+1)
                    curr_pos_list.append(nums[i+pos+1])
                    jump_count.append(self.counter)
                    if curr_pos_ind[-1] == len(nums) - 1:
                        break
                dfs(curr_pos_ind, curr_pos_list)
                # self.counter -= 1

        dfs(curr_pos_ind, curr_pos_list)

        return self.counter    
