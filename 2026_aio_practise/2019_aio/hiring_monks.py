N = int(input())
n = []
for i in range(N):
    n.append(int(input()))
n.sort()
S = int(input())
s = []
for i in range(S):
    s.append(int(input()))
s.sort()
M = int(input())
m = []
for i in range(M):
    m.append(int(input()))
m.sort()

# print(N, S, M)
# print(n, s, m)

small_pointer = 0
large_pointer = -1
skill_pointer = 0
master_pointer = -1
total_hired = 0

# Pointers to trace through arrays
# Lower end of monks array matches with Student Jobs (lowest skills match lowest limits)
s_job_ptr = 0
m_monk_ptr = 0 # Lowerbound of monks that can do student jobs

# Upper end of monks array matches with Master Jobs (highest skills match highest requirements)
m_job_ptr = M - 1
max_monk_ptr = N - 1

# Step 1: Greedily allocate Master Jobs from the top down
# We match the most skilled monks with the most restrictive master jobs
while max_monk_ptr >= m_monk_ptr and m_job_ptr >= 0:
    if n[max_monk_ptr] >= m[m_job_ptr]:
        # Monk qualifies for the master job
        total_hired += 1
        max_monk_ptr -= 1
        m_job_ptr -= 1
    else:
        # Job is too difficult even for our most skilled remaining monk; discard the job
        m_job_ptr -= 1

# Step 2: Greedily allocate Student Jobs from the bottom up
# The remaining pool of monks spans from m_monk_ptr to max_monk_ptr
while m_monk_ptr <= max_monk_ptr and s_job_ptr < S:
    if n[m_monk_ptr] <= s[s_job_ptr]:
        # Monk is qualified for the student job (skill <= limit)
        total_hired += 1
        m_monk_ptr += 1
        s_job_ptr += 1
    else:
        # Monk's skill is too high for this student job; try next available student job
        s_job_ptr += 1

print(total_hired)

