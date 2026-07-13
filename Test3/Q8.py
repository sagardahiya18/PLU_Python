'''8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.'''



patients = input("Enter patient names: ").split()
prior = list(map(int, input("Enter priority level:").split()))


n = len(prior)
for i in range(n):
    for j in range(0, n - i - 1):
        if prior[j] < prior[j + 1]:
            prior[j], prior[j + 1] = prior[j + 1], prior[j]
            patients[j], patients[j + 1] = patients[j + 1], patients[j]

print("Highest Priority First:")
for i in range(n):
    print("Patient:", patients[i], ", Priority:", prior[i])

